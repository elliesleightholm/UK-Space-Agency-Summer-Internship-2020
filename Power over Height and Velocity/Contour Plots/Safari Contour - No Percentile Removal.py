import plotly.graph_objects as go
from math import log10
import dask.dataframe as dd

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

# Begin the Contour Plot

# Assign the row
n = 50

# Begin plotting the contour plot for power over height and velocity
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
