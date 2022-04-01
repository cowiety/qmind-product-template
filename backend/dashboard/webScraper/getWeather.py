import pandas as pd #data processing, CSV I/O
import requests
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
import datetime

# chromium settings for web scraper
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
prefs = {"download.default_directory" : "/content/"};
chrome_options.add_experimental_option("prefs",prefs);

cities = { # declare dictionary with relevant coordinates and population
                  "toronto": [43.7001, -79.4163, 5429524],
                  "ottawa": [45.4112, -75.6981, 989567],
                  "hamilton": [43.2334, -79.9496, 693645],
                  "kitchenerwaterloo": [43.4254, -80.5112, 470015],
                  "london": [42.9834, -81.233, 383437],
                  "oshawa": [43.9001, -78.8496, 308875],
                  "windsoron": [42.3001, -83.0165, 287069],
                  "stcatharines": [43.1668, -79.2496, 229246],
                  "barrie": [44.4001, -79.6663, 145614],
                  "guelph": [43.5501, -80.2497, 132397],
                  "kingston": [44.2298, -76.481, 117660]
}
# sum of all the populations listed above
total_pop = 9187049
# number of hours to request
hour_length = 24
dfs = {}

# pull the weather data from weatherstats.ca for each city in cities
for city in cities:
    # initialize an HTTP session
    web = webdriver.Chrome('chromedriver', options=chrome_options)
    url = f"https://{city}.weatherstats.ca/download.html"#{city}
    web.get(url)
    download_type = web.find_element_by_xpath('//*[@id="form_download"]/label[2]')
    download_type.click()
    row_limit = web.find_element_by_xpath('//*[@id="form_download"]/label[9]')
    row_limit.click()
    row_limit.send_keys(Keys.CONTROL + 'a')
    row_limit.send_keys(Keys.DELETE)
    row_limit.send_keys(hour_length)
    row_limit.send_keys(Keys.RETURN)
    time.sleep(3)
    web.quit()

    # import data from webscraper into Dataframe
    filename = f"weatherstats_{city}_hourly.csv"
    df = pd.read_csv(filename)
    # convert timestamps to datetime objects
    df['Time'] = pd.to_datetime(df['unixtime'], unit='s')
    # cut off current hour to fit dataset
    if (df.iloc[-1, -1].hour == datetime.datetime.now().hour):
      df = df.iloc[:-2, :]
    # data cleaning
    if (df.cloud_cover_10.isnull().all() == False):
      df['Cloudiness (%)'] = df['cloud_cover_10'] * 10
    elif (df.cloud_cover_8.isnull().all() == False):
      df['Cloudiness (%)'] = df['cloud_cover_8'] * 12.5
    else:
      df['Cloudiness (%)'] = df['cloud_cover_4'] * 25
    df['Cloudiness (%)'] = df['Cloudiness (%)'].fillna(0)
    df['Temp (°C)'] = df['temperature']
    df['Humidity (%)'] = df['relative_humidity']
    df['Wind Speed (m/s)'] = df.apply(lambda row: row['wind_speed'] * 0.2777778, axis=1)
    df.drop(['date_time_local', 'unixtime', 'pressure_station', \
           'pressure_sea', 'wind_dir', 'wind_dir_10s', \
           'wind_speed', 'wind_gust', 'relative_humidity', \
           'dew_point', 'temperature', 'windchill', 'humidex', \
           'visibility', 'health_index', 'cloud_cover_4', \
           'cloud_cover_8', 'cloud_cover_10', 'solar_radiation', \
           'max_air_temp_pst1hr', 'min_air_temp_pst1hr'], axis=1, inplace=True)
    df = df.sort_values(by="Time")
    # place the weather data for each city into a dictionary
    dfs['{}'.format(city)] = df

# perform weighted average calculations
# create new Dataframe ave, which will be the population-weighted average of all weather data
ave = pd.DataFrame(data=None, columns=['Time', 'Cloudiness (%)', 'Temp (°C)', 'Humidity (%)', 'Wind Speed (m/s)'])
ave.Time = dfs['barrie'].Time
ave['Cloudiness (%)'] = ( dfs['hamilton']['Cloudiness (%)'] * cities['hamilton'][2] + \
                         dfs['kingston']['Cloudiness (%)'] * cities['kingston'][2] + \
                         dfs['kitchenerwaterloo']['Cloudiness (%)'] * cities['kitchenerwaterloo'][2] + \
                         dfs['london']['Cloudiness (%)'] * cities['london'][2] + \
                         dfs['oshawa']['Cloudiness (%)'] * cities['oshawa'][2] + \
                         dfs['ottawa']['Cloudiness (%)'] * cities['ottawa'][2] + \
                         dfs['stcatharines']['Cloudiness (%)'] * cities['stcatharines'][2] + \
                         dfs['toronto']['Cloudiness (%)'] * cities['toronto'][2] + \
                         dfs['windsoron']['Cloudiness (%)'] * cities['windsoron'][2] ) / (total_pop - cities['guelph'][2] - cities['barrie'][2]) # guelph and barrie show NaN values
ave['Temp (°C)'] = ( dfs['barrie']['Temp (°C)'] * cities['barrie'][2] + \
                         dfs['hamilton']['Temp (°C)'] * cities['hamilton'][2] + \
                         dfs['kingston']['Temp (°C)'] * cities['kingston'][2] + \
                         dfs['kitchenerwaterloo']['Temp (°C)'] * cities['kitchenerwaterloo'][2] + \
                         dfs['london']['Temp (°C)'] * cities['london'][2] + \
                         dfs['oshawa']['Temp (°C)'] * cities['oshawa'][2] + \
                         dfs['ottawa']['Temp (°C)'] * cities['ottawa'][2] + \
                         dfs['stcatharines']['Temp (°C)'] * cities['stcatharines'][2] + \
                         dfs['toronto']['Temp (°C)'] * cities['toronto'][2] + \
                         dfs['windsoron']['Temp (°C)'] * cities['windsoron'][2] ) / (total_pop - cities['guelph'][2])  # guelph shows NaN values
ave['Humidity (%)'] = ( dfs['barrie']['Humidity (%)'] * cities['barrie'][2] + \
                         dfs['guelph']['Humidity (%)'] * cities['guelph'][2] + \
                         dfs['hamilton']['Humidity (%)'] * cities['hamilton'][2] + \
                         dfs['kingston']['Humidity (%)'] * cities['kingston'][2] + \
                         dfs['kitchenerwaterloo']['Humidity (%)'] * cities['kitchenerwaterloo'][2] + \
                         dfs['london']['Humidity (%)'] * cities['london'][2] + \
                         dfs['oshawa']['Humidity (%)'] * cities['oshawa'][2] + \
                         dfs['ottawa']['Humidity (%)'] * cities['ottawa'][2] + \
                         dfs['stcatharines']['Humidity (%)'] * cities['stcatharines'][2] + \
                         dfs['toronto']['Humidity (%)'] * cities['toronto'][2] + \
                         dfs['windsoron']['Humidity (%)'] * cities['windsoron'][2] ) / total_pop
ave['Wind Speed (m/s)'] = ( dfs['barrie']['Wind Speed (m/s)'] * cities['barrie'][2] + \
                         dfs['hamilton']['Wind Speed (m/s)'] * cities['hamilton'][2] + \
                         dfs['kingston']['Wind Speed (m/s)'] * cities['kingston'][2] + \
                         dfs['kitchenerwaterloo']['Wind Speed (m/s)'] * cities['kitchenerwaterloo'][2] + \
                         dfs['london']['Wind Speed (m/s)'] * cities['london'][2] + \
                         dfs['oshawa']['Wind Speed (m/s)'] * cities['oshawa'][2] + \
                         dfs['ottawa']['Wind Speed (m/s)'] * cities['ottawa'][2] + \
                         dfs['stcatharines']['Wind Speed (m/s)'] * cities['stcatharines'][2] + \
                         dfs['toronto']['Wind Speed (m/s)'] * cities['toronto'][2] + \
                         dfs['windsoron']['Wind Speed (m/s)'] * cities['windsoron'][2] ) / (total_pop - cities['guelph'][2]) # guelph shows NaN values

# clean up data values
ave = ave.round({'Cloudiness (%)': 2, 'Temp (°C)': 2, 'Humidity (%)': 2, 'Wind Speed (m/s)': 3})
# fill any leftover NaN values
ave.interpolate(inplace=True)
# export weather Dataframe to .csv file
ave.to_csv('Weather.csv'.format(datetime.datetime.today().year, datetime.datetime.today().month, datetime.datetime.today().day), index = False)