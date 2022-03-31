from rest_framework import status
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from prediction.apps import PredictionConfig
import pandas as pd
import tensorflow as tf
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

# Create your views here.
# Class based view to predict based on IRIS model
class Demand_Model_Predict(APIView):
    def post(self, request, format=None):
        data = request.data
        
        demand = np.asarray(data['demand'])
        holiday = np.asarray(flatten_list(data['holiday']))
        clouds = np.asarray(flatten_list(data['clouds']))
        temp = np.asarray(flatten_list(data['temp']))
        humidity = np.asarray(flatten_list(data['humidity']))
        wind = np.asarray(flatten_list(data['wind']))
        X = np.stack((demand, holiday, clouds, temp, humidity, wind), axis=1)
        X = X.reshape(1, 24, 6)
        loaded_mlmodel = PredictionConfig.mlmodel
        y_pred = loaded_mlmodel.predict(X)
        y_pred = y_pred * 1000
        return Response(y_pred, status=200)
