import os
from sys import exit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import copy

pwd = os.getcwd()
dataset_url = 'https://www.kaggle.com/zaheenhamidani/ultimate-spotify-tracks-db'
dataset_path = 'SpotifyFeatures.csv'

# Load data sets
try:
    with open(dataset_path) as f:
        data = pd.read_csv(f)
except FileNotFoundError as e:
    print(f'''\
Unable to locate dataset at "{dataset_path}".
Download it at:
"{dataset_url}"
And extract to:
"{pwd}/{dataset_path}"''')


# Do stuff...


