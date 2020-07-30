# Import relevant modules
import dask.dataframe as dd
import numpy as np

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i))

# Creating the dataframe for particular dataset
df = dd.read_csv('191001T000014.csv', sample=1000000000, names=col_names)

# Computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df1 = df.compute()

# Creates the date of the dataset
from datetime import datetime
computed_df2 = computed_df1.astype(int)
a = '%s'%(computed_df2.iloc[0,0] + 20000000)
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y')

# Since we begin plotting for Power Spectra, we must omit the first 4 columns from our dataset
computed_df = computed_df1.drop(['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point',
                        'Frequency Step Between Data Bins'],axis=1)


# We set the transients to a value less than the minimum value in the dataset. Here we choose -110

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

# Set our y axis - frequency
frequency = [i*18.46621255 for i in range(0,2048)]

# Now we have our data with no spikes, we can begin to plot it on a 3D axis where we plot multiple Power vs
# Frequency plots.

# SCATTER GRAPHS FOR DIFFERENT VALUES OF TIME
n = 10 # First Time Step
m = 20 # End Time Step
t = 2 # Time Step Between Graphs

import matplotlib.pyplot as plt
fig = plt.figure()
ax = fig.gca(projection = '3d')
for i in range(n,m+1,t):
    x = computed_df1.iloc[i,1]
    # Our own specific colour range - this can be altered for user preference.
    # Here we use a very simple colour range
    col = np.where(computed_df.iloc[i,:]<=(-107.304882 + 1.176044), 'none', # Removes any data not above noise floor
                  np.where(computed_df.iloc[i, :] <= -105, 'r',
                   np.where(computed_df.iloc[i,:]<= -104, 'orange',
                    np.where(computed_df.iloc[i,:]<= -103, 'y',
                     np.where(computed_df.iloc[i,:]<= -102, 'g',
                      np.where(computed_df.iloc[i, :] <= -101, 'lime',
                        np.where(computed_df.iloc[i, :] <= -100, 'aqua',
                         np.where(computed_df.iloc[i,:]<=-95, 'b', 'purple'))))))))
    ax.scatter(x, frequency, computed_df.iloc[i,:],s=1,c=col)
    ax.set_ylabel('Frequency / Hz')
    ax.set_zlabel('Power / dB(AU)')
    ax.set_xlabel('Time of Day / Decimal Hours')
    plt.title('Every %s Time Steps between %s hrs (Time Step %s) and %s hrs (Time Step %s)'%(t,computed_df1.iloc[n,1],
                                                                        n,computed_df1.iloc[m,1],m), fontsize=11,y=1.1)
    plt.suptitle('%s, Spectrum: Power vs Frequency per Time'%date, fontsize=13, y=0.97)
plt.show()


# LINE GRAPHS - COLOUR BLUE
n = 10 # First Time Step
m = 20 # End Time Step
t = 2 # Time Step Between Graphs

fig = plt.figure()
ax = fig.gca(projection = '3d')
for i in range(n,m+1,t): # Includes range as specified above
    ax.plot([computed_df1.iloc[i,1]]*2048, frequency, computed_df.iloc[i,:],linewidth=0.5,c='blue')
    ax.set_ylabel('Frequency / Hz')
    ax.set_zlabel('Power / dB(AU)')
    ax.set_xlabel('Time of Day / Decimal Hours')
    plt.title('Every %s Time Steps between %s hrs (Time Step %s) and %s hrs (Time Step %s)' % (t, computed_df1.iloc[n, 1],
                                                                n, computed_df1.iloc[m, 1], m), fontsize=11, y=1.1)
    plt.suptitle('%s, Spectrum: Power vs Frequency per Time'%date, fontsize=13, y=0.97)
plt.show()


#Creates a graph of times between n and m with power spectra less than the inputted value
def plot_per_range(power_range,n,m):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    for i in range(n,m+1):
        col = np.where(computed_df.iloc[i,:]<power_range,'r','none')
        ax.scatter(computed_df1.iloc[i,1],frequency,computed_df.iloc[i,:],s=1.5,c=col)
        ax.set_zlim(-110,power_range + 5)
        ax.set_ylabel('Frequency / Hz')
        ax.set_zlabel('Power / dB(AU)')
        ax.set_xlabel('Time of Day / Decimal Hours')
    plt.title('Time Step %s (%s hrs) to %s (%s hrs) with Power Spectral Less than %s dB(AU)' %(n,computed_df1.iloc[n,1],
                                                                                       m,computed_df1.iloc[m,1],
                                                                                       power_range), fontsize=11,y=1.1)
    plt.suptitle('%s, Spectrum: Power vs Frequency per Time'%date, fontsize=13, y=0.97)
    plt.show()

# To test this function we input a command like the following:
# This asks Python to plot a graph for all the spectral points below -105 between the 400th and 415th time steps
plot_per_range(-105,400,415)

# We create a second function that plots between a specific power range and specific time step range:
def plot_per_range(power_range1,power_range2,n,m):
    fig = plt.figure()
    ax = fig.gca(projection = '3d')
    for i in range(n-1,m):
        col = np.where(computed_df.iloc[i,:]< power_range1,'none',
                       np.where(computed_df.iloc[i, :] <= power_range2, 'r',
                        np.where(computed_df.iloc[i,:] > power_range2, 'none','r')))
        ax.scatter(computed_df1.iloc[i,1],frequency,computed_df.iloc[i,:],s=1.5,c=col)
        ax.set_zlim(-110,power_range2 + 3)
        ax.set_ylabel('Frequency / Hz')
        ax.set_zlabel('Power / dB(AU)')
        ax.set_xlabel('Time of Day / Decimal Hours')
    plt.title('Time Step %s (%s hrs) to %s (%s hrs) with Power Spectral Between %s db(AU) and %s db(AU)'
              %(n,computed_df1.iloc[n-1,1],m,computed_df1.iloc[m,1],power_range1,power_range2), fontsize=11,y=1.1)
    plt.suptitle('%s, Spectrum: Power vs Frequency per Time'%date, fontsize=13, y=0.97)
    plt.show()


# To test this function we input a command like the following:
# This asks Python to plot a graph for all the spectral points between -110 and -103 between the 400th and 415th time steps
plot_per_range(-110,-103,400,415)
