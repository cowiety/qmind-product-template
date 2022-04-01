from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import numpy as np

def normalize(data):
  data_mean = data[:].mean(axis=0)
  data_std = data[:].std(axis=0)
  return (data-data_mean) / data_std

# Class based view to produce new model data
class Data_Creation(APIView):
    def post(self, request, format=None):
        data = request.data

        # open uploaded csv file and generate numpy array from file
        demand_file = open('Demand.csv')
        demand = np.genfromtxt(demand_file, delimiter=',', skip_header=1, usecols=(0))
        weather_file = open('Weather.csv')
        weather = np.genfromtxt(weather_file, delimiter=',', skip_header=1, usecols=(1, 2, 3, 4))
        holiday_file = open('isHoliday.csv')
        holiday = np.genfromtxt(holiday_file, delimiter=',', skip_header=1, usecols=(1))

        # normalize weather and demand data
        weather = normalize(weather)
        weather = weather[0:demand.shape[0]]
        demand = demand / 1000

        # splitting weather array into a dictionary called weather_comp
        weather_comp = np.split(weather, 4, axis=1)

        # split each weather feature into its own rray
        clouds = weather_comp[0]
        temp = weather_comp[1]
        humidity = weather_comp[2]
        wind = weather_comp[3]
        holiday = holiday[0:demand.shape[0]]

        # convert numpy arrays to a dictionary
        input = {
            'demand': demand.tolist(),
            'holiday': holiday.tolist(),
            'clouds': clouds.tolist(),
            'temp': temp.tolist(),
            'humidity': humidity.tolist(),
            'wind': wind.tolist()
        }

        return Response(input, status=200)