from selenium import webdriver
import pandas as pd
import datetime
import time

# disable warnings about copying Dataframes
pd.options.mode.chained_assignment = None


# def getDemand():
# converts datetime object ot ISO format
def toISO(x):
    return datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:00.000Z")


# Split df.Time into sub-columns for easier sorting
def reformat_df(df):
    df['Year'] = df.Time.apply(lambda x: int(str(x)[:4]))
    df['Month'] = df.Time.apply(lambda x: int(str(x)[5:7]))
    df['Day'] = df.Time.apply(lambda x: int(str(x)[8:10]))
    df['Hour'] = df.Time.apply(lambda x: int(str(x)[11:13]))
    df['Time'] = df['Time'].apply(toISO)
    df.Demand.fillna(df.Forecast, inplace=True)
    df.drop(['Time', 'Forecast'], axis=1, inplace=True)
    df = df.reset_index(drop=True)


# Combine sub-columns back into df.Time
def CombineTime(df):
    df['Time'] = df.apply(
        lambda row: '{day:2.0f}/{month:.0f}/{year:2.0f} {hour:2.0f}:00'.format(day=row['Day'], month=row['Month'],
                                                                               year=row['Year'] % 2000,
                                                                               hour=row['Hour']), axis=1)
    df.drop(['Day', 'Year', 'Month', 'Hour'], inplace=True, axis=1)
    df = df.reset_index(drop=True)


# chromium settings for web scraper
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
prefs = {"download.default_directory": "/content/"};
chrome_options.add_experimental_option("prefs", prefs);

# pull Highcharts demand data from ieso.ca
web = webdriver.Chrome('chromedriver', options=chrome_options)
url = "https://www.ieso.ca/power-data"
web.get(url)
time.sleep(3)
dates = web.execute_script(
    'return Highcharts.charts[0].series[3].data.map(x => x.series).map(x => x.xData)[0].map(x => new Date('
    'x).toISOString())')
actual_values = web.execute_script(
    'return Highcharts.charts[0].series[3].data.map(x => x.series).map(x => x.yData)[0]')
forecast_values = web.execute_script(
    'return Highcharts.charts[0].series[5].data.map(x => x.series).map(x => x.yData)[0]')
web.quit()

# convert demand data to Dataframe
df = pd.DataFrame({'Time': dates, 'Demand': actual_values, 'Forecast': forecast_values})
reformat_df(df)

# time-zone shift correction
now = datetime.datetime.now()
start_time = now - datetime.timedelta(days=2)
end_time = now

# determine time range to collect data for
first_index_pred = \
    df[(df.Day == start_time.day) & (df.Hour == 23) & (df.Month == start_time.month)].index[0]
first_index_plot = df[(df.Day == now.day) & (df.Hour == 0) & (df.Month == now.month)].index[0]

last_index_pred = \
    df[(df.Day == end_time.day) & (df.Hour == 23) & (df.Month == end_time.month)].index[0]
last_index_plot = df[(df.Day == now.day) & (df.Hour == now.hour) & (df.Month == now.month)].index[0]

# reshape and split data into two Dataframes
# pred dataset is for producing LSTM prediction
pred = df.iloc[first_index_pred:last_index_pred+1]
pred.reset_index(drop=True)
# plot is for plotting the Recharts API graph
plot = df.iloc[first_index_plot:last_index_plot]
plot.reset_index(drop=True)

# reformat each Dataframe and export as .csv
CombineTime(pred)
CombineTime(plot)
# df = pd.concat([plot, pred], ignore_index=True, axis=1)
plot.drop(['Time'], inplace=True, axis=1)
pred.drop(['Time'], inplace=True, axis=1)
plot.to_csv('real_demand.csv', index=False, header=False)
pred.to_csv('demand.csv', index=False, header=False)
# return plot, pred
