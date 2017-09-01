#import ing pandas, and coverting the tab delimited data to dataframes
import pandas as pd
import matplotlib.pyplot as plt


#putting the column header names into variables
l_cols = ['Year', 'ppm(CO2)']
m_cols = ['Year', 'ppm(CO2)', 'Unc.']
n_cols = ['Annual Mean(GTA)','Year']

#declaring file paths to three variables
lawDome = "C:\\Users\\user\\Downloads\\LawDome.txt"
mauna = "C:\\Users\\user\\Downloads\\\Mauna Loa TabDelim.txt"
nasa = "C:\\Users\\user\\Downloads\\NASA TabDelim.txt"

#reading in the data files into pandas data frames
LawD = pd.read_csv(lawDome, sep='\t', names=l_cols, usecols=range(2))
maunaL = pd.read_csv(mauna, sep='\t', names=m_cols, usecols=range(3))
nasag = pd.read_csv(nasa, sep='\t', names=n_cols, usecols=range(2))




#converting columns in the dataframes to x and y variables i will use in scatter charts
x_val1 = maunaL[[0]]
y_val1 = maunaL[[1]]

x_val2 = LawD[[0]]
y_val2 = LawD[[1]]

x_val3 = nasag[[1]]
y_val3 = nasag[[0]]

plt.figure(figsize=(8, 5))
fig, ax1 = plt.subplots()
ax1.plot(x_val1, y_val1, color='b')

ax1.set_xlabel('Year')
# Make the y-axis label, ticks and tick labels match the line color.
ax1.set_ylabel('ppm(CO2)', color='b')
ax1.tick_params('y', colors='b')
ax2 = ax1.twinx()
ax2.plot(x_val3, y_val3, 'r-')
ax2.set_ylabel('Global Temp Anomaly', color='r')
ax2.tick_params('y', colors='r')
fig.tight_layout()
plt.show()


#concatenating the dataframe columns into one dataframe.
correlation_table = pd.concat([x_val1,y_val3, y_val1], axis=1)
#calling the corr() function that gives a correlation table below
correlation_table.corr()

#checking the spearman method correlation score
spearman = correlation_table['Annual Mean(GTA)'].corr(correlation_table['ppm(CO2)'], method='spearman') 
spearman