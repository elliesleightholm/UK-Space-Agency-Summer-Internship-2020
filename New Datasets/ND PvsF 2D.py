# Import the relevant modules
import matplotlib.pyplot as plt # allows us to plot
import dask.dataframe as dd # this module will allow us to turn our dataset into a dataframe we can analyse with Pandas
from math import log10 # import log10 so we can perform our calculations
import numpy as np # allows us to plot the colour range
import plotly.graph_objects as go # this allows us to plot the contour plots

# New datasets:
    # 171103T000001                                     - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.078125
    # 171110T000001                                     - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.109375
    # 171127T000524 - has some but not massses of data  - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.078125 * 2
    # 171128T000002 - has some but not masses of data   - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.078125 * 2
    # 171206T001724                                     - Range Resolution: 60m, Maximum Range: 960m, velocity = 0.078125 * 2
    # 180129T000002 - has little data                   - Range Resolution: 60m, Maximum Range: 960m, velocity = 0.078125 * 2
    # 180227T000003                                     - Range Resolution: 60m, Maximum Range: 960m, velocity = 0.078125

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i)) # Assigning the headers for the spectral powers from 1 to 2048

# Creating the dataframe for a particular inputted dataset and naming the columns as defined above
df = dd.read_csv('180227T000003.csv', sample=1000000000, names=col_names)
# This code computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df = df.compute()

# Creates the date of the dataset
from datetime import datetime
computed_df1 = computed_df.astype(int)  # Changes the dataframe to integer only (Python produces it as a decimal
# which we don't want)
a = '%s'%(computed_df1.iloc[0,0] + 20000000) # This changes the date from 191001 to 20191001 which is the format we
# need to input it in d/m/y format.
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y') # assigning d/m/y format

# Creates the bin width
frequency_bin_width = computed_df1.iloc[0,3]

# WE BEGIN PLOTTING THE DASHBOARD GRAPHS:

# User specifies their time step value
l = -1050

# We comment this out so we can plot one row spectra value - to plot four row spectra, we remove the comments and choose
# for our specific values

# m = -1060
#
# n = -1070 # 150 second time step (5*30 = 150)
#
# o = -1080

# Plotting Power vs Frequency for specified values - fourth transient
# All explanation of code can be seen above, the only difference is that the plot omits the first 3 transients
plt.figure(figsize=(9,3))
x = [i*frequency_bin_width for i in range(4,2048)] # frequency
y0 = computed_df.iloc[l,8:2053]
plt.plot(x,y0,c='blue', linewidth=0.5,label='%s hrs (Time Step %s)'%(computed_df.iloc[l,1],l))
# These plot the three extra row spectra we commented out above
# y1 = computed_df.iloc[m,8:2053]
# plt.plot(x,y1,c='green', linewidth=0.5,label='%s hrs (Time Step %s)'%(computed_df.iloc[m,1],m))
# y2 = computed_df.iloc[n,8:2053]
# plt.plot(x,y2,c='red', linewidth=0.5,label='%s hrs (Time Step %s)'%(computed_df.iloc[n,1],n))
# y3 = computed_df.iloc[o,8:2053]
# plt.plot(x,y3,c='blue', linewidth=0.5,label='%s hrs (Time Step %s)'%(computed_df.iloc[o,1],o))
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('%s: Spectrum: Power vs Frequency'%date,fontsize=13)
plt.legend(loc="upper right") # plots a key
plt.show()

