import matplotlib.pyplot as plt
import dask.dataframe as dd
from math import log10
import numpy as np
import plotly.graph_objects as go

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

# WE BEGIN PLOTTING THE DASHBOARD GRAPHS:

# Plotting Power vs Frequency for specified n value - first transient
plt.figure()
n = 3000
x = [i*18.46621255 for i in range(0,2048)] # frequency
y = computed_df.iloc[n,4:2053]
plt.plot(x,y,c='blue', linewidth=0.5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('From First Spectral Power - Including Transients',fontsize=10)
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency'%(date,computed_df.iloc[n,1]),fontsize=13,y=0.97)
plt.show()


# Plotting Power vs Frequency for specified n value - fourth transient
plt.figure()
x = [i*18.46621255 for i in range(4,2048)] # frequency
y = computed_df.iloc[n,8:2053]
plt.plot(x,y,c='blue', linewidth=0.5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('From Fourth Spectral Power - Including Transients',fontsize=10)
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency'%(date,computed_df.iloc[n,1]),fontsize=13,y=0.97)
plt.show()


# Waterfall Plot - Power vs Velocity
plt.figure()
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
plt.ylim(min(computed_df.iloc[n,132:388])-2,-60)
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


# Contour Plot
fig = go.Figure(data =
    go.Contour(
        z=[computed_df.iloc[n,132:388],
            computed_df.iloc[n,388:644]+10*log10(2**2),
             computed_df.iloc[n,644:900]+10*log10(2**3),
                computed_df.iloc[n,900:1156]+10*log10(2**4),
                computed_df.iloc[n,1156:1412]+10*log10(2**5),
                computed_df.iloc[n,1412:1668]+10*log10(2**6),
            computed_df.iloc[n,1668:1924]+10*log10(2**7)],
        y=[75, 150, 225, 300, 375, 450, 525], # height
        x=[i*(2*0.03898614179) for i in range(-128,128)],
        # horizontal axis - vertical velocity,
        colorscale="rainbow",
        colorbar=dict(
            title="Power / dB(AU)",
            titleside="top",
            tickmode="array",
            tickvals=[-108, -107, -106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
                      -85,-84,-83],
            ticktext=[-108, -107, -106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
                      -85,-84,-83],
            ticks=""),
        contours = dict(
            start= -108, #-107.304882 + 1.176044,
            size=1,
            end = -83,
            showlines=True)))
fig.update_layout(
    title={
        'text': "%s, %s hrs: Contour Plot - Power Over Height and Velocity "%(date,computed_df.iloc[n,1]),
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

# Height vs Total Power
# Give m values, etc
m = 3044
k = 3045
l = 3050

# For n values - we add up their total spectra for each height range
y = computed_df.iloc[n,132:260]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log1 = 10*log10(total_power_linear)

y = computed_df.iloc[n,388:516]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2 = 10*log10(total_power_linear)

y = computed_df.iloc[n,644:772]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3 = 10*log10(total_power_linear)

y = computed_df.iloc[n,900:1028]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1156:1284]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1412:1540]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1668:1796]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1924:2052]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8 = 10*log10(total_power_linear)


# For m values
y = computed_df.iloc[m,132:260]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log1m = 10*log10(total_power_linear)

y = computed_df.iloc[m,388:516]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2m = 10*log10(total_power_linear)

y = computed_df.iloc[m,644:772]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3m = 10*log10(total_power_linear)

y = computed_df.iloc[m,900:1028]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1156:1284]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1412:1540]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1668:1796]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1924:2052]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8m = 10*log10(total_power_linear)


# For k values
y = computed_df.iloc[k,132:260]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log1k = 10*log10(total_power_linear)

y = computed_df.iloc[k,388:516]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2k = 10*log10(total_power_linear)

y = computed_df.iloc[k,644:772]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3k = 10*log10(total_power_linear)

y = computed_df.iloc[k,900:1028]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1156:1284]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1412:1540]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1668:1796]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1924:2052]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8k = 10*log10(total_power_linear)


# For l values
y = computed_df.iloc[l,132:260]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log1l = 10*log10(total_power_linear)

y = computed_df.iloc[l,388:516]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2l = 10*log10(total_power_linear)

y = computed_df.iloc[l,644:772]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3l = 10*log10(total_power_linear)

y = computed_df.iloc[l,900:1028]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1156:1284]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1412:1540]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1668:1796]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1924:2052]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8l = 10*log10(total_power_linear)

# Plot the graph
y = [75,150,225,300,375,450,525,600]
x = [total_power_log1,total_power_log2,total_power_log3,total_power_log4,total_power_log5,total_power_log6,total_power_log7,total_power_log8]
x1 = [total_power_log1m,total_power_log2m,total_power_log3m,total_power_log4m,total_power_log5m,total_power_log6m,total_power_log7m,total_power_log8m]
x2 = [total_power_log1k,total_power_log2k,total_power_log3k,total_power_log4k,total_power_log5k,total_power_log6k,total_power_log7k,total_power_log8k]
x3 = [total_power_log1l,total_power_log2l,total_power_log3l,total_power_log4l,total_power_log5l,total_power_log6l,total_power_log7l,total_power_log8l]
plt.figure()
plt.plot(x,y,c='fuchsia',label='%s hrs (%s Time Step)'%(computed_df.iloc[n,1],n))
plt.plot(x1,y,c='orange',label='%s hrs (%s Time Step)'%(computed_df.iloc[m,1],m))
plt.plot(x2,y,c='r',label='%s hrs (%s Time Step)'%(computed_df.iloc[k,1],k))
plt.plot(x3,y,c='b',label='%s hrs (%s Time Step)'%(computed_df.iloc[l,1],l))
plt.xlabel('Total Power / dB(AU)')
plt.ylabel('Height (AGL) / m')
plt.title('%s'%date,fontsize=10)
plt.ylim(0,675)
plt.suptitle('Height vs Total Power',fontsize=13,y=0.97)
plt.legend(loc="upper right")
plt.yticks(np.arange(0, 601, 75))
plt.show()
