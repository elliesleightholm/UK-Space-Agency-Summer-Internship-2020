import dask.dataframe as dd
import matplotlib.pyplot as plt
from math import log10
import numpy as np

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i))

# Creating the dataframe
df = dd.read_csv('input_csv_here', sample=1000000000, names=col_names)

# Computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df = df.compute()

# Creating the date of the dataset:
from datetime import datetime
computed_df1 = computed_df.astype(int)
a = '%s'%(computed_df1.iloc[0,0] + 20000000)
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y')

# # # Generic plot - not a waterfall plot - Raw Data

plt.figure()
n = 200
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
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df.iloc[n-1,1]),fontsize=13,y=0.97)
plt.show()


# Plot ammended with range correction WITH waterfall plot

plt.figure()
n = 200
x = [i*18.46621255 for i in range(-128,128)] # frequency
y = computed_df.iloc[n,132:388]
plt.plot(x,y,c='red', linewidth=0.5, label="75m")
y = computed_df.iloc[n,388:644] + 10*log10(2**2) + 2.5
plt.plot(x,y,c='orange', linewidth=0.5, label="150m")
y = computed_df.iloc[n,644:900] + 10*log10(2**3) + 5
plt.plot(x,y,c='yellow', linewidth=0.5, label="225m")
y = computed_df.iloc[n,900:1156] + 10*log10(2**4) + 7.5
plt.plot(x,y,c='green', linewidth=0.5, label="300m")
y = computed_df.iloc[n,1156:1412] + 10*log10(2**5) + 10
plt.plot(x,y,c='blue', linewidth=0.5, label="375m")
y = computed_df.iloc[n,1412:1668] + 10*log10(2**6) + 12.5
plt.plot(x,y,c='purple', linewidth=0.5, label="450m")
y = computed_df.iloc[n,1668:1924] + 10*log10(2**7) + 15
plt.plot(x,y,c='indigo', linewidth=0.5, label="525m")
plt.xlabel('Frequency / Hz')
plt.ylabel('Range Corrected Power / dB(AU) -- Waterfall Plot')
plt.title('All Height Ranges')
#plt.legend(loc="upper left")
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.grid()
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df.iloc[n-1,1]),fontsize=13,y=0.97)
plt.show()



# # REMOVING NOISE SPECTRA - Include the Range Correction AND waterfall plot

plt.figure()
n = 200                            # Assign the given row
m = 2.5                             # Waterfall Step
y = computed_df.iloc[n,:]           # covers the entire row
percentile = np.percentile(y,10)    # Finds the 10th percentile of the entire row
percentile = 10**(percentile/10)    # Converts this into the linear value

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
plt.title('Excluding 10th Percentile')
#plt.legend(loc="upper left")
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.grid()
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency for Each Individual Height Range'%(date,computed_df.iloc[n-1,1]),fontsize=13,y=0.97)
plt.show()


# Velocity

plt.figure()
n = 50
x = [i*(2*0.03898614179) for i in range(-128,128)] # vertical velocity
y = computed_df.iloc[n,132:388]
plt.plot(x,y,c='red', linewidth=0.5, label="75m")
y = computed_df.iloc[n,388:644] + 10*log10(2**2) + 2.5
plt.plot(x,y,c='orange', linewidth=0.5, label="150m")
y = computed_df.iloc[n,644:900] + 10*log10(2**3) + 5
plt.plot(x,y,c='yellow', linewidth=0.5, label="225m")
y = computed_df.iloc[n,900:1156] + 10*log10(2**4) + 7.5
plt.plot(x,y,c='green', linewidth=0.5, label="300m")
y = computed_df.iloc[n,1156:1412] + 10*log10(2**5) + 10
plt.plot(x,y,c='blue', linewidth=0.5, label="375m")
y = computed_df.iloc[n,1412:1668] + 10*log10(2**6) + 12.5
plt.plot(x,y,c='purple', linewidth=0.5, label="450m")
y = computed_df.iloc[n,1668:1924] + 10*log10(2**7) + 15
plt.plot(x,y,c='indigo', linewidth=0.5, label="525m")
plt.xlabel('Vertical Velocity / $ms^{-1}$')
plt.ylim(-110,-65)
x = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
my_xticks = [-10,-9,-8,-7,-6,-5,-4,-3,-2,-1,0,1,2,3,4,5,6,7,8,9,10]
plt.xticks(x, my_xticks)
plt.ylabel('Range Corrected Power / dB(AU) -- Waterfall Plot')
plt.title('All Height Ranges')
#plt.legend(loc="upper left")
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1))
plt.suptitle('%s, %s hrs: Power vs Vertical Velocity for Each Individual Height Range'%(date,computed_df.iloc[n,1]),fontsize=13,y=0.97)
plt.grid()
plt.show()

