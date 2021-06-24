## Environment Setup

# ignore warnings
import warnings
warnings.filterwarnings("ignore")
# Wrangling
import pandas as pd
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler
# Statistical Tests
import scipy.stats as stats
from scipy.stats import norm
# Visualizing
import matplotlib.pyplot as plt
from matplotlib import cm
import matplotlib.dates as dates
import seaborn as sns
from sklearn.model_selection import learning_curve
import datetime
pd.options.display.float_format = '{:20,.2f}'.format

#-----------------------------------------------------------------------------

def acquire_asteroid():
    '''
    This is a simple function to create a pandas dataframe from the asteroid.csv file
    '''
    df = pd.read_csv('asteroid.csv')
    return df

#-----------------------------------------------------------------------------

