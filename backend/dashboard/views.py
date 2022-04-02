from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from dashboard.apps import PredictionConfig
import pandas as pd
import numpy as np


def flatten_list(_2d_list):
    flat_list = []
    # Iterate through the outer list
    for element in _2d_list:
        if type(element) is list:
            # If the element is of type list, iterate through the sublist
            for item in element:
                flat_list.append(item)
        else:
            flat_list.append(element)
    return flat_list


def normalize(data):
    data_mean = data[:].mean(axis=0)
    data_std = data[:].std(axis=0)
    return (data - data_mean) / data_std


# Create your views here.
# Class based view to predict based on IRIS model
class Demand_Model_Predict(APIView):

    def post(self, request, format=None):
        # data = request.data

        holiday = pd.read_csv('dashboard/holiday.csv')
        time = holiday.iloc[1, :]
        holiday = pd.read_csv('dashboard/holiday.csv')
        holiday = np.asarray(pd.read_csv('dashboard/holiday.csv'))
        holiday = np.delete(holiday, 0, 1).astype('float32')
        demand = np.asarray(pd.read_csv('dashboard/demand.csv')).astype('float32')
        demand = demand / 1000

        weather = np.asarray(pd.read_csv('dashboard/weather.csv')).astype('float32')
        weather = normalize(weather)
        weather_comp = np.split(weather, 4, axis=1)
        clouds = weather_comp[0]
        temp = weather_comp[1]
        humidity = weather_comp[2]
        wind = weather_comp[3]

        data = np.column_stack((demand, holiday, clouds, temp, humidity, wind))

        forecast = []
        for i in range(data.shape[0] - 24):
            pred_data = data[i: i + 24, :]
            pred_data = pred_data.reshape(1, 24, 6)

            loaded_mlmodel = PredictionConfig.mlmodel
            yhat = loaded_mlmodel.predict(pred_data)

            yhat = yhat * 1000
            forecast.append(int(yhat))

        demand = []
        i = 0
        for element in forecast:
            demand.append(float(element))
            i += 1

        path = open('dashboard/real_demand.csv')
        real_demand = np.loadtxt(path, delimiter=",", dtype='double')

        alert = []

        for data in forecast:
            if data > 40000:
                alert.append = i
        peak_demand = False
        if alert:
            lower = min(alert)
            upper = max(alert)
            peak_demand = True

        alert = [None] * len(forecast)

        full_data = []
        for j in range(len(forecast)):
            print(j)
            if not peak_demand:
                alert[j] = 0
            else:
                if lower == i:
                    alert[j] = 1
                elif upper == i:
                    alert[j] = 1
                else:
                    alert[j] = 0
            #full_data[0, j] = forecast[j]
            #if real_demand:
                #full_data[1, j] = real_demand[j]
            #full_data[2, j] = alert[j]




        return Response(forecast, status=200)
