import dask.dataframe as dd
import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
import matplotlib as mpl
import dask.dataframe as dd
from math import log10
import numpy as np
import plotly.graph_objects as go
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i))

# Datasets:
# Half Day Datasets:
    # 191212T215726
    # 191215T214532
# Full Day Datasets:
    #191001T000014
    #191002T000010 - lack of data
    #191024T000013
    #191025T000009
    #191026T000005
    #191108T000002 - lack of data
    #191109T000013

# Creating the dataframe
df = dd.read_csv('191212T215726.csv', sample=1000000000, names=col_names)

# Computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df1 = df.compute()

# Creates the date of the dataset
from datetime import datetime
computed_df2 = computed_df1.astype(int)
a = '%s'%(computed_df2.iloc[0,0] + 20000000)
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y')

# We need to drop the first four columns before we plot as they do not observe spectral power
computed_df = computed_df1.drop(['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point',
                        'Frequency Step Between Data Bins'],axis=1)


# We reassign any transients to a value below the minimum value of the dataset
e = len(computed_df.iloc[:,1].tolist())
computed_df['Spectral Power 254'] = [-110]*e
computed_df['Spectral Power 255'] = [-110]*e
computed_df['Spectral Power 256'] = [-110]*e
computed_df['Spectral Power 257'] = [-110]*e
computed_df['Spectral Power 258'] = [-110]*e
computed_df['Spectral Power 510'] = [-110]*e
computed_df['Spectral Power 511'] = [-110]*e
computed_df['Spectral Power 512'] = [-110]*e
computed_df['Spectral Power 513'] = [-110]*e
computed_df['Spectral Power 514'] = [-110]*e
computed_df['Spectral Power 766'] = [-110]*e
computed_df['Spectral Power 767'] = [-110]*e
computed_df['Spectral Power 768'] = [-110]*e
computed_df['Spectral Power 769'] = [-110]*e
computed_df['Spectral Power 770'] = [-110]*e
computed_df['Spectral Power 1024'] = [-110]*e
computed_df['Spectral Power 1025'] = [-110]*e
computed_df['Spectral Power 1026'] = [-110]*e
computed_df['Spectral Power 1027'] = [-110]*e
computed_df['Spectral Power 1028'] = [-110]*e
computed_df['Spectral Power 1278'] = [-110]*e
computed_df['Spectral Power 1279'] = [-110]*e
computed_df['Spectral Power 1280'] = [-110]*e
computed_df['Spectral Power 1281'] = [-110]*e
computed_df['Spectral Power 1282'] = [-110]*e
computed_df['Spectral Power 1534'] = [-110]*e
computed_df['Spectral Power 1535'] = [-110]*e
computed_df['Spectral Power 1536'] = [-110]*e
computed_df['Spectral Power 1537'] = [-110]*e
computed_df['Spectral Power 1538'] = [-110]*e
computed_df['Spectral Power 1790'] = [-110]*e
computed_df['Spectral Power 1791'] = [-110]*e
computed_df['Spectral Power 1792'] = [-110]*e
computed_df['Spectral Power 1793'] = [-110]*e
computed_df['Spectral Power 1794'] = [-110]*e
computed_df['Spectral Power 2047'] = [-110]*e
computed_df['Spectral Power 2048'] = [-110]*e
computed_df['Spectral Power 1'] = [-110]*e
computed_df['Spectral Power 2'] = [-110]*e
computed_df['Spectral Power 3'] = [-110]*e

# Create our frequency list for our y axis
frequency = [i*18.46621255 for i in range(0,2048)]

# Now we have our data with no spikes, we can begin to plot it on a 3D axis where we plot multiple Power vs
# Frequency plots.

# PLOTTING AERIAL VIEW - SCATTER PLOT

fig = plt.figure()
ax = fig.gca(projection = '3d')
for i in range(0,e):
    x = computed_df1.iloc[i,1]
    # We create our colour range
    col = np.where(computed_df.iloc[i, :] <= (-107.304882 + 1.176044), 'white',
          np.where(computed_df.iloc[i, :] <= -106, 'magenta',
          np.where(computed_df.iloc[i, :] <= -105.5, 'fuchsia',
          np.where(computed_df.iloc[i, :] <= -105, 'blueviolet',
          np.where(computed_df.iloc[i, :] <= -104.5, 'darkviolet',
          np.where(computed_df.iloc[i, :] <= -104, 'purple',
          np.where(computed_df.iloc[i, :] <= -103.5, 'navy',
          np.where(computed_df.iloc[i, :] <= -103, 'b',
          np.where(computed_df.iloc[i, :] <= -102.5,'royalblue',
          np.where(computed_df.iloc[i, :] <= -102,'dodgerblue' ,
          np.where(computed_df.iloc[i, :] <= -101.5,'deepskyblue',
          np.where(computed_df.iloc[i, :] <= -101,'aqua',
          np.where(computed_df.iloc[i, :] <= -100.5,'turquoise',
          np.where(computed_df.iloc[i, :] <= -100,'green',
          np.where(computed_df.iloc[i, :] <= -98,'lime',
          np.where(computed_df.iloc[i, :] <= -96,'gold',
          np.where(computed_df.iloc[i, :] <= -94,'yellow',
          np.where(computed_df.iloc[i, :] <= -92,'orange',
          np.where(computed_df.iloc[i, :] <= -90,'darkorange',
          np.where(computed_df.iloc[i, :] <= -88,'red',
          np.where(computed_df.iloc[i, :] <= -86,'crimson', 'brown')))))))))))))))))))))
    ax.scatter(x, frequency, computed_df.iloc[i,:],s=0.01,c=col)
ax.set_ylabel('Frequency / Hz',labelpad=20)
ax.set_xlabel('Time of Day / Decimal Hours',labelpad=25)
plt.title('Entire Spectrum - Beginning at %s'%computed_df1.iloc[0,1], fontsize=11,y=1.1)
plt.suptitle('%s, Spectrum: Power vs Frequency vs Time'%date, fontsize=13, y=0.97)
ax.view_init(azim=-90, elev=90) # Produces aerial view of plot
ax.w_zaxis.line.set_lw(0.) # Gets rid of z-axis
ax.set_zticks([])   # Gets rid of z-axis
ax.tick_params(axis='both', which='major', pad=15) # Increases the distance between numbers and ticks plotted on the graph
plt.show()
