# Import the relevant modules
import matplotlib.pyplot as plt # allows us to plot
import dask.dataframe as dd # this module will allow us to turn our dataset into a dataframe we can analyse with Pandas
from math import log10 # import log10 so we can perform our calculations
import numpy as np # allows us to plot the colour range
import plotly.graph_objects as go # this allows us to plot the contour plots

# Sets the velocity for selected dataset (as defined above)
velocity = 0.109375

# Inputs Range Resolution for selected dataset (can be found above):
RR = 75

# Inputs Maximum Range for selected dataset (can be found above):
MR = 1200

# User specifies their time step value
n = -210

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i)) # Assigning the headers for the spectral powers from 1 to 2048

# Creating the dataframe for a particular inputted dataset and naming the columns as defined above
df = dd.read_csv('171110T000001.csv', sample=1000000000, names=col_names)
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

# WE BEGIN PLOTTING THE DASHBOARD GRAPHS:

# Plotting Power vs Frequency for specified n value - first transient
plt.figure()
# For this plot, we know that our x axis will be the frequency beginning from 0 to (2048*bin_width). After calculation,
# we obtain a bin width of 18.46621255. Therefore, we create a list, beginnning from 0, that increases by a bin width
# each time until it reaches (2048*bin_width). We do this as follows:
x = [i*frequency_bin_width for i in range(0,2048)] # frequency axis - can be
y = computed_df.iloc[n,4:2053] # this plots the specified n time step's row power spectra
plt.plot(x,y,c='blue', linewidth=0.5) # plots the graph and specifies line properties
plt.xlabel('Frequency / Hz') # labels x axis
plt.ylabel('Power / dB(AU)') # labels y axis
plt.title('From First Spectral Power - Including Transients',fontsize=10) # plots a subtitle
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency'%(date,computed_df.iloc[n,1]),fontsize=13,y=0.97) # additional title
plt.show()


# Plotting Power vs Frequency for specified n value - fourth transient
# All explanation of code can be seen above, the only difference is that the plot omits the first 3 transients
plt.figure()
x = [i*frequency_bin_width for i in range(4,2048)] # frequency
y = computed_df.iloc[n,8:2053]
plt.plot(x,y,c='blue', linewidth=0.5)
plt.xlabel('Frequency / Hz')
plt.ylabel('Power / dB(AU)')
plt.title('From Fourth Spectral Power - Including Transients',fontsize=10)
plt.suptitle('%s, %s hrs: Spectrum: Power vs Frequency'%(date,computed_df.iloc[n,1]),fontsize=13,y=0.97)
plt.show()


# Waterfall Plot - Power vs Velocity
plt.figure()
# For this plot, we know that our x axis will be the vertical velocity beginning from (-128*velocity resolution) and
# (128*velocity resolution). After calculation, we obtain a velocity resolution. Therefore, we create
# a list, beginnning from (-128*velocity resolution), that increases by a bin width each time until it reaches
# (128*velocity resolution). We do this as follows:
x = [i*(velocity) for i in range(-64,64)] # vertical velocity
# Next, we continually plot the different height ranges, we do this step by step.
# First we take the power spectra values in the height range 75m. This is range corrected (multiplied by 1) and is the
# starting step for our waterfall plot.

# Define waterfall step:
w = 1

y = computed_df.iloc[n,68:196]
plt.plot(x,y,c='brown', linewidth=1, label="%sm"%(RR))
y = computed_df.iloc[n,196:324] + 10*log10(2**2) + w
plt.plot(x,y,c='crimson', linewidth=1, label="%sm"%(2*RR))
y = computed_df.iloc[n,324:452] + 10*log10(2**3) + 2*w
plt.plot(x,y,c='red', linewidth=1, label="%sm"%(3*RR))
y = computed_df.iloc[n,452:580] + 10*log10(2**4) + 3*w
plt.plot(x,y,c='orange', linewidth=1, label="%sm"%(4*RR))
y = computed_df.iloc[n,580:708] + 10*log10(2**5) + 4*w
plt.plot(x,y,c='gold', linewidth=1,label="%sm"%(5*RR))
y = computed_df.iloc[n,708:836] + 10*log10(2**6) + 5*w
plt.plot(x,y,c='yellow', linewidth=1,  label="%sm"%(6*RR))
y = computed_df.iloc[n,836:964] + 10*log10(2**7) + 6*w
plt.plot(x,y,c='lime', linewidth=1,label="%sm"%(7*RR))
y = computed_df.iloc[n,964:1092] + 10*log10(2**8) + 7*w
plt.plot(x,y,c='green', linewidth=1, label="%sm"%(8*RR))
y = computed_df.iloc[n,1092:1220] + 10*log10(2**9) + 8*w
plt.plot(x,y,c='turquoise', linewidth=1, label="%sm"%(8*RR))
y = computed_df.iloc[n,1220:1348] + 10*log10(2**10) + 9*w
plt.plot(x,y,c='aqua', linewidth=1, label="%sm"%(10*RR))
y = computed_df.iloc[n,1348:1476] + 10*log10(2**11) + 10*w
plt.plot(x,y,c='deepskyblue', linewidth=1,  label="%sm"%(11*RR))
y = computed_df.iloc[n,1476:1604]+ 10*log10(2**12) + 11*w
plt.plot(x,y,c='dodgerblue', linewidth=1,label="%sm"%(12*RR))
y = computed_df.iloc[n,1604:1732] + 10*log10(2**13) + 12*w
plt.plot(x,y,c='royalblue', linewidth=1, label="%sm"%(13*RR))
y = computed_df.iloc[n,1732:1860] + 10*log10(2**14) + 13*w
plt.plot(x,y,c='darkviolet', linewidth=1, label="%sm"%(14*RR))
y = computed_df.iloc[n,1860:1988] + 10*log10(2**15) + 14*w
plt.plot(x,y,c='purple', linewidth=1, label="%sm"%(15*RR))
plt.xlabel('Vertical Velocity / $ms^{-1}$') # labels the x axi
# plt.ylim(min(computed_df.iloc[n,132:388])-2,-60) # ensure the y limits are reasonable
# x = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
# my_xticks = [-5,-4,-3,-2,-1,0,1,2,3,4,5]
# plt.xticks(x, my_xticks)  # plots x axis ticks
plt.xlim((-64*velocity-1), (64*velocity+1))
plt.ylabel('Range Corrected Power / dB(AU) -- Waterfall Plot (%dB(AU))'%w) # labels the y axis
plt.title('All Height Ranges')  # plots the title
plt.legend(loc='upper center', bbox_to_anchor=(1.05, 1)) # plots a key
# title
plt.suptitle('%s, %s hrs: Power vs Vertical Velocity for Each Individual Height Range'%(date,computed_df.iloc[n,1]),fontsize=13,y=0.97)
plt.grid()
plt.show()



# Contour Plot
fig = go.Figure(data =
    go.Contour(
        # our z value is a list of each of the height ranges spectral power
        z=[computed_df.iloc[n,68:196],
            computed_df.iloc[n,196:324] + 10*log10(2**2),
            computed_df.iloc[n,324:452] + 10*log10(2**3),
            computed_df.iloc[n,452:580] + 10*log10(2**4),
            computed_df.iloc[n,580:708] + 10*log10(2**5),
            computed_df.iloc[n,708:836] + 10*log10(2**6),
            computed_df.iloc[n,836:964] + 10*log10(2**7),
            computed_df.iloc[n,964:1092] + 10*log10(2**8),
            computed_df.iloc[n,1092:1220] + 10*log10(2**9),
            computed_df.iloc[n,1220:1348] + 10*log10(2**10),
            computed_df.iloc[n,1348:1476] + 10*log10(2**11) ,
            computed_df.iloc[n,1476:1604]+ 10*log10(2**12),
            computed_df.iloc[n,1604:1732] + 10*log10(2**13),
            computed_df.iloc[n,1732:1860] + 10*log10(2**14),
            computed_df.iloc[n,1860:1988] + 10*log10(2**15)],
        y=[RR,2*RR,3*RR,4*RR,5*RR,6*RR,7*RR,8*RR,9*RR,10*RR,11*RR,12*RR,13*RR,14*RR,15*RR], # height ranges
        x=[i*(velocity) for i in range(-64,64)],  # vertical velocity as described above
        # horizontal axis - vertical velocity,
        colorscale="rainbow", # choose the rainbow colour scale
        colorbar=dict(
            title="Power / dB(AU)", # plots the title of the colour bar
            titleside="top",
            tickmode="array",
            # tickvals=[-108, -107, -106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
            #           -85,-84,-83], # gives the colour bar's intervals
            # ticktext=[-108, -107, -106,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
            #           -85,-84,-83], # plots the colour bar's text
            ticks=""),
        contours = dict(
            start= -108, # Can use (-107.304882 + 1.176044) for removing noise spectra
            size=2, # colour bar line width
            end = max(computed_df.iloc[n,1860:1988] + 10*log10(2**15)), # ends at -83
            showlines=True))) # Show the contour lines
fig.update_layout(
    title={
        'text': "%s, %s hrs: Contour Plot - Power Over Height and Velocity "%(date,computed_df.iloc[n,1]), # plots the title
        'y':0.9, # aligns the title
        'x':0.487, # aligns the title
        'xanchor': 'center',
        'yanchor': 'top'},
         xaxis_title = "$Vertical~Velocity~ms^{-1}$", # labels the x axis
         yaxis_title = "Height (AHL) / m", # labels the y axis
         legend_title = "Range Corrected Power") # labels the colour bar
fig.update_xaxes(ticks="outside") # puts the x axis ticks outside the plot
fig.update_yaxes(ticks="outside") # puts the y axis ticks outside the plot
# fig.update_layout(
#     xaxis = dict(
#         tickmode = 'linear',
#         tick0 = -5, # x axis begins at -10
#         dtick = 1 # increases by 1
#     ))
fig.update_layout(
    yaxis = dict(
        tickmode = 'linear',
        tick0 = RR, # y axis begins at 60
        dtick = RR # increases by 60
    ))
fig.show()





# Height vs Total Power
# For this plot, we want to plot for 4 different time steps in the dataset. Below we have assigned these time stamp
# values but the user can change these if and when they wish to.
# Assign values, etc
m = -220
k = - 240
l = -260

# In order to plot Height vs Total Power we must add up the total power on the left hand side of the transient for
# each individual height range. This requires a bit of work. I am looking into making this code more concise but for now,
# the code works.

# First, we take the inputted n value.
# For n values - we add up their total spectra for each height range
y = computed_df.iloc[n,68:136] # This adds up the individual height range's total spectra on the left side of the transient
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1) # here we sum the linear values together
total_power_log1 = 10*log10(total_power_linear) # convert it back into dB

# The process described above is repeated for all individual height ranges, as can be seen below, and is then repeated
# for the additional time steps described by m, k and l above.

y = computed_df.iloc[n,196:264]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2 = 10*log10(total_power_linear)

y = computed_df.iloc[n,324:392]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3 = 10*log10(total_power_linear)

y = computed_df.iloc[n,452:520]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4 = 10*log10(total_power_linear)

y = computed_df.iloc[n,580:648]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5 = 10*log10(total_power_linear)

y = computed_df.iloc[n,708:776]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6 = 10*log10(total_power_linear)

y = computed_df.iloc[n,836:904]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7 = 10*log10(total_power_linear)

y = computed_df.iloc[n,964:1032]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1092:1160]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log9 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1220:1288]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log10 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1348:1416]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log11 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1476:1544]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log12 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1604:1672]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log13 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1732:1800]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log14 = 10*log10(total_power_linear)

y = computed_df.iloc[n,1860:1928]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log15 = 10*log10(total_power_linear)

# m values
y = computed_df.iloc[m,68:136] # This adds up the individual height range's total spectra on the left side of the transient
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1) # here we sum the linear values together
total_power_log1m = 10*log10(total_power_linear) # convert it back into dB

y = computed_df.iloc[m,196:264]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2m = 10*log10(total_power_linear)

y = computed_df.iloc[m,324:392]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3m = 10*log10(total_power_linear)

y = computed_df.iloc[m,452:520]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4m = 10*log10(total_power_linear)

y = computed_df.iloc[m,580:648]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5m = 10*log10(total_power_linear)

y = computed_df.iloc[m,708:776]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6m = 10*log10(total_power_linear)

y = computed_df.iloc[m,836:904]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7m = 10*log10(total_power_linear)

y = computed_df.iloc[m,964:1032]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1092:1160]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log9m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1220:1288]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log10m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1348:1416]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log11m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1476:1544]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log12m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1604:1672]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log13m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1732:1800]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log14m = 10*log10(total_power_linear)

y = computed_df.iloc[m,1860:1928]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log15m = 10*log10(total_power_linear)


# k values
y = computed_df.iloc[k,68:136] # This adds up the individual height range's total spectra on the left side of the transient
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1) # here we sum the linear values together
total_power_log1k = 10*log10(total_power_linear) # convert it back into dB

y = computed_df.iloc[k,196:264]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2k = 10*log10(total_power_linear)

y = computed_df.iloc[k,324:392]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3k = 10*log10(total_power_linear)

y = computed_df.iloc[k,452:520]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4k = 10*log10(total_power_linear)

y = computed_df.iloc[k,580:648]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5k = 10*log10(total_power_linear)

y = computed_df.iloc[k,708:776]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6k = 10*log10(total_power_linear)

y = computed_df.iloc[k,836:904]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7k = 10*log10(total_power_linear)

y = computed_df.iloc[k,964:1032]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1092:1160]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log9k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1220:1288]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log10k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1348:1416]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log11k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1476:1544]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log12k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1604:1672]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log13k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1732:1800]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log14k = 10*log10(total_power_linear)

y = computed_df.iloc[k,1860:1928]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log15k = 10*log10(total_power_linear)



# l values
y = computed_df.iloc[l,68:136] # This adds up the individual height range's total spectra on the left side of the transient
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1) # here we sum the linear values together
total_power_log1l = 10*log10(total_power_linear) # convert it back into dB

y = computed_df.iloc[l,196:264]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log2l = 10*log10(total_power_linear)

y = computed_df.iloc[l,324:392]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log3l = 10*log10(total_power_linear)

y = computed_df.iloc[l,452:520]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log4l = 10*log10(total_power_linear)

y = computed_df.iloc[l,580:648]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log5l = 10*log10(total_power_linear)

y = computed_df.iloc[l,708:776]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log6l = 10*log10(total_power_linear)

y = computed_df.iloc[l,836:904]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log7l = 10*log10(total_power_linear)

y = computed_df.iloc[l,964:1032]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log8l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1092:1160]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log9l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1220:1288]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log10l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1348:1416]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log11l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1476:1544]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log12l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1604:1672]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log13l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1732:1800]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log14l = 10*log10(total_power_linear)

y = computed_df.iloc[l,1860:1928]
y1 = [10**(i/10) for i in y] # this takes the spectra (in dB) and returns it's linear value
total_power_linear = sum(y1)
total_power_log15l = 10*log10(total_power_linear)


# Plot the graph
y = [60,120,180,240,300,360,420,480,540,600,660,720,780,840,900]
# we assign the x axis to the total power in dB for each height range and each given n, m, k and l value.
x = [total_power_log1,total_power_log2,total_power_log3,total_power_log4,total_power_log5,total_power_log6,total_power_log7,total_power_log8,
     total_power_log9,total_power_log10,total_power_log11,total_power_log12,total_power_log13,total_power_log14,total_power_log15]
x1 = [total_power_log1m,total_power_log2m,total_power_log3m,total_power_log4m,total_power_log5m,total_power_log6m,total_power_log7m,total_power_log8m,
      total_power_log9m,total_power_log10m,total_power_log11m,total_power_log12m,total_power_log13m,total_power_log14m,total_power_log15m]
x2 = [total_power_log1k,total_power_log2k,total_power_log3k,total_power_log4k,total_power_log5k,total_power_log6k,total_power_log7k,total_power_log8k,
      total_power_log9k,total_power_log10k,total_power_log11k,total_power_log12k,total_power_log13k,total_power_log14k,total_power_log15k]
x3 = [total_power_log1l,total_power_log2l,total_power_log3l,total_power_log4l,total_power_log5l,total_power_log6l,total_power_log7l,total_power_log8l,
      total_power_log9l,total_power_log10l,total_power_log11l,total_power_log12l,total_power_log13l,total_power_log14l,total_power_log15l]
plt.figure()
# Plotting the four line graphs on the same plot
plt.plot(x,y,c='fuchsia',label='%s hrs (%s Time Step)'%(round(computed_df.iloc[n,1],5),n))
plt.plot(x1,y,c='orange',label='%s hrs (%s Time Step)'%(round(computed_df.iloc[m,1],5),m))
plt.plot(x2,y,c='r',label='%s hrs (%s Time Step)'%(round(computed_df.iloc[k,1],5),k))
plt.plot(x3,y,c='b',label='%s hrs (%s Time Step)'%(round(computed_df.iloc[l,1],5),l))
plt.xlabel('Total Power / dB(AU)') # labels x axis
plt.ylabel('Height (AGL) / m')  # labels y axis
plt.title('%s'%date,fontsize=10) # plots title
plt.ylim(0,960) # ensures the y limit is appropriate
plt.suptitle('Height vs Total Power',fontsize=13,y=0.97) # plots a title
plt.legend(loc="upper right") # plots a key
plt.yticks(np.arange(0, 961, 60)) # plots the y ticks along the y axis
plt.show()
