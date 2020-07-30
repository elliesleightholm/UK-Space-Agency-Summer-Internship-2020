# Importing relevant modules
import dask.dataframe as dd
import matplotlib.pyplot as plt

# Creating the names for the dataframe headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i))

# Creating the dataframe
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

# Assign the frequency - this will become the x axis of the graph
frequency = [i*18.46621255 for i in range(0,2048)]

# Begin Plotting

# Assign the spectral row you are interested in
n = 5756

# Now plot the power vs frequency graph with no transients
plt.figure()
x = frequency                               # Plots the frequency bin steps on the x axis
y = computed_df.iloc[n,:]                   # Plots the Power Spectra for the given row
plt.plot(x,y,c='blue', linewidth=0.5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('No Transients',fontsize=10)
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df1.iloc[n,1]),
             fontsize=13,y=0.97)
plt.show()