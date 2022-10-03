from exclude_tortoise import *
from model.siamese.model_generator import create_model, base_models
import tensorflow as tf
import tensorflow_addons as tfa
from tqdm.keras import TqdmCallback
from data.data_generator import DataGenerator
from model.siamese.config import cfg
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np


def embed_missing_tortoise(tortoise_number: int):
    """
    Embeds the tortoise_number-th tortoise usine a model trained on every tortoise except that one.
    This function should store and/or return the distance from that tortoise's embedding to the other classes.
    """
    pass


if __name__ == "__main__":
    pass
