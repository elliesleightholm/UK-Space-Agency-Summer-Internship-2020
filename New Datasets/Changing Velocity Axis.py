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
n = -350

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

# Define the range of the velocity plot:
a = -10 # m /s (this will be the start of the x axis)
b = 0.5 # m / s (this will be the end of the x axis)


# # REMOVING NOISE SPECTRA - Include the Range Correction AND waterfall plot
p = 0 # defining the percentile you want to remove
plt.figure()
y = computed_df.iloc[n,:]           # covers the entire row
percentile = np.percentile(y,p)    # Finds the 10th percentile of the entire row
percentile = 10**(percentile/10)    # Converts this into the linear value

# Waterfall Step

w = 2.5

# For this plot, we know that our x axis will be the vertical velocity beginning from (-128*velocity resolution) and
# (128*velocity resolution). After calculation, we obtain a velocity resolution of 0.03898614179. Therefore, we create
# a list, beginnning from (-128*velocity resolution), that increases by a bin width each time until it reaches
# (128*velocity resolution). We do this as follows:
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
        y4[k] = None  # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y4,c='brown', linewidth=1, label="%sm"%(RR))

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
y5 = [(x + w + 10*log10(2**2))for x in y5] # range corrected and waterfall plot
for k, i in enumerate(y5):
    if i == (60 + w + 10*log10(2**2)):
        y5[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y5,c='crimson', linewidth=1, label="%sm"%(2*RR))

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
y6 = [(x + (2*w) + 10*log10(2**3))for x in y6] # range corrected and waterfall plot
for k, i in enumerate(y6):
    if i == (60 + (2*w) + 10*log10(2**3)):
        y6[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y6,c='red', linewidth=1, label="%sm"%(3*RR))

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
y7 = [(x + (3*w)+ 10*log10(2**4))for x in y7] # range corrected and waterfall plot
for k, i in enumerate(y7):
    if i == (60 + (3*w) + 10*log10(2**4)):
        y7[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y7,c='orange', linewidth=1, label="%sm"%(4*RR))

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
y8 = [(x + (4*w)+ 10*log10(2**5))for x in y8] # range corrected and waterfall plot
for k, i in enumerate(y8):
    if i == (60 + (4*w)+ 10*log10(2**5)):
        y8[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y8,c='gold', linewidth=1, label="%sm"%(5*RR))

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
y9 = [(x + (5*w)+ 10*log10(2**6))for x in y9] # range corrected and waterfall plot
for k, i in enumerate(y9):
    if i == (60 + (5*w)+ 10*log10(2**6)):
        y9[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y9,c='yellow', linewidth=1, label="%sm"%(6*RR))

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
y10 = [(x + (6*w)+ 10*log10(2**7))for x in y10] # range corrected and waterfall plot
for k, i in enumerate(y10):
    if i == (60 + (6*w)+ 10*log10(2**7)):
        y10[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y10,c='lime', linewidth=1, label="%sm"%(7*RR))

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
y11 = [(x + (7*w)+ 10*log10(2**8))for x in y11] # range corrected and waterfall plot
for k, i in enumerate(y11):
    if i == (60 + (7*w)+ 10*log10(2**8)):
        y11[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y11,c='green', linewidth=1, label="%sm"%(8*RR))

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
y12 = [(x + (8*w)+ 10*log10(2**9))for x in y12] # range corrected and waterfall plot
for k, i in enumerate(y12):
    if i == (60 + (8*w)+ 10*log10(2**9)):
        y12[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y12,c='turquoise', linewidth=1, label="%sm"%(9*RR))

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
y13 = [(x + (9*w)+ 10*log10(2**10))for x in y13] # range corrected and waterfall plot
for k, i in enumerate(y13):
    if i == (60 + (9*w)+ 10*log10(2**10)):
        y13[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y13,c='aqua', linewidth=1, label="%sm"%(10*RR))

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
y14 = [(x + (10*w)+ 10*log10(2**11))for x in y14] # range corrected and waterfall plot
for k, i in enumerate(y14):
    if i == (60 + (10*w)+ 10*log10(2**11)):
        y14[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y14,c='deepskyblue', linewidth=1, label="%sm"%(11*RR))

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
y15 = [(x + (11*w)+ 10*log10(2**12))for x in y15] # range corrected and waterfall plot
for k, i in enumerate(y15):
    if i == (60 + (11*w)+ 10*log10(2**12)):
        y15[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y15,c='dodgerblue', linewidth=1, label="%sm"%(12*RR))

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
y16 = [(x + (12*w)+ 10*log10(2**13))for x in y16] # range corrected and waterfall plot
for k, i in enumerate(y16):
    if i == (60 + (12*w)+ 10*log10(2**13)):
        y16[k] = None # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y16,c='royalblue', linewidth=1, label="%sm"%(13*RR))

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
y17 = [(x + (13 * w) + 10 * log10(2 ** 14)) for x in y17]  # range corrected and waterfall plot
for k, i in enumerate(y17):
    if i == (60 + (13 * w) + 10 * log10(2 ** 14)):
        y17[k] = None  # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y17,c='darkviolet', linewidth=1, label="%sm"%(14*RR))

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
y18 = [(x + (14 * w) + 10 * log10(2 ** 15)) for x in y18]  # range corrected and waterfall plot
for k, i in enumerate(y18):
    if i == (60 + (14 * w) + 10 * log10(2 ** 15)):
        y18[k] = None  # assigns the removed percentile to 'none' so that it is not visible on the plot
plt.plot(x,y18,c='darkviolet', linewidth=1, label="%sm"%(15*RR))

plt.xlabel('Vertical Velocity / $ms^{-1}$')
miny = min(computed_df.iloc[n,132:388] - 2.5)
maxy = max(computed_df.iloc[n,1668:1924])
# plt.ylim(miny,-65)
# plt.xlim(-10,10)
# x1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
# my_xticks = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
# plt.xticks(x1, my_xticks)
plt.ylabel('Range Corrected Power / dB(AU) -- Waterfall Plot (%sdB)'%w)
plt.title('Excluding %sth Percentile'%p)
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.xlim(a,b)
plt.grid()
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Vertical Velocity for Each Individual Height Range'%(date,
                                                                round(computed_df.iloc[n,1],5),n),fontsize=13,y=0.97)
plt.show()


# Setting the vector values
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
plt.plot(x,y4,c='brown', linewidth=0.5, label="%sm"%(RR))

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
plt.plot(x,y5,c='crimson', linewidth=0.5, label="%sm"%(2*RR))

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
plt.plot(x,y6,c='red', linewidth=0.5, label="%sm"%(3*RR))

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
plt.plot(x,y7,c='orange', linewidth=0.5, label="%sm"%(4*RR))

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
plt.plot(x,y8,c='gold', linewidth=0.5, label="%sm"%(5*RR))

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
plt.plot(x,y9,c='yellow', linewidth=0.5, label="%sm"%(6*RR))

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
plt.plot(x,y10,c='lime', linewidth=0.5, label="%sm"%(7*RR))

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
plt.plot(x,y11,c='green', linewidth=0.5, label="%sm"%(8*RR))

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
plt.plot(x,y12,c='turquoise', linewidth=0.5, label="%sm"%(9*RR))

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
plt.plot(x,y13,c='aqua', linewidth=0.5, label="%sm"%(10*RR))

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
plt.plot(x,y14,c='deepskyblue', linewidth=0.5, label="%sm"%(11*RR))

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
plt.plot(x,y15,c='dodgerblue', linewidth=0.5, label="%sm"%(12*RR))

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
plt.plot(x,y16,c='royalblue', linewidth=0.5, label="%sm"%(13*RR))

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
plt.plot(x,y17,c='darkviolet', linewidth=0.5, label="%sm"%(14*RR))

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
plt.plot(x,y18,c='darkviolet', linewidth=0.5, label="%sm"%(15*RR))


# Plot the contour
fig = go.Figure(data =
    [go.Contour(
        z=[y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18], # plots for each height range with percentile removal
        y= [RR,2*RR,3*RR,4*RR,5*RR,6*RR,7*RR,8*RR,9*RR,10*RR,11*RR,12*RR,13*RR,14*RR,15*RR], # height ranges
        x= np.array([i*(velocity) for i in range(-64,64)]), # Creates velocity on the x-axis
        # plots a given colorscale as specified by the user
        colorscale=[[(0), 'white'],
                    [(1/12), 'darkviolet'],
                    [(2/12), 'royalblue'],
                    [(3/12), 'dodgerblue'],
                    [(4/12), 'deepskyblue'],
                    #[(5/15), 'aqua'],
                    #[(6/15), 'turquoise'],
                    [(5/12), 'green'],
                    [(6/12), 'lime'],
                    [(7/12), 'yellow'],
                    #[(10/15), 'gold'],
                    [(8/12), 'orange'],
                    [(9/12),'darkorange'],
                    [(10/12), 'red'],
                    [(11/12), 'crimson'],
                    [1.0, 'brown']],
        colorbar=dict(
            title="Power / dB(AU)", # labels the title
            titleside="top",
            tickmode="array",
            tickvals=[-108, -106,-104,-102,-100,-98,-96,-94,-92,-90,-88,-86,-84,-82,-80,-78,-76,-74,-72,-70,-68,-66,-64,-62,-60], # gives the interval ticks
            ticktext=[" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "], # We don't want to plot the numbers just yet
            ticks=""),
        contours = dict(
            start= -108, # power spectra begins at -108
            size=0.1, # size of the bar width on the power spectra colour range - we make this small so that the
            # colours appear to have a colour gradient effect
            end = -60, # end the colour bar at -86
            showlines=False)), # we don't want to show contour lines just yet
# In order to get the colour gradient effect, we plot our contour lines ON TOP of our already plotted contour plot.
# We do this as follows:
    # Follow the same code as above
    go.Contour(
        z=[y4,y5,y6,y7,y8,y9,y10,y11,y12,y13,y14,y15,y16,y17,y18],
        y= [RR,2*RR,3*RR,4*RR,5*RR,6*RR,7*RR,8*RR,9*RR,10*RR,11*RR,12*RR,13*RR,14*RR,15*RR], # height
        x= np.array([i*(velocity) for i in range(-64,64)]),
        contours_coloring='lines', # use contour lines
        line_width=1, # set the contour line width
        # Assign all the colours to black - this will be the colour of the contour lines
        colorscale=[[(0), 'black'],
                    [(1/12), 'black'],
                    [(2/12), 'black'],
                    [(3/12), 'black'],
                    [(4/12), 'black'],
                    [(5/12), 'black'],
                    [(6/12), 'black'],
                    [(7/12), 'black'],
                    [(8/12), 'black'],
                    [(9/12), 'black'],
                    [(10/12), 'black'],
                    [(11/12), 'black'],
                    [1.0, 'black']],
        colorbar=dict(
            title="Power / dB(AU)",
            titleside="top",
            tickmode="array",
            tickvals=[-108, -106,-104,-102,-100,-98,-96,-94,-92,-90,-88,-86,-84,-82,-80,-78,-76,-74,-72,-70,-68,-66,-64,-62,-60],
            ticktext=[-108, -106,-104,-102,-100,-98,-96,-94,-92,-90,-88,-86,-84,-82,-80,-78,-76,-74,-72,-70,-68,-66,-64,-62,-60],
            ticks=""),
        contours = dict(
            start= -108,
            size=2,
            end = -60,
            showlines=True))]) # Show the lines as true
# Plot the necessary axes and titles:
fig.update_layout(
    title={
        'text': "%s, %s hrs (%s Time Step): Contour Plot - Power Over Height and Velocity (%sth Percentile Removed)"%(date, computed_df.iloc[n,1],n,p),
        'y':0.9,
        'x':0.487,
        'xanchor': 'center',
        'yanchor': 'top'},
         xaxis_title = "$Vertical~Velocity~ms^{-1}$",
         yaxis_title = "Height (AHL) / m",
         legend_title = "Range Corrected Power")
fig.update_xaxes(ticks="outside")
fig.update_yaxes(ticks="outside")
fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = (-64*velocity),
        dtick = 1,
        range = [a,b]  # Plots for the specific velocity range
    ))
fig.update_layout(
    yaxis = dict(
        tickmode = 'linear',
        tick0 = RR,
        dtick = RR
    ))
fig.show()




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
# Interpolation supported values are 'none', 'nearest', 'bilinear', 'bicubic', 'spline16', 'spline36', 'hanning', 'hamming',
# 'hermite','kaiser', 'quadric', 'catrom', 'gaussian', 'bessel', 'mitchell', 'sinc', 'lanczos'.
               origin='lower', extent=[(-64*velocity), (64*velocity),(0.5*RR),(15.5*RR)],
               vmax=-110, vmin=-60)
cbar = plt.colorbar(im, ax=ax)
#                     ticks=[-110,-109,-108,-107,-106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,
#                          -95,-94,-93,-92,-91,-90,-89,-88,-87,-86,-85,-84,-83,-82,-81,-80])
# cbar.ax.set_yticklabels(['-110','-109','-108','-107','-106','-105','-104','-103','-102','-101','-100','-99','-98','-97','-96',
#                          '-95','-94','-93','-92','-91','-90','-89','-88','-87','-86','-85','-84','-83','-82','-81','-80'])
cbar.set_label('Power / dB(AU)',rotation=270,labelpad=10)
ax.set_aspect(0.005) # stretches the graph so that it is visible
ax.set_ylabel('Height (AHL) / m')
ax.set_xlabel('Vertical Velocity ms$^{-1}$')
#plt.title('Nearest Plot', fontsize=12,y=1.1)
plt.title('%s, %s hrs (%s Time Step): Contour Plot - Power Over Height and Velocity'%(date, computed_df.iloc[n,1],n), fontsize=13, y=1.1)
ax.xaxis.labelpad = 10
ax.yaxis.labelpad = 10
# x1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
# my_xticks = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
# plt.xticks(x1, my_xticks)
y1 = [RR,2*RR,3*RR,4*RR,5*RR,6*RR,7*RR,8*RR,9*RR,10*RR,11*RR,12*RR,13*RR,14*RR,15*RR]
plt.yticks(y1)
plt.xlim(xmin=a,xmax=b)
plt.show()

