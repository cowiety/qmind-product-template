from django.apps import AppConfig
from pathlib import Path
import tensorflow as tf
import pandas as pd
import os

class PredictionConfig(AppConfig):
    name = 'prediction'
    BASE_DIR = Path(__file__).resolve().parent.parent
    MLMODEL_PATH = os.path.join(BASE_DIR, 'dashboard\mlmodel\BestModel')
    mlmodel = tf.keras.models.load_model(MLMODEL_PATH)
