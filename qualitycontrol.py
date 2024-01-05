import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt
from flagit import flagit
import matplotlib.dates as mdates

import os
os.chdir('/Users/cherryleheu/Documents/Thesis')

#Import csv
#I need to figure out a function for processing my file!
file = pd.read_csv('./SoilMoistureData/6819_AllData.csv')
file['DateTime'] = pd.to_datetime(file['DateTime'])
file.set_index('DateTime', inplace=True)
file = file[file['SM_10'].notna()].loc[file[file['SM_10'].notna()].index[0]:]

#Rename variables so it goes into the ISMN package
file_mean = file.resample('H').mean()
file_mean = file_mean.rename({'SM_10': 'soil_moisture','Temp_10':'soil_temperature'},axis='columns')
file_sum = file.resample('H').sum()
file_sum = file_mean.rename({'Rain': 'precipitation'},axis='columns')

qc_input = pd.concat([file_mean['soil_moisture'],file_mean['soil_temperature'], file_sum['precipitation']], axis=1)