from selenium import webdriver
import pandas as pd #data processing, CSV I/O
import datetime
import time

def getDemand():
  # converts datetime object ot ISO format
  def toISO (x):
    return datetime.datetime.strptime(x, "%Y-%m-%dT%H:%M:00.000Z")

  # Split df.Time into sub-columns for easier sorting
  def reformat_df(df):
    df['Year'] = df.Time.apply(lambda x: int(str(x)[:4]))
    df['Month'] = df.Time.apply(lambda x: int(str(x)[5:7]))
    df['Day'] = df.Time.apply(lambda x: int(str(x)[8:10]))
    df['Hour'] = df.Time.apply(lambda x: int(str(x)[11:13]))
    df['Time'] = df['Time'].apply(toISO)
    df.Demand.fillna(df.Forecast, inplace=True)
    df.drop(['Time', 'Forecast'], axis=1, inplace = True)
    df.reset_index(drop=True)

  # Combine sub-columns back into df.Time
  def CombineTime(df):
    df['Time'] = df.apply(lambda row: '{day:2.0f}/{month:.0f}/{year:2.0f} {hour:2.0f}:00'.format(day=row['Day'], month=row['Month'], year=row['Year'] % 2000, hour=row['Hour']), axis = 1)
    df.drop(['Day', 'Year', 'Month', 'Hour'], inplace = True, axis = 1)
    df.reset_index(drop=True)

  # chromium settings for web scraper
  chrome_options = webdriver.ChromeOptions()
  chrome_options.add_argument('--headless')
  chrome_options.add_argument('--no-sandbox')
  chrome_options.add_argument('--disable-dev-shm-usage')
  prefs = {"download.default_directory" : "/content/"};
  chrome_options.add_experimental_option("prefs",prefs);

  # pull Highcharts demand data from ieso.ca
  web = webdriver.Chrome('chromedriver', options=chrome_options)
  url = "https://www.ieso.ca/power-data"
  web.get(url)
  time.sleep(3)
  dates = web.execute_script('return Highcharts.charts[0].series[3].data.map(x => x.series).map(x => x.xData)[0].map(x => new Date(x).toISOString())')
  actual_values = web.execute_script('return Highcharts.charts[0].series[3].data.map(x => x.series).map(x => x.yData)[0]')
  forecast_values = web.execute_script('return Highcharts.charts[0].series[5].data.map(x => x.series).map(x => x.yData)[0]')
  web.quit()

  # convert demand data to Dataframe
  df = pd.DataFrame({'Time': dates, 'Demand': actual_values, 'Forecast': forecast_values })
  reformat_df(df)

  # time-zone shift correction
  hours = range(24)
  # 4 am UTC = 12 am EST
  if (datetime.datetime.today().hour >= 4):
    first_index_pred = df[(df.Day == datetime.datetime.today().day-1) & (df.Hour == hours[datetime.datetime.today().hour - 4 - 1]) & (df.Month == datetime.datetime.today().month)].index[0]
    first_index_plot = df[(df.Day == datetime.datetime.today().day-1) & (df.Hour == 0) & (df.Month == datetime.datetime.today().month)].index[0]#remove first -1
  else:
    first_index_pred = df[(df.Day == datetime.datetime.today().day-2) & (df.Hour == hours[datetime.datetime.today().hour - 4 - 1]) & (df.Month == datetime.datetime.today().month)].index[0]
    first_index_plot = df[(df.Day == datetime.datetime.today().day-1) & (df.Hour == 0) & (df.Month == datetime.datetime.today().month)].index[0]
  last_index_pred = first_index_pred + 24
  last_index_plot = first_index_plot + 24

  # reshape and split data into two Dataframes
  # pred dataset is for producing LSTM prediction
  pred = df[first_index_pred:last_index_pred]
  pred.reset_index(drop=True)
  # plot is for plotting the Recharts API graph
  plot = df[first_index_plot:last_index_plot]
  plot.reset_index(drop=True)

  # reformat each Dataframe and export as .csv
  CombineTime(pred)
  CombineTime(plot)
  df = pd.merge(pred, plot)
  return df