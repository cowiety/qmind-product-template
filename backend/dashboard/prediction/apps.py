from django.apps import AppConfig
import tensorflow as tf
import pandas as pd
import os

class PredictionConfig(AppConfig):
    name = 'prediction'
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    MLMODEL_PATH = os.path.join(BASE_DIR, 'prediction/mlmodel/BestModel')
    mlmodel = tf.keras.models.load_model(MLMODEL_PATH)
