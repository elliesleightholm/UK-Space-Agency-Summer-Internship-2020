import matplotlib.pyplot as plt
import matplotlib as mpl
import dask.dataframe as dd
from matplotlib.colors import LinearSegmentedColormap
import numpy as np
import matplotlib.pyplot as plt
from math import log10

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

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i))

# Creating the dataframe
df = dd.read_csv('input_csv_here', sample=1000000000, names=col_names)
computed_df = df.compute()

# Creating the date of the dataset:
from datetime import datetime
computed_df1 = computed_df.astype(int)
a = '%s'%(computed_df1.iloc[0,0] + 20000000)
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y')

# Define nth value
n = 3410

# # REMOVING NOISE SPECTRA - Include the Range Correction AND waterfall plot
p = 50 # defining the percentile you want to remove
plt.figure()
y = computed_df.iloc[n,:]           # covers the entire row
percentile = np.percentile(y,p)    # Finds the 10th percentile of the entire row
percentile = 10**(percentile/10)

# The following section of code is subtracting the percentiles for each height range

y = computed_df.iloc[n,132:388] # The first height range for given n
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3]
y4 = [x for x in y4]
for k, i in enumerate(y4):
    if i == 60:
        y4[k] = -120

y = computed_df.iloc[n,388:644]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y5 = [10*log10(j) for j in y3]
y5 = [(x + 10*log10(2**2))for x in y5]
for k, i in enumerate(y5):
    if i == (60 + 10*log10(2**2)):
        y5[k] = -120

y = computed_df.iloc[n,644:900]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y6 = [10*log10(j) for j in y3]
y6 = [(x + 10*log10(2**3))for x in y6]
for k, i in enumerate(y6):
    if i == (60 + 10*log10(2**3)):
        y6[k] = -120

y = computed_df.iloc[n,900:1156]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y7 = [10*log10(j) for j in y3]
y7 = [(x + 10*log10(2**4))for x in y7]
for k, i in enumerate(y7):
    if i == (60 + 10*log10(2**4)):
        y7[k] = -120

y = computed_df.iloc[n,1156:1412]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y8 = [10*log10(j) for j in y3]
y8 = [(x + 10*log10(2**5))for x in y8]
for k, i in enumerate(y8):
    if i == (60 + 10*log10(2**5)):
        y8[k] = -120

y = computed_df.iloc[n,1412:1668]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y9 = [10*log10(j) for j in y3]
y9 = [(x + 10*log10(2**6))for x in y9]
for k, i in enumerate(y9):
    if i == (60 + 10*log10(2**6)):
        y9[k] = -120

y = computed_df.iloc[n,1668:1924]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y10 = [10*log10(j) for j in y3]
y10 = [(x + 10*log10(2**7))for x in y10]
for k, i in enumerate(y10):
    if i == (60 + 10*log10(2**7)):
        y10[k] = -120


# Another way of plotting a contour plot
fig = plt.figure()
x = [i*(2*0.03898614179) for i in range(-128,128)]
y = [75,150,225,300,375,450,525]
A = [y4,y5,y6,y7,y8,y9,y10]
norm=plt.Normalize(-110,-80)
cmap = mpl.colors.LinearSegmentedColormap.from_list("", ["white","red","violet","blue"])
plt.contourf(x,y,A,cmap=cmap,norm=norm)
#plt.scatter(x,y,)
cb = plt.colorbar()
plt.show()
