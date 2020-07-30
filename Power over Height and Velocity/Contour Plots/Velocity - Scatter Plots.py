import matplotlib.pyplot as plt
import matplotlib as mpl
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
n = 3410

# # REMOVING NOISE SPECTRA - Include the Range Correction AND waterfall plot
p = 0# defining the percentile you want to remove
plt.figure()
y = computed_df.iloc[n,:]           # covers the entire row
percentile = np.percentile(y,p)    # Finds the 10th percentile of the entire row
percentile = 10**(percentile/10)

# CONTOUR PLOT

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
        y3.append(1000000)
y9 = [10*log10(j) for j in y3]
y9 = [(x + 10*log10(2**6))for x in y9]
for k, i in enumerate(y9):
    if i == (60 + 10*log10(2**6)):
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

# Now we have subtracted the percentiles for each height range we can begin to plot a scatter contour plot

# Plotting the 3D Graph

fig = plt.figure(figsize=(15,5))
ax = fig.gca(projection = '3d')
x = [i*(2*0.03898614179) for i in range(-128,128)]
z = np.array(y4)
# Assign the colour:
col = np.where(z <=-120, 'none',
                            np.where(z <= -107, 'pink',
                            np.where(z <= -106, 'magenta',
                            np.where(z <= -105, 'fuchsia',
                            np.where(z <= -104, 'blueviolet',
                            np.where(z <= -103, 'darkviolet',
                            np.where(z<= -102, 'purple',
                            np.where(z<= -101, 'navy',
                            np.where(z<= -100, 'b',
                            np.where(z <= -99,'royalblue',
                            np.where(z <= -98,'dodgerblue' ,
                            np.where(z<=-97,'deepskyblue',
                            np.where(z<=-96,'aqua',
                            np.where(z<=-95,'turquoise',
                            np.where(z<=-94,'green',
                            np.where(z<=-93,'lime',
                            np.where(z<=-92,'gold',
                            np.where(z<=-91,'yellow',
                            np.where(z<=-90,'orange',
                            np.where(z<=-89,'darkorange',
                            np.where(z<=-88,'red',
                            np.where(z<=-87,'crimson',
                            np.where(z<=0,'brown',
                                     'none')))))))))))))))))))))))
# We repeat this for two points in the height range
ax.scatter(x, [75]*256, y4,s=7,c=col)
#ax.scatter(x, [93.75]*256, y4,s=3,c=col,marker = "s")


z = np.array(y5)
yax1 = [2]*256 #[((225/2) + ((75*i)/256)) for i in range(256)]
col = np.where(z <=-110, 'none',
                            np.where(z <= -107, 'pink',
                            np.where(z <= -106, 'magenta',
                            np.where(z <= -105, 'fuchsia',
                            np.where(z <= -104, 'blueviolet',
                            np.where(z <= -103, 'darkviolet',
                            np.where(z<= -102, 'purple',
                            np.where(z<= -101, 'navy',
                            np.where(z<= -100, 'b',
                            np.where(z <= -99,'royalblue',
                            np.where(z <= -98,'dodgerblue' ,
                            np.where(z<=-97,'deepskyblue',
                            np.where(z<=-96,'aqua',
                            np.where(z<=-95,'turquoise',
                            np.where(z<=-94,'green',
                            np.where(z<=-93,'lime',
                            np.where(z<=-92,'gold',
                            np.where(z<=-91,'yellow',
                            np.where(z<=-90,'orange',
                            np.where(z<=-89,'darkorange',
                            np.where(z<=-88,'red',
                            np.where(z<=-87,'crimson',
                            np.where(z<=0,'brown',
                                     'none')))))))))))))))))))))))
#ax.scatter(x, [112.5]*256, y5,s=7,c=col,marker="s")
#ax.scatter(x, [131.25]*256, y5,s=3,c=col)
ax.scatter(x, [150]*256, y5,s=7,c=col)
#ax.scatter(x, [168.75]*256, y5,s=3,c=col)



z = np.array(y6)
yax2 = [3]*256 #[((375/2) + ((75*i)/256)) for i in range(256)]
col = np.where(z <=-110, 'none',
                            np.where(z <= -107, 'pink',
                            np.where(z <= -106, 'magenta',
                            np.where(z <= -105, 'fuchsia',
                            np.where(z <= -104, 'blueviolet',
                            np.where(z <= -103, 'darkviolet',
                            np.where(z<= -102, 'purple',
                            np.where(z<= -101, 'navy',
                            np.where(z<= -100, 'b',
                            np.where(z <= -99,'royalblue',
                            np.where(z <= -98,'dodgerblue' ,
                            np.where(z<=-97,'deepskyblue',
                            np.where(z<=-96,'aqua',
                            np.where(z<=-95,'turquoise',
                            np.where(z<=-94,'green',
                            np.where(z<=-93,'lime',
                            np.where(z<=-92,'gold',
                            np.where(z<=-91,'yellow',
                            np.where(z<=-90,'orange',
                            np.where(z<=-89,'darkorange',
                            np.where(z<=-88,'red',
                            np.where(z<=-87,'crimson',
                            np.where(z<=0,'brown',
                                     'none')))))))))))))))))))))))
##ax.scatter(x, [187.5]*256, y6,s=7,c=col,marker="s")
#ax.scatter(x, [206.25]*256, y6,s=3,c=col)
ax.scatter(x, [225]*256, y6, s=7, c=col)
#ax.scatter(x, [243.75]*256, y6, s=3, c=col)


z = np.array(y7)
yax3 = [4]*256 #[((525/2) + ((75*i)/256)) for i in range(256)]
col = np.where(z <=-110, 'none',
                            np.where(z <= -107, 'pink',
                            np.where(z <= -106, 'magenta',
                            np.where(z <= -105, 'fuchsia',
                            np.where(z <= -104, 'blueviolet',
                            np.where(z <= -103, 'darkviolet',
                            np.where(z<= -102, 'purple',
                            np.where(z<= -101, 'navy',
                            np.where(z<= -100, 'b',
                            np.where(z <= -99,'royalblue',
                            np.where(z <= -98,'dodgerblue' ,
                            np.where(z<=-97,'deepskyblue',
                            np.where(z<=-96,'aqua',
                            np.where(z<=-95,'turquoise',
                            np.where(z<=-94,'green',
                            np.where(z<=-93,'lime',
                            np.where(z<=-92,'gold',
                            np.where(z<=-91,'yellow',
                            np.where(z<=-90,'orange',
                            np.where(z<=-89,'darkorange',
                            np.where(z<=-88,'red',
                            np.where(z<=-87,'crimson',
                            np.where(z<=0,'brown',
                                     'none')))))))))))))))))))))))
###ax.scatter(x, [262.5]*256, y7, s=7, c=col,marker="s")
#ax.scatter(x, [281.25]*256, y7, s=3, c=col)
ax.scatter(x, [300]*256, y7, s=7, c=col)
#ax.scatter(x, [318.75]*256, y7, s=3, c=col)


z = np.array(y8)
yax4 = [5]*256 #[((675/2) + ((75*i)/256)) for i in range(256)]
col = np.where(z <=-110, 'none',
                            np.where(z <= -107, 'pink',
                            np.where(z <= -106, 'magenta',
                            np.where(z <= -105, 'fuchsia',
                            np.where(z <= -104, 'blueviolet',
                            np.where(z <= -103, 'darkviolet',
                            np.where(z<= -102, 'purple',
                            np.where(z<= -101, 'navy',
                            np.where(z<= -100, 'b',
                            np.where(z <= -99,'royalblue',
                            np.where(z <= -98,'dodgerblue' ,
                            np.where(z<=-97,'deepskyblue',
                            np.where(z<=-96,'aqua',
                            np.where(z<=-95,'turquoise',
                            np.where(z<=-94,'green',
                            np.where(z<=-93,'lime',
                            np.where(z<=-92,'gold',
                            np.where(z<=-91,'yellow',
                            np.where(z<=-90,'orange',
                            np.where(z<=-89,'darkorange',
                            np.where(z<=-88,'red',
                            np.where(z<=-87,'crimson',
                            np.where(z<=0,'brown',
                                     'none')))))))))))))))))))))))
#ax.scatter(x, [337.5]*256, y8, s=7, c=col,marker="s")
#ax.scatter(x, [356.25]*256, y8, s=3, c=col)
ax.scatter(x, [375]*256, y8, s=7, c=col)
#ax.scatter(x, [393.75]*256, y8, s=3, c=col)


z = np.array(y9)
yax5 = [6]*256 #[((825/2) + ((75*i)/256)) for i in range(256)]
col = np.where(z <=-110, 'none',
                            np.where(z <= -107, 'pink',
                            np.where(z <= -106, 'magenta',
                            np.where(z <= -105, 'fuchsia',
                            np.where(z <= -104, 'blueviolet',
                            np.where(z <= -103, 'darkviolet',
                            np.where(z<= -102, 'purple',
                            np.where(z<= -101, 'navy',
                            np.where(z<= -100, 'b',
                            np.where(z <= -99,'royalblue',
                            np.where(z <= -98,'dodgerblue' ,
                            np.where(z<=-97,'deepskyblue',
                            np.where(z<=-96,'aqua',
                            np.where(z<=-95,'turquoise',
                            np.where(z<=-94,'green',
                            np.where(z<=-93,'lime',
                            np.where(z<=-92,'gold',
                            np.where(z<=-91,'yellow',
                            np.where(z<=-90,'orange',
                            np.where(z<=-89,'darkorange',
                            np.where(z<=-88,'red',
                            np.where(z<=-87,'crimson',
                            np.where(z<=-0,'brown',
                                     'none')))))))))))))))))))))))
#ax.scatter(x, [412.5]*256, y9, s=7, c=col,marker="s")
#ax.scatter(x, [431.25]*256, y9, s=3, c=col)
ax.scatter(x, [450]*256,y9, s=7, c=col)
#ax.scatter(x, [468.75]*256,y9, s=3, c=col)

z = np.array(y10)
yax6 = [7]*256 #[((975/2) + ((75*i)/256)) for i in range(256)]
col = np.where(z <=-115, 'none',
                            np.where(z <= -107, 'pink',
                            np.where(z <= -106, 'magenta',
                            np.where(z <= -105, 'fuchsia',
                            np.where(z <= -104, 'blueviolet',
                            np.where(z <= -103, 'darkviolet',
                            np.where(z<= -102, 'purple',
                            np.where(z<= -101, 'navy',
                            np.where(z<= -100, 'b',
                            np.where(z <= -99,'royalblue',
                            np.where(z <= -98,'dodgerblue' ,
                            np.where(z<=-97,'deepskyblue',
                            np.where(z<=-96,'aqua',
                            np.where(z<=-95,'turquoise',
                            np.where(z<=-94,'green',
                            np.where(z<=-93,'lime',
                            np.where(z<=-92,'gold',
                            np.where(z<=-91,'yellow',
                            np.where(z<=-90,'orange',
                            np.where(z<=-89,'darkorange',
                            np.where(z<=-88,'red',
                            np.where(z<=-87,'crimson',
                            np.where(z<=0,'brown',
                                     'none')))))))))))))))))))))))
#ax.scatter(x, [487.5]*256,y10, s=7, c=col,marker="s")
#ax.scatter(x, [506.25]*256,y10, s=3, c=col)
ax.scatter(x, [525]*256,  y10, s=7, c=col)
#ax.scatter(x, [543.75]*256,  y10, s=3, c=col)
#ax.scatter(x, [562.5]*256,  y10, s=3, c=col)

#[0, 1, 2, 3, 4, u'D', 6, 7, 8, u's', u'|', 11, u'None', u'P', 9, u'x', u'X', 5, u'_', u'^', u' ',
# None, u'd', u'h', u'+', u'*', u',', u'o', u'.', u'1', u'p', u'3', u'2', u'4', u'H', u'v', u'', u'8', 10, u'&lt;', u'&gt;']

ax.set_ylabel('Height (AHL) / m')
ax.set_xlabel('Vertical Velocity ms$^{-1}$')
plt.suptitle('%s, %s hrs (%s Time Step): Contour Plot - Power Over Height and Velocity '
             '(%sth Percentile Removed)'%(date, computed_df.iloc[n,1],n,p), fontsize=13, y=0.97)
ax.set_ylim3d(0, 600)
ax.view_init(azim=270, elev=90)
ax.w_zaxis.line.set_lw(0.) # Gets rid of z-axis
ax.set_zticks([])
ax.tick_params(axis='both', which='major', pad=15)
ax.xaxis.labelpad = 20
ax.yaxis.labelpad = 20
ax.set_xlim3d(-10,10)
plt.show()
