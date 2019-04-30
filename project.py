import os
from sys import exit
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from copy import copy


pwd = os.getcwd()
data_dir = './spotify-audio-features'
data_path_nov2018 = data_dir+'/SpotifyAudioFeaturesNov2018.csv'
data_path_apr2019 = data_dir+'/SpotifyAudioFeaturesApril2019.csv'


# Load data sets
try:
    try:
        with open(data_path_nov2018) as f:
            data_nov2018 = pd.read_csv(f)
    except FileNotFoundError as e:
        print('Unable to locate November 2018 data.')
        raise e
    try:
        with open(data_path_apr2019) as f:
            data_apr2018 = pd.read_csv(f)
    except FileNotFoundError as e:
        print('Unable to locate April 2019 data.')
        raise e
except:
    print(f'''\
Download the datasets from:
<https://www.kaggle.com/tomigelo/spotify-audio-features/downloads/spotify-audio-features.zip/3>

And extract to "{pwd}/spotify-audio-features"''')


# Do stuff...


