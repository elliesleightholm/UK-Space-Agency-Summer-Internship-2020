import matplotlib.pyplot as plt
import dask.dataframe as dd
from math import log10
import numpy as np
import plotly.graph_objects as go

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
n = 3415

# Plotting Power vs Frequency for specified n value - first transient
plt.figure()
x = [i*18.46621255 for i in range(0,2048)] # frequency
y = computed_df.iloc[n,4:2053]
plt.plot(x,y,c='blue', linewidth=0.5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('From First Spectral Power - Including Transients',fontsize=10)
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Frequency'%(date,computed_df.iloc[n,1],n),fontsize=13,y=0.97)
plt.show()

# Plotting Power vs Frequency for specified n value - fourth transient
plt.figure()
x = [i*18.46621255 for i in range(4,2048)] # frequency
y = computed_df.iloc[n,8:2053]
plt.plot(x,y,c='blue', linewidth=0.5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('From Fourth Spectral Power - Including Transients',fontsize=10)
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Frequency'%(date,computed_df.iloc[n,1],n),fontsize=13,y=0.97)
plt.show()

# # Generic plot - raw data - not corrected/waterfall
plt.figure()
x = [i*18.46621255 for i in range(-128,128)] # frequency
y = computed_df.iloc[n,132:388]
plt.plot(x,y,c='red', linewidth=0.5, label="75m")
y = computed_df.iloc[n,388:644]
plt.plot(x,y,c='orange', linewidth=0.5, label="150m")
y = computed_df.iloc[n,644:900]
plt.plot(x,y,c='yellow', linewidth=0.5, label="225m")
y = computed_df.iloc[n,900:1156]
plt.plot(x,y,c='green', linewidth=0.5, label="300m")
y = computed_df.iloc[n,1156:1412]
plt.plot(x,y,c='blue', linewidth=0.5, label="375m")
y = computed_df.iloc[n,1412:1668]
plt.plot(x,y,c='purple', linewidth=0.5, label="450m")
y = computed_df.iloc[n,1668:1924]
plt.plot(x,y,c='indigo', linewidth=0.5, label="525m")
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('All Height Ranges')
plt.legend(loc="upper left")
plt.grid()
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df.iloc[n,1],n),fontsize=13,y=0.97)
plt.show()


# # Plot ammended with range correction WITHOUT waterfall plot
plt.figure()
x = [i*18.46621255 for i in range(-128,128)] # frequency
y = computed_df.iloc[n,132:388]
plt.plot(x,y,c='red', linewidth=0.5, label="75m")
y = computed_df.iloc[n,388:644] + 10*log10(2**2)
plt.plot(x,y,c='orange', linewidth=0.5, label="150m")
y = computed_df.iloc[n,644:900] + 10*log10(2**3)
plt.plot(x,y,c='yellow', linewidth=0.5, label="225m")
y = computed_df.iloc[n,900:1156] + 10*log10(2**4)
plt.plot(x,y,c='green', linewidth=0.5, label="300m")
y = computed_df.iloc[n,1156:1412] + 10*log10(2**5)
plt.plot(x,y,c='blue', linewidth=0.5, label="375m")
y = computed_df.iloc[n,1412:1668] + 10*log10(2**6)
plt.plot(x,y,c='purple', linewidth=0.5, label="450m")
y = computed_df.iloc[n,1668:1924] + 10*log10(2**7)
plt.plot(x,y,c='indigo', linewidth=0.5, label="525m")
plt.xlabel('Frequency / Hz')
plt.ylabel('Range Corrected Power / dB(AU)')
plt.title('All Height Ranges')
#plt.legend(loc="upper left")
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.grid()
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df.iloc[n,1],n),fontsize=13,y=0.97)
plt.show()


# Range Correction AND Waterfall Plot
m = 2.5                             # Waterfall Step
plt.figure()
x = [i*18.46621255 for i in range(-128,128)] # frequency
y = computed_df.iloc[n,132:388]
plt.plot(x,y,c='red', linewidth=0.5, label="75m")
y = computed_df.iloc[n,388:644] + 10*log10(2**2) + m
plt.plot(x,y,c='orange', linewidth=0.5, label="150m")
y = computed_df.iloc[n,644:900] + 10*log10(2**3) + (2*m)
plt.plot(x,y,c='yellow', linewidth=0.5, label="225m")
y = computed_df.iloc[n,900:1156] + 10*log10(2**4) + (3*m)
plt.plot(x,y,c='green', linewidth=0.5, label="300m")
y = computed_df.iloc[n,1156:1412] + 10*log10(2**5) + (4*m)
plt.plot(x,y,c='blue', linewidth=0.5, label="375m")
y = computed_df.iloc[n,1412:1668] + 10*log10(2**6) + (5*m)
plt.plot(x,y,c='purple', linewidth=0.5, label="450m")
y = computed_df.iloc[n,1668:1924] + 10*log10(2**7) + (6*m)
plt.plot(x,y,c='indigo', linewidth=0.5, label="525m")
plt.xlabel('Frequency / Hz')
plt.ylabel('Range Corrected Power / dB(AU) -- Waterfall Plot')
plt.title('All Height Ranges')
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.grid()
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df.iloc[n,1],n),fontsize=13,y=0.97)
plt.show()


# # REMOVING NOISE SPECTRA - Include the Range Correction AND waterfall plot
p = 0 # defining the percentile you want to remove
plt.figure()
y = computed_df.iloc[n,:]           # covers the entire row
percentile = np.percentile(y,p)    # Finds the 10th percentile of the entire row
percentile = 10**(percentile/10)    # Converts this into the linear value

# Removing the percentile from each height range
x = [i*18.46621255 for i in range(-128,128)] # frequency value - this stays constant throughout
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
        y4[k] = None
plt.plot(x,y4,c='red', linewidth=0.5, label="75m")

y = computed_df.iloc[n,388:644]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3]
y4 = [(x + 1*m + 10*log10(2**2))for x in y4]
for k, i in enumerate(y4):
    if i == (60 + 1*m + 10*log10(2**2)):
        y4[k] = None
plt.plot(x,y4,c='orange', linewidth=0.5, label="150m")

y = computed_df.iloc[n,644:900]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3]
y4 = [(x + 2*m + 10*log10(2**3))for x in y4]
for k, i in enumerate(y4):
    if i == (60 + 2*m + 10*log10(2**3)):
        y4[k] = None
plt.plot(x,y4,c='yellow', linewidth=0.5, label="225m")

y = computed_df.iloc[n,900:1156]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3]
y4 = [(x + 3*m + 10*log10(2**4))for x in y4]
for k, i in enumerate(y4):
    if i == (60 + 3*m + 10*log10(2**4)):
        y4[k] = None
plt.plot(x,y4,c='green', linewidth=0.5, label="300m")

y = computed_df.iloc[n,1156:1412]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3]
y4 = [(x + 4*m + 10*log10(2**5))for x in y4]
for k, i in enumerate(y4):
    if i == (60 + 4*m + 10*log10(2**5)):
        y4[k] = None
plt.plot(x,y4,c='blue', linewidth=0.5, label="375m")

y = computed_df.iloc[n,1412:1668]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3]
y4 = [(x + 5*m + 10*log10(2**6))for x in y4]
for k, i in enumerate(y4):
    if i == (60 + 5*m + 10*log10(2**6)):
        y4[k] = None
plt.plot(x,y4,c='purple', linewidth=0.5, label="450m")

y = computed_df.iloc[n,1668:1924]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1000000)
y4 = [10*log10(j) for j in y3]
y4 = [(x + 6*m + 10*log10(2**7))for x in y4]
for k, i in enumerate(y4):
    if i == (60 + 6*m + 10*log10(2**7)):
        y4[k] = None
plt.plot(x,y4,c='indigo', linewidth=0.5, label="525m")
plt.xlabel('Frequency / Hz')
plt.ylabel('Range Corrected Power / dB(AU) -- Waterfall Plot')
plt.title('Excluding %sth Percentile'%p)
#plt.legend(loc="upper left")
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.grid()
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df.iloc[n,1],n),fontsize=13,y=0.97)
plt.show()


# Plot but for velocity
plt.figure()
y = computed_df.iloc[n,:]           # covers the entire row
percentile = np.percentile(y,p)    # Finds the 10th percentile of the entire row
percentile = 10**(percentile/10)    # Converts this into the linear value

x = [i*(2*0.03898614179) for i in range(-128,128)] # vertical velocity # frequency value - this stays constant throughout
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
        y4[k] = None
plt.plot(x,y4,c='red', linewidth=0.5, label="75m")

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
y5 = [(x + m + 10*log10(2**2))for x in y5]
for k, i in enumerate(y5):
    if i == (60 + m + 10*log10(2**2)):
        y5[k] = None
plt.plot(x,y5,c='orange', linewidth=0.5, label="150m")

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
y6 = [(x + (2*m) + 10*log10(2**3))for x in y6]
for k, i in enumerate(y6):
    if i == (60 + (2*m) + 10*log10(2**3)):
        y6[k] = None
plt.plot(x,y6,c='yellow', linewidth=0.5, label="225m")

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
y7 = [(x + (3*m)+ 10*log10(2**4))for x in y7]
for k, i in enumerate(y7):
    if i == (60 + (3*m) + 10*log10(2**4)):
        y7[k] = None
plt.plot(x,y7,c='green', linewidth=0.5, label="300m")

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
y8 = [(x + (4*m)+ 10*log10(2**5))for x in y8]
for k, i in enumerate(y8):
    if i == (60 + (4*m)+ 10*log10(2**5)):
        y8[k] = None
plt.plot(x,y8,c='blue', linewidth=0.5, label="375m")

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
y9 = [(x + (5*m)+ 10*log10(2**6))for x in y9]
for k, i in enumerate(y9):
    if i == (60 + (5*m)+ 10*log10(2**6)):
        y9[k] = None
plt.plot(x,y9,c='purple', linewidth=0.5, label="450m")

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
y10 = [(x + (6*m)+ 10*log10(2**7))for x in y10]
for k, i in enumerate(y10):
    if i == (60 + (6*m)+ 10*log10(2**7)):
        y10[k] = None
plt.plot(x,y10,c='indigo', linewidth=0.5, label="525m")
plt.xlabel('Vertical Velocity / $ms^{-1}$')
miny = min(computed_df.iloc[n,132:388] - 2.5)
maxy = max(computed_df.iloc[n,1668:1924])
plt.ylim(miny,-65)
plt.xlim(-10,10)
x1 = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
my_xticks = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
plt.xticks(x1, my_xticks)
plt.ylabel('Range Corrected Power / dB(AU) -- Waterfall Plot')
plt.title('Excluding %sth Percentile'%p)
#plt.legend(loc="upper left")
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.grid()
plt.suptitle('%s, %s hrs (%s Time Step): Spectrum: Power vs Vertical Velocity for Each Individual Height Range'%(date,computed_df.iloc[n,1],n),fontsize=13,y=0.97)
plt.show()


# CONTOUR PLOT
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
        y4[k] = -1000000

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
        y5[k] = -1000000

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
        y6[k] = -1000000

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
        y7[k] = -1000000

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
        y8[k] = -1000000

y = computed_df.iloc[n,1412:1668]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
y2 = [i - percentile for i in y1] # this subtracts the 10th percentile from the whole linear spectra
y3 = []
for j in y2:
    if j > 0:
        y3.append(j + percentile)
    else:
        y3.append(1)
y9 = [10*log10(j) for j in y3]
y9 = [(x + 10*log10(2**6))for x in y9]
for k, i in enumerate(y9):
    if i == (10*log10(1) + 10*log10(2**6)):
        y9[k] = -1000000

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
        y10[k] = -1000000


# Plot the contour
fig = go.Figure(data =
    [go.Contour(
        z=[y4,y5,y6,y7,y8,y9,y10],
        y= [75,150, 225, 300, 375, 450, 525], # height
        x= np.array([i*(2*0.03898614179) for i in range(-128,128)]),#[i*(2*0.03898614179) for i in range(-128,128)],
        # horizontal axis - vertical velocity,
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
        #[[(0), 'white'],[(1/12), 'darkviolet'],[(2/12), 'royalblue'], [(3/12), 'dodgerblue'], [(4/12), 'deepskyblue'],
        #            [(5/12), 'aqua'], [(6/12), 'turquoise'], [(7/12), 'mediumspringgreen'], [(8/12), 'lime'],
        #            [(9/12), 'greenyellow'], [(10/12), 'yellow'], [(11/12), 'orange'],
        #            [1.0, 'red']],#"rainbow",
        #connectgaps=True,
        #line_smoothing=0.85,
        colorbar=dict(
            title="Power / dB(AU)",
            titleside="top",
            tickmode="array",
            tickvals=[-108, -106,-104,-102,-100,-98,-96,-94,-92,-90,-88,-86],
#[-108, -107, -106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
#                      -85,-84,-83],
            ticktext=[" "," "," "," "," "," "," "," "," "," "," "," "],
            ticks=""),
        contours = dict(
            start= -108, #-107.304882 + 1.176044,
            size=0.1,
            end = -86,
            showlines=False)),
    go.Contour(
        z=[y4,y5,y6,y7,y8,y9,y10],
        y= [75,150, 225, 300, 375, 450, 525], # height
        x= np.array([i*(2*0.03898614179) for i in range(-128,128)]),
        contours_coloring='lines',
        line_width=1,
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
        #[[(0), 'white'],[(1/12), 'darkviolet'],[(2/12), 'royalblue'], [(3/12), 'dodgerblue'], [(4/12), 'deepskyblue'],
        #            [(5/12), 'aqua'], [(6/12), 'turquoise'], [(7/12), 'mediumspringgreen'], [(8/12), 'lime'],
        #            [(9/12), 'greenyellow'], [(10/12), 'yellow'], [(11/12), 'orange'],
        #            [1.0, 'red']],#"rainbow",
        #connectgaps=True,
        #line_smoothing=0.85,
        colorbar=dict(
            title="Power / dB(AU)",
            titleside="top",
            tickmode="array",
            tickvals=[-108, -106,-104,-102,-100,-98,-96,-94,-92,-90,-88,-86],
#[-108, -107, -106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
#                      -85,-84,-83],
            ticktext=[-108, -106,-104,-102,-100,-98,-96,-94,-92,-90,-88,-86],#-108, -106,-104,-102,-100,-98,-96,-94,-92,-90,-88,-86,-84],
            ticks=""),
            #yanchor="top", y=1,x=1),
        contours = dict(
            start= -108, #-107.304882 + 1.176044,
            size=2,
            end = -86,
            showlines=True))])
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
        tick0 = -10,
        dtick = 1
    ))
fig.update_layout(
    yaxis = dict(
        tickmode = 'linear',
        tick0 = 75,
        dtick = 75
    ))

fig.show()

