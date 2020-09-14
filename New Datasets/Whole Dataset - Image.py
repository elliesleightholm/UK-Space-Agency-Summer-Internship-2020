# Import the relevant modules
import dask.dataframe as dd # this module will allow us to turn our dataset into a dataframe we can analyse with Pandas
import numpy as np # allows us to plot the colour range
import matplotlib.pyplot as plt # allows us to plot
from matplotlib import cm # allows us to plot the colour range
from matplotlib.colors import ListedColormap # allows us to plot the colour range

# The other code plots for the other datasets.

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i)) # Assigning the headers for the spectral powers from 1 to 2048

# Creating the dataframe for a particular inputted dataset and naming the columns as defined above
df = dd.read_csv('171206T001724.csv', sample=1000000000, names=col_names)
# This code computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df1 = df.compute()

# Creates the date of the dataset
from datetime import datetime
computed_df2 = computed_df1.astype(int)  # Changes the dataframe to integer only (Python produces it as a decimal
# which we don't want)
a = '%s'%(computed_df2.iloc[0,0] + 20000000) # This changes the date from 191001 to 20191001 which is the format we
# need to input it in d/m/y format.
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y') # assigning d/m/y format

# Creates the bin width
frequency_bin_width = computed_df1.iloc[0,3]

# We need to drop the first four columns before we plot as they do not observe spectral power
computed_df = computed_df1.drop(['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point',
                        'Frequency Step Between Data Bins'],axis=1)


# We reassign any transients to a value below the minimum value of the dataset
e = len(computed_df.iloc[:,1].tolist())
computed_df['Spectral Power 126'] = [-110]*e
computed_df['Spectral Power 127'] = [-110]*e
computed_df['Spectral Power 128'] = [-110]*e
computed_df['Spectral Power 129'] = [-110]*e
computed_df['Spectral Power 130'] = [-110]*e
computed_df['Spectral Power 254'] = [-110]*e
computed_df['Spectral Power 255'] = [-110]*e
computed_df['Spectral Power 256'] = [-110]*e
computed_df['Spectral Power 257'] = [-110]*e
computed_df['Spectral Power 258'] = [-110]*e
computed_df['Spectral Power 382'] = [-110]*e
computed_df['Spectral Power 383'] = [-110]*e
computed_df['Spectral Power 384'] = [-110]*e
computed_df['Spectral Power 385'] = [-110]*e
computed_df['Spectral Power 386'] = [-110]*e
computed_df['Spectral Power 510'] = [-110]*e
computed_df['Spectral Power 511'] = [-110]*e
computed_df['Spectral Power 512'] = [-110]*e
computed_df['Spectral Power 513'] = [-110]*e
computed_df['Spectral Power 514'] = [-110]*e
computed_df['Spectral Power 638'] = [-110]*e
computed_df['Spectral Power 639'] = [-110]*e
computed_df['Spectral Power 640'] = [-110]*e
computed_df['Spectral Power 641'] = [-110]*e
computed_df['Spectral Power 642'] = [-110]*e
computed_df['Spectral Power 766'] = [-110]*e
computed_df['Spectral Power 767'] = [-110]*e
computed_df['Spectral Power 768'] = [-110]*e
computed_df['Spectral Power 769'] = [-110]*e
computed_df['Spectral Power 770'] = [-110]*e
computed_df['Spectral Power 894'] = [-110]*e
computed_df['Spectral Power 895'] = [-110]*e
computed_df['Spectral Power 896'] = [-110]*e
computed_df['Spectral Power 897'] = [-110]*e
computed_df['Spectral Power 898'] = [-110]*e
computed_df['Spectral Power 1024'] = [-110]*e
computed_df['Spectral Power 1025'] = [-110]*e
computed_df['Spectral Power 1026'] = [-110]*e
computed_df['Spectral Power 1027'] = [-110]*e
computed_df['Spectral Power 1028'] = [-110]*e
computed_df['Spectral Power 1150'] = [-110]*e
computed_df['Spectral Power 1151'] = [-110]*e
computed_df['Spectral Power 1152'] = [-110]*e
computed_df['Spectral Power 1153'] = [-110]*e
computed_df['Spectral Power 1154'] = [-110]*e
computed_df['Spectral Power 1278'] = [-110]*e
computed_df['Spectral Power 1279'] = [-110]*e
computed_df['Spectral Power 1280'] = [-110]*e
computed_df['Spectral Power 1281'] = [-110]*e
computed_df['Spectral Power 1282'] = [-110]*e
computed_df['Spectral Power 1406'] = [-110]*e
computed_df['Spectral Power 1407'] = [-110]*e
computed_df['Spectral Power 1408'] = [-110]*e
computed_df['Spectral Power 1409'] = [-110]*e
computed_df['Spectral Power 1410'] = [-110]*e
computed_df['Spectral Power 1534'] = [-110]*e
computed_df['Spectral Power 1535'] = [-110]*e
computed_df['Spectral Power 1536'] = [-110]*e
computed_df['Spectral Power 1537'] = [-110]*e
computed_df['Spectral Power 1538'] = [-110]*e
computed_df['Spectral Power 1662'] = [-110]*e
computed_df['Spectral Power 1663'] = [-110]*e
computed_df['Spectral Power 1664'] = [-110]*e
computed_df['Spectral Power 1665'] = [-110]*e
computed_df['Spectral Power 1666'] = [-110]*e
computed_df['Spectral Power 1790'] = [-110]*e
computed_df['Spectral Power 1791'] = [-110]*e
computed_df['Spectral Power 1792'] = [-110]*e
computed_df['Spectral Power 1793'] = [-110]*e
computed_df['Spectral Power 1794'] = [-110]*e
computed_df['Spectral Power 1918'] = [-110]*e
computed_df['Spectral Power 1919'] = [-110]*e
computed_df['Spectral Power 1920'] = [-110]*e
computed_df['Spectral Power 1921'] = [-110]*e
computed_df['Spectral Power 1922'] = [-110]*e
computed_df['Spectral Power 2047'] = [-110]*e
computed_df['Spectral Power 2048'] = [-110]*e
computed_df['Spectral Power 1'] = [-110]*e
computed_df['Spectral Power 2'] = [-110]*e
computed_df['Spectral Power 3'] = [-110]*e

# For this plot, we know that our x axis will be the frequency beginning from 0 to (2048*bin_width). After calculation,
# we obtain a bin width. Therefore, we create a list, beginnning from 0, that increases by a bin width
# each time until it reaches (2048*bin_width). We do this as follows:
frequency = [i*frequency_bin_width for i in range(0,2048)]

# assign the plotting range
a = computed_df1.iloc[0,1] # first time step in the dataset
b = computed_df1.iloc[e-1,1] # final time step in the dataset
c = 0 # first frequency bin
d = (frequency_bin_width*2047) # last frequency bin

# Create a list that appends every column in the dataset and plot this as z
z = []
for i in range(len(computed_df.iloc[1,:].tolist())):
    z.append(computed_df.iloc[:,i])

# Begin plotting
fig, ax = plt.subplots(figsize=(6,6))
jet = cm.get_cmap('jet', 256) # sets colour range
newcolors = jet(np.linspace(0, 1, 256)) # creates a new colour range
white = np.array([256/256, 256/256, 256/256, 1]) # creates the colour white
newcolors[:1, :] = white # assigns the first 17 rows in the colour bar to the colour white
newcmp = ListedColormap(newcolors)
im = ax.imshow(z, interpolation='none', cmap=newcmp,
# Interpolation supported values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming',
# 'hermite','kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'.
               origin='lower', extent=[a,b,c,d], # plots for the intervals defined above
               vmax=(-107.304882 + 1.176044), vmin=-95) # maximum value on the colour bar removes noise spectra
cbar = plt.colorbar(im, ax=ax,
                    # plots x axis ticks
                    ticks=[-110,-109,-108,-107,-106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,
                         -95,-94,-93,-92,-91,-90,-89,-88,-87,-86,-85,-84,-83,-82,-81,-80])
# plots y axis ticks
cbar.ax.set_yticklabels(['-110','-109','-108','-107','-106','-105','-104','-103','-102','-101','-100','-99','-98','-97','-96',
                         '-95','-94','-93','-92','-91','-90','-89','-88','-87','-86','-85','-84','-83','-82','-81','-80'])
cbar.set_label('Power / dB(AU)',rotation=270,labelpad=12) # positions and labels the colour bar
# stretches the graph so that it is visible - this needs editing for each dataset
# Take the length of the dataset and divide by the highest frequency value = 40,000
# We multiply by 0.75 to give a better visualisation
ax.set_aspect(abs(0.75*(computed_df1.iloc[-2,1] - computed_df1.iloc[0,1])/d))
ax.set_ylabel('Frequency / Hz') # labels the y axis
ax.set_xlabel('Time of Day / Decimal Hours') # labels the x axis
plt.suptitle('%s, Entire Spectrum: Power vs Frequency vs Time'%date, fontsize=13, y=0.97,x=0.5)
ax.xaxis.labelpad = 10 # moves the axis text away from the axis
ax.yaxis.labelpad = 10
# We set up a x axis tick method:
# We want to plot from the first time step to the last time step with 4 labels overall. We do this as follows:
x1 = [a, b]
my_xticks = [round(a,4), round(b,4)]
plt.xticks(x1, my_xticks) # plots the ticks
plt.show()
