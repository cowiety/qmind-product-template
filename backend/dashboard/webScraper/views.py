from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import pandas as pd
import numpy as np
import getDemand
import getHoliday
import getWeather

def normalize(data):
  data_mean = data[:].mean(axis=0)
  data_std = data[:].std(axis=0)
  return (data-data_mean) / data_std

# Class based view to produce new model data
class Data_Creation(APIView):

    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        data = request.data

        demand = getDemand().to_numpy()
        holday = getHoliday().to_numpy()
        weather = getWeather().to_numpy()

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

        with open('input.json', "w") as f:
            json.dump(input, f)

        return Response(input, status=200)