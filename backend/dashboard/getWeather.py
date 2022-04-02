import requests
import pandas as pd
import datetime
import calendar
import time

cities = {
    "Toronto": [43.7001, -79.4163, 5429524],
    "Ottawa": [45.4112, -75.6981, 989567],
    "Hamilton": [43.2334, -79.9496, 693645],
    "Kitchener": [43.4254, -80.5112, 470015],
    "London": [42.9834, -81.233, 383437],
    "Oshawa": [43.9001, -78.8496, 308875],
    "Windsor": [42.3001, -83.0165, 287069],
    "St. Catharines": [43.1668, -79.2496, 229246],
    "Barrie": [44.4001, -79.6663, 145614],
    "Guelph": [43.5501, -80.2497, 132397],
    "Kingston": [44.2298, -76.481, 117660]
}
total_pop = 9187049
api_key = "1ae675d5ed1ea683ef55260eef326480"


def get_forecast_weather(city):
    # format city dictionary into API parameters
    lat = cities[city][0]
    lon = cities[city][1]
    url = f"https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=current,minutely,daily," \
          f"alerts&appid={api_key} "

    # pulls API request and converts to json
    response = requests.get(url).json()
    print(response)
    # initialize 4 empty lists
    hours, clouds, temp, humidity, w_speed = [], [], [], [], []

    # looping through next 24 hours of weather data
    for i in range(0, 24):
        hour = time.gmtime(int(response['hourly'][i]['dt'] + response['timezone_offset']))[3]
        hours.append(hour)
        cloudiness = response['hourly'][i]['clouds']
        clouds.append(cloudiness)
        temperature = "{:.2f}".format(response['hourly'][i]['temp'] - 273.15)
        temp.append(float(temperature))
        humidex = response['hourly'][i]['humidity']
        humidity.append(humidex)
        wind = response['hourly'][i]['wind_speed']
        w_speed.append(wind)
    return hours, clouds, temp, humidity, w_speed


def get_historical_weather(city):
    # format city dictionary into API parameters
    lat = cities[city][0]
    lon = cities[city][1]
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1, hours=5)
    yesterday = calendar.timegm(yesterday.utctimetuple())

    url = f"https://api.openweathermap.org/data/2.5/onecall/timemachine?lat={lat}&lon={lon}&dt={yesterday}&appid={api_key}"

    # pulls API request and converts to json
    response = requests.get(url).json()
    print(response)
    # initialize 4 empty lists
    hours, clouds, temp, humidity, w_speed = [], [], [], [], []
    # looping through next 24 hours of weather data
    for i in range(0, 24):
        hour = time.gmtime(int(response['hourly'][i]['dt'] + response['timezone_offset']))[3]
        hours.append(hour)
        cloudiness = response['hourly'][i]['clouds']
        clouds.append(cloudiness)
        temperature = "{:.2f}".format(response['hourly'][i]['temp'] - 273.15)
        temp.append(float(temperature))
        humidex = response['hourly'][i]['humidity']
        humidity.append(humidex)
        wind = response['hourly'][i]['wind_speed']
        w_speed.append(wind)
    return hours, clouds, temp, humidity, w_speed


# start of forecast data
weighted_clouds, weighted_temp, weighted_humidity, weighted_w_speed = [], [], [], []
for city in cities:
    hours, clouds, temp, humidity, w_speed = get_forecast_weather(city)

    # weight each city's data point according to the population of that city
    clouds = [element * cities[city][2] for element in clouds]
    temp = [element * cities[city][2] for element in temp]
    humidity = [element * cities[city][2] for element in humidity]
    w_speed = [element * cities[city][2] for element in w_speed]

    # concatenate the data from each city into individual arrays for data processing later
    weighted_clouds = weighted_clouds + clouds
    weighted_temp = weighted_temp + temp
    weighted_humidity = weighted_humidity + humidity
    weighted_w_speed = weighted_w_speed + w_speed

# initialize 4 empty lists
ave_clouds, ave_temp, ave_humidity, ave_w_speed = [0] * 24, [0] * 24, [0] * 24, [0] * 24

# loop through the concatenated array for each hour of the day
for i in range(len(hours)):
    # loop through the same concatenated array for each city
    for j in range(len(cities)):
        # since there are 24 hours x 11 cities in each list
        # [j*24 + i - 1] collects all data for the ith hour
        ave_clouds[i] = ave_clouds[i] + weighted_clouds[j * 24 + i - 1]
        ave_temp[i] = ave_temp[i] + weighted_temp[j * 24 + i - 1]
        ave_humidity[i] = ave_humidity[i] + weighted_humidity[j * 24 + i - 1]
        ave_w_speed[i] = ave_w_speed[i] + weighted_w_speed[j * 24 + i - 1]

# format the temperature and wind speed to 3 decimal places
formatter = "{0:.3f}"
# format the data appropriately and divide each element by the total population
ave_clouds = [round(element / total_pop) for element in ave_clouds]
ave_temp = [formatter.format(element / total_pop) for element in ave_temp]
ave_humidity = [round(element / total_pop) for element in ave_humidity]
ave_w_speed = [formatter.format(element / total_pop) for element in ave_w_speed]

# format all the data into a new DataFrame
data = {'Hour': hours,
        'Cloudiness (%)': ave_clouds,
        'Temp (°C)': ave_temp,
        'Humidity (%)': ave_humidity,
        'Wind Speed (m/s)': ave_w_speed
        }
forecast = pd.DataFrame(data)

# historical code
weighted_clouds, weighted_temp, weighted_humidity, weighted_w_speed = [], [], [], []
for city in cities:
    hours, clouds, temp, humidity, w_speed = get_historical_weather(city)

    # weight each city's data point according to the population of that city
    clouds = [element * cities[city][2] for element in clouds]
    temp = [element * cities[city][2] for element in temp]
    humidity = [element * cities[city][2] for element in humidity]
    w_speed = [element * cities[city][2] for element in w_speed]

    # concatenate the data from each city into individual arrays for data processing later
    weighted_clouds = weighted_clouds + clouds
    weighted_temp = weighted_temp + temp
    weighted_humidity = weighted_humidity + humidity
    weighted_w_speed = weighted_w_speed + w_speed

# initialize 4 empty lists
ave_clouds, ave_temp, ave_humidity, ave_w_speed = [0] * 24, [0] * 24, [0] * 24, [0] * 24

# loop through the concatenated array for each hour of the day
for i in range(len(hours)):
    # loop through the same concatenated array for each city
    for j in range(len(cities)):
        # since there are 24 hours x 11 cities in each list
        # [j*24 + i - 1] collects all data for the ith hour
        ave_clouds[i] = ave_clouds[i] + weighted_clouds[j * 24 + i - 1]
        ave_temp[i] = ave_temp[i] + weighted_temp[j * 24 + i - 1]
        ave_humidity[i] = ave_humidity[i] + weighted_humidity[j * 24 + i - 1]
        ave_w_speed[i] = ave_w_speed[i] + weighted_w_speed[j * 24 + i - 1]

# format the temperature and wind speed to 3 decimal places
formatter = "{0:.3f}"
# format the data appropriately and divide each element by the total population
ave_clouds = [round(element / total_pop) for element in ave_clouds]
ave_temp = [formatter.format(element / total_pop) for element in ave_temp]
ave_humidity = [round(element / total_pop) for element in ave_humidity]
ave_w_speed = [formatter.format(element / total_pop) for element in ave_w_speed]

# format all the data into a new DataFrame
data = {'Hour': hours,
        'Cloudiness (%)': ave_clouds,
        'Temp (°C)': ave_temp,
        'Humidity (%)': ave_humidity,
        'Wind Speed (m/s)': ave_w_speed
        }
historical = pd.DataFrame(data)

if int(historical.iloc[-1, 0]) != int(forecast.iloc[1, 0]) - 1:
    diff = forecast.iloc[1, 0] - historical.iloc[-1, 0]
    print(diff)
    for i in range(1, diff+1):
        print('added extra row value of ' + str(historical.iloc[-i, 0] + i))
        historical = historical.append({'Hour': int(historical.iloc[-i, 0]) + i}, ignore_index=True)
print(historical.head(30))
print(forecast.head(30))
'''
df = pd.concat([historical, forecast], axis=0)
df = df[(24-datetime.datetime.now().hour):-(int(datetime.datetime.now().hour))]
df = df.fillna(method='ffill', axis=0)
df = df.reset_index(drop=True)
df.to_csv('weather.csv', index=False, header=False)
'''