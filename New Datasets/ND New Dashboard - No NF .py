# Importing the relevant modules
import dask.dataframe as dd # this module will allow us to turn our dataset into a dataframe we can analyse with Pandas
import numpy as np # importing a module that will allow us to assign a specific colour range
import matplotlib.pyplot as plt # will allow us to plot

# New datasets:
    # 171103T000001                                     - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.078125 .
    # 171110T000001                                     - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.109375
    # 171127T000524 - has some but not massses of data  - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.078125 * 2 .
    # 171128T000002 - has some but not masses of data   - Range Resolution: 75m, Maximum Range: 1200m, velocity = 0.078125 * 2 .
    # 171206T001724                                     - Range Resolution: 60m, Maximum Range: 960m, velocity = 0.078125 * 2 .
    # 180129T000002 - has little data                   - Range Resolution: 60m, Maximum Range: 960m, velocity = 0.078125 * 2 .
    # 180227T000003                                     - Range Resolution: 60m, Maximum Range: 960m, velocity = 0.078125 .

# Give specific n value and time step for scatter plot
n = 1550
t = 1

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i)) # Assigning the headers for the spectral powers from 1 to 2048

# Creating the dataframe for a particular inputted dataset and naming the columns as defined above
df = dd.read_csv('180129T000002.csv', sample=1000000000, names=col_names)

# This code computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df1 = df.compute()

# Creates the date of the dataset
from datetime import datetime
computed_df2 = computed_df1.astype(int)  # Changes the dataframe to integer only (Python produces it as a decimal
# which we don't want)
a = '%s'%(computed_df2.iloc[0,0] + 20000000) # This changes the date from 191001 to 20191001 which is the format we
# need to input it in d/m/y format.
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y') # assigning d/m/y format

# We are only interested in plotting for Power Spectra, therefore, we must omit the first 4 columns from our dataset
computed_df = computed_df1.drop(['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point',
                        'Frequency Step Between Data Bins'],axis=1)

# Creates the bin width
frequency_bin_width = computed_df1.iloc[0,3]

# We set the transients to a value less than the minimum value in the dataset. Here we choose -110
e = len(computed_df.iloc[:,1].tolist()) # this assigns 'e' to the length of rows in the dataset
# This entire code replaces ALL of the transients to -110 dB (a value below the minimum value of the dataset) so that
# when we begin plotting, the transients don't obscure the visualisation
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

# For this plot, we know that our y axis will be the frequency beginning from 0 to (2048*bin_width). After calculation,
# we obtain a bin width of 18.46621255. Therefore, we create a list, beginning from 0, that increases by a bin width
# each time until it reaches (2048*bin_width). We do this as follows:
frequency = [i*frequency_bin_width for i in range(0,2048)]

# Now we have our data with no spikes, we can begin to plot it on a 3D axis where we plot multiple Power vs
# Frequency plots.

# SCATTER GRAPHS FOR DIFFERENT VALUES OF TIME
fig = plt.figure() # begins plotting the figure
ax = fig.gca(projection = '3d') # creates a 3D axis for our plot
for i in range(n-5,n+5,t): # iterates over the dataset values specified above
    x = computed_df1.iloc[i,1] # our x axis will be the time in decimal hours of the selected time step
    # Our own specific colour range - this can be altered for user preference.
    col = np.where(computed_df.iloc[i,:]<=(-107.304882 + 1.176044), 'none', # Removes any data not above noise floor
                  np.where(computed_df.iloc[i, :] <= -105, 'r',
                   np.where(computed_df.iloc[i,:]<= -104, 'orange',
                    np.where(computed_df.iloc[i,:]<= -103, 'y',
                     np.where(computed_df.iloc[i,:]<= -102, 'g',
                      np.where(computed_df.iloc[i, :] <= -101, 'lime',
                        np.where(computed_df.iloc[i, :] <= -100, 'aqua',
                         np.where(computed_df.iloc[i,:]<=-95, 'b', 'purple'))))))))
    ax.scatter(x, frequency, computed_df.iloc[i,:],s=1,c=col) # creates a scatter graph for our defined x,y and time step,
    # sets the marker of the scatter point to 1 and assigns the colour as defined above
    ax.set_ylabel('Frequency / Hz') # labels the y axis
    ax.set_zlabel('Power / dB(AU)') # labels the z axis
    ax.set_xlabel('Time of Day / Decimal Hours') # labels the x axis
    # We use %s to input real variables defined in this python file, e.g. the date, time step and time.
    plt.title('Every %s Time Steps between %s hrs (Time Step %s) and %s hrs (Time Step %s)'%(t,computed_df1.iloc[n-5,1],
                                                                        n-5,computed_df1.iloc[n+5,1],n+5), fontsize=11,y=1.1)
    plt.suptitle('%s, Spectrum: Power vs Frequency per Time'%date, fontsize=13, y=0.97)
plt.show() # shows the plot we have produced
