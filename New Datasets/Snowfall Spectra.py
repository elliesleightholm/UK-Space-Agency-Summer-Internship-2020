# Import the relevant modules
import plotly.graph_objects as go # this allows us to plot the contour plots
import dask.dataframe as dd # this module will allow us to turn our dataset into a dataframe we can analyse with Pandas
from math import log10 # import log10 so we can perform our calculations
import numpy as np # allows us to plot the colour range
import matplotlib.pyplot as plt # allows us to plot the plots
from matplotlib import cm # allows us to plot for a specific colour map
from matplotlib.colors import ListedColormap # again, allows us to plot for a specific colour map

# Sets the velocity for selected dataset (as defined above)
velocity = 0.15625

# Inputs Range Resolution for selected dataset (can be found above):
RR = 60

# Inputs Maximum Range for selected dataset (can be found above):
MR = 960

# User specifies their time step value
n = -260

# Define the range of the velocity plot:
a = -10 # m /s (this will be the start of the x axis)
b = 0.5 # m / s (this will be the end of the x axis)

p = 50 # defining the percentile you want to remove - here we choose 50

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i)) # Assigning the headers for the spectral powers from 1 to 2048

# Creating the dataframe for a particular inputted dataset and naming the columns as defined above
df = dd.read_csv('171206T001724.csv', sample=1000000000, names=col_names)
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
frequency_bin_width = computed_df.iloc[0,3]

# # REMOVING NOISE SPECTRA - Include the Range Correction AND waterfall plot
plt.figure()
y = computed_df.iloc[n,:]           # covers the entire row
percentile = np.percentile(y,p)    # Finds the 10th percentile of the entire row
percentile = 10**(percentile/10)    # Converts this into the linear value


# Plotting Power vs Frequency for specified n value - fourth transient
# All explanation of code can be seen above, the only difference is that the plot omits the first 3 transients
plt.figure()
x = [i*frequency_bin_width for i in range(4,2048)] # frequency
y = computed_df.iloc[n,8:2053]
plt.plot(x,y,c='blue', linewidth=0.5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('From Fourth Spectral Power - Including Transients',fontsize=10)
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency'%(date,round(computed_df.iloc[n,1],5)),fontsize=13,y=0.97)
plt.show()

# Set the height ranges:

x = [i*(velocity) for i in range(-64,64)] # vertical velocity
y = computed_df.iloc[n,68:196] # The first height range for given n
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3] # range corrected and waterfall plot
y4 = [x for x in y4]
for k, i in enumerate(y4):
    if i == 60:
        y4[k] = -1000000  # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,196:324]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y5 = [10*log10(j) for j in y3]
y5 = [(x + 10*log10(2**2))for x in y5] # range corrected and waterfall plot
for k, i in enumerate(y5):
    if i == (60 + 10*log10(2**2)):
        y5[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,324:452]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y6 = [10*log10(j) for j in y3]
y6 = [(x + 10*log10(2**3))for x in y6] # range corrected and waterfall plot
for k, i in enumerate(y6):
    if i == (60 + 10*log10(2**3)):
        y6[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,452:580]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y7 = [10*log10(j) for j in y3]
y7 = [(x + 10*log10(2**4))for x in y7] # range corrected and waterfall plot
for k, i in enumerate(y7):
    if i == (60 + 10*log10(2**4)):
        y7[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,580:708]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y8 = [10*log10(j) for j in y3]
y8 = [(x + 10*log10(2**5))for x in y8] # range corrected and waterfall plot
for k, i in enumerate(y8):
    if i == (60 + 10*log10(2**5)):
        y8[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,708:836]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y9 = [10*log10(j) for j in y3]
y9 = [(x + 10*log10(2**6))for x in y9] # range corrected and waterfall plot
for k, i in enumerate(y9):
    if i == (60 + 10*log10(2**6)):
        y9[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,836:964]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y10 = [10*log10(j) for j in y3]
y10 = [(x + 10*log10(2**7))for x in y10] # range corrected and waterfall plot
for k, i in enumerate(y10):
    if i == (60 + 10*log10(2**7)):
        y10[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,964:1092]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y11 = [10*log10(j) for j in y3]
y11 = [(x + 10*log10(2**8))for x in y11] # range corrected and waterfall plot
for k, i in enumerate(y11):
    if i == (60 + 10*log10(2**8)):
        y11[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,1092:1220]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y12 = [10*log10(j) for j in y3]
y12 = [(x + 10*log10(2**9))for x in y12] # range corrected and waterfall plot
for k, i in enumerate(y12):
    if i == (60 + 10*log10(2**9)):
        y12[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,1220:1348]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y13 = [10*log10(j) for j in y3]
y13 = [(x + 10*log10(2**10))for x in y13] # range corrected and waterfall plot
for k, i in enumerate(y13):
    if i == (60 + 10*log10(2**10)):
        y13[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,1348:1476]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y14 = [10*log10(j) for j in y3]
y14 = [(x + 10*log10(2**11))for x in y14] # range corrected and waterfall plot
for k, i in enumerate(y14):
    if i == (60 + 10*log10(2**11)):
        y14[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n,1476:1604]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y15 = [10*log10(j) for j in y3]
y15 = [(x + 10*log10(2**12))for x in y15] # range corrected and waterfall plot
for k, i in enumerate(y15):
    if i == (60 + 10*log10(2**12)):
        y15[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n, 1604:1732]
y1 = [10 ** (i / 10) for i in y]  # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1]  # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y16 = [10*log10(j) for j in y3]
y16 = [(x + 10*log10(2**13))for x in y16] # range corrected and waterfall plot
for k, i in enumerate(y16):
    if i == (60 + 10*log10(2**13)):
        y16[k] = -1000000 # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n, 1732:1860]
y1 = [10 ** (i / 10) for i in y]  # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1]  # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y17 = [10 * log10(j) for j in y3]
y17 = [(x + 10 * log10(2 ** 14)) for x in y17]  # range corrected and waterfall plot
for k, i in enumerate(y17):
    if i == (60 + 10 * log10(2 ** 14)):
        y17[k] = -1000000  # assigns the removed percentile to 'none' so that it is not visible on the plot

y = computed_df.iloc[n, 1860:1988]
y1 = [10 ** (i / 10) for i in y]  # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1]  # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y18 = [10 * log10(j) for j in y3]
y18 = [(x + 10 * log10(2 ** 15)) for x in y18]  # range corrected and waterfall plot
for k, i in enumerate(y18):
    if i == (60 + 10 * log10(2 ** 15)):
        y18[k] = -1000000  # assigns the removed percentile to 'none' so that it is not visible on the plot


# Plotting an image plot for the Power over height and velocity
# Nearest Plot
z=[y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18] # plots for each of the height ranges with the percentile removed
fig, ax = plt.subplots(figsize=(15,6))
jet = cm.get_cmap('jet', 256) # assigns the colour map to the 'jet' colour
newcolors = jet(np.linspace(0, 1, 256)) # creating a new colour map
white = np.array([256/256, 256/256, 256/256, 1]) # creates the colour white
newcolors[:1, :] = white # assigns the first 17 rows of the new colour map to white so that we assign the removed percentiles to white
newcmp = ListedColormap(newcolors)
im = ax.imshow(z, interpolation='nearest', cmap=newcmp,
               origin='lower', extent=[(-64*velocity), (64*velocity),(0.5*RR),(15.5*RR)],
               vmax=-110, vmin=-60)
cbar = plt.colorbar(im, ax=ax)
cbar.set_label('Power / dB(AU)',rotation=270,labelpad=10)
ax.set_aspect(0.005) # stretches the graph so that it is visible
ax.set_ylabel('Height (AHL) / m')
ax.set_xlabel('Vertical Velocity ms$^{-1}$')
#plt.title('Nearest Plot', fontsize=12,y=1.1)
plt.title('%s, %s hrs (%s Time Step): Contour Plot - Power Over Height and Velocity'%(date, computed_df.iloc[n,1],n), fontsize=13, y=1.1)
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
y1 = [RR,2*RR,3*RR,4*RR,5*RR,6*RR,7*RR,8*RR,9*RR,10*RR,11*RR,12*RR,13*RR,14*RR,15*RR]
plt.yticks(y1)
plt.xlim(xmin=a,xmax=b)
plt.show()

