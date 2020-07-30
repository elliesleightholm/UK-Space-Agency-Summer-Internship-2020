import dask.dataframe as dd
import numpy as np

# Creating the names for the headers (2052 headers altogether)
col_names = ['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point','Frequency Step Between Data Bins']
for i in range(1, 2049):
    col_names.append("Spectral Power " + str(i))

# Creating the dataframe
df = dd.read_csv('191001T000014.csv', sample=1000000000, names=col_names)

# Computes our dask.dataframe into a pandas dataframe so we can analyse the data and start plotting graphs
computed_df1 = df.compute()
# print(computed_df.iloc[105,1720:1735]) - anomalous data between SP1722 - 1726

# Since we begin plotting for Power Spectra, we must omit the first 4 columns from our dataset and subsequently,
# remove the transients too

computed_df = computed_df1.drop(['Date (YYMMDD)','Time of Day (Decimal Hours)','Frequency of First Spectral point',
                        'Frequency Step Between Data Bins','Spectral Power 254',
                        'Spectral Power 255','Spectral Power 256','Spectral Power 257','Spectral Power 258','Spectral Power 510',
                        'Spectral Power 511','Spectral Power 512','Spectral Power 513','Spectral Power 514','Spectral Power 766',
                        'Spectral Power 767','Spectral Power 768','Spectral Power 769','Spectral Power 770','Spectral Power 1024',
                        'Spectral Power 1025','Spectral Power 1026','Spectral Power 1027','Spectral Power 1028','Spectral Power 1278',
                        'Spectral Power 1279','Spectral Power 1280','Spectral Power 1281','Spectral Power 1282','Spectral Power 1534',
                        'Spectral Power 1535','Spectral Power 1536','Spectral Power 1537','Spectral Power 1538','Spectral Power 1790',
                        'Spectral Power 1791','Spectral Power 1792','Spectral Power 1793','Spectral Power 1794','Spectral Power 2047',
                        'Spectral Power 2048','Spectral Power 1','Spectral Power 2','Spectral Power 3',
                        'Spectral Power 4'],axis=1)


# We want to edit the colour code - we seek to find the average noise floor and the standard deviation of
# variability. We therefore take a dataset that has no transients and from a spectra where there are no non-noise peaks
# to do this we delete all the columns that are assigned to transients and then find a row that has no non-noise peaks

# We have dropped all of the transient columns from our dataset.

# We compute the mean power spectra and standard deviation:
print(computed_df.mean(axis=1))
print(computed_df.std(axis=1))

# 5756th Spectra gives spectra with no peaks other than noise power - after calculating we know that the average
# noise floor is -107.304882 and the standard deviation is 1.176044 so this is the range we will set our colour range
# to for our graphs. This allows no noise spectra to be plotted

# We use this and plot a 3D Graph and observe the findings