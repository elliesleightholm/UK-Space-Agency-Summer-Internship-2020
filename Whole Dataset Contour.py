import plotly.graph_objects as go
import dask.dataframe as dd

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i))

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

# Creating the dataframe
df = dd.read_csv('191109T000013.csv', sample=1000000000, names=col_names)

# Computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df1 = df.compute()

# Creates the date of the dataset
from datetime import datetime
computed_df2 = computed_df1.astype(int)
a = '%s'%(computed_df2.iloc[0,0] + 20000000)
date = datetime.strptime(a, '%Y%m%d').strftime('%d/%m/%Y')

# We need to drop the first four columns before we plot as they do not observe spectral power
computed_df = computed_df1.drop(['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point',
                        'Frequency Step Between Data Bins'],axis=1)


# We reassign any transients to a value below the minimum value of the dataset
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

# Create our frequency list for our y axis
frequency = [i*18.46621255 for i in range(0,2048)]

# Create a list that appends every column in the dataset and plot this as z
z = []
for i in range(len(computed_df.iloc[1,:].tolist())):
    z.append(computed_df.iloc[:,i])

# Begin plotting the contour
fig = go.Figure(data =
    go.Contour(
        z=z, # Power Spectra for each row
        x=computed_df1.iloc[:,1].tolist(), # Time of Day
        y=frequency, # Frequency
        colorscale=[[(0), 'white'],             # We create our own colour range
                    [(1/24), 'darkviolet'],
                    [(2/24), 'royalblue'],
                    [(3/24), 'dodgerblue'],
                    [(4/24), 'deepskyblue'],
                    [(5/24), 'aqua'],
                    [(6/24), 'turquoise'],
                    [(7/24), 'green'],
                    [(8/24), 'lime'],
                    [(3/7), 'yellow'],
                    [(11/21), 'gold'],
                    [(13/21), 'orange'],
                    [(5/7), 'darkorange'],
                    [(17/21), 'red'],
                    [(19/21), 'crimson'],
                    [1.0, 'brown']],
        colorbar=dict(
            title="Power / dB(AU)",
            titleside="top",
            tickvals=[(-107.304882 + 1.176044),-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
                      -85,-84,-83,-82,-81,-80],  # Assign the tick intervals
            ticktext=[-106.1288,-105,-104,-103,-102,-101,-100,-99,-98,-97,-96,-95,-94,-93,-92,-91,-90,-89,-88,-87,-86,
                      -85,-84,-83,-82,-81,-80],  # Assign the text for each tick
           ticks="",),
        contours = dict(
           start= (-107.304882 + 1.176044), # this is the minimum value - anthing below this is noise floor
           size=0.5,
           end = -80,
           showlines=False))) # We choose not to include contour lines as it affects the visualisation of data

fig.update_layout(
    title={
        'text': "%s: Contour Plot - Entire Dataset"%date,
        'y':0.9,
        'x':0.487,
        'xanchor': 'center',
        'yanchor': 'top'},
         xaxis_title = "Time of Day / Decimal Hours",
         yaxis_title = "Frequency / Hz")
fig.update_xaxes(ticks="outside")
fig.update_yaxes(ticks="outside")
fig.update_layout(
    yaxis = dict(
        tickmode = 'linear',
        tick0 = 0,
        dtick = 5000
    ))
fig.update_layout(
    xaxis = dict(
        tickmode = 'linear',
        tick0 = min(computed_df1.iloc[:,1].tolist()) + 1,
        dtick = (max(computed_df1.iloc[:,1].tolist()) - min(computed_df1.iloc[:,1].tolist()))/10
    ))
fig.show()
