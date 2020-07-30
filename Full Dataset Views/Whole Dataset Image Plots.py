import dask.dataframe as dd
from math import log10
import numpy as np
import matplotlib.pyplot as plt
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
df = dd.read_csv('input_csv_here', sample=1000000000, names=col_names)

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
a = computed_df1.iloc[0,1]
b = computed_df1.iloc[e-1,1]
c = 0
d = (18.46621255*2047)


# Create a list that appends every column in the dataset and plot this as z
z = []
for i in range(len(computed_df.iloc[1,:].tolist())):
    z.append(computed_df.iloc[:,i])

fig, ax = plt.subplots(figsize=(6,6))
jet = cm.get_cmap('jet', 256)
newcolors = jet(np.linspace(0, 1, 256))
white = np.array([256/256, 256/256, 256/256, 1]) # creates the colour white
newcolors[:1, :] = white
newcmp = ListedColormap(newcolors)
im = ax.imshow(z, interpolation='bilinear', cmap=newcmp,
# Interpolation supported values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming',
# 'hermite','kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'.
               origin='lower', extent=[a,b,c,d],
               vmax=(-107.304882 + 1.176044), vmin=-95)
cbar = plt.colorbar(im, ax=ax,
                    ticks=[-110,-109,-108,-107,-106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,
                         -95,-94,-93,-92,-91,-90,-89,-88,-87,-86,-85,-84,-83,-82,-81,-80])
cbar.ax.set_yticklabels(['-110','-109','-108','-107','-106','-105','-104','-103','-102','-101','-100','-99','-98','-97','-96',
                         '-95','-94','-93','-92','-91','-90','-89','-88','-87','-86','-85','-84','-83','-82','-81','-80'])
cbar.set_label('Power / dB(AU)',rotation=270,labelpad=12)
# stretches the graph so that it is visible - this needs editing for each dataset
# Take the length of the dataset and divide by the highest frequency value = 40,000
ax.set_aspect(0.75*(computed_df1.iloc[-1,1] - computed_df1.iloc[0,1])/d)
ax.set_xlabel('Frequency / Hz')
ax.set_ylabel('Time of Day / Decimal Hours')
plt.suptitle('%s, Entire Spectrum: Power vs Frequency vs Time'%date, fontsize=13, y=0.97,x=0.5)
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
plt.show()

print(computed_df1.iloc[0,1])
print(computed_df1.iloc[-1,1])
print(d)
