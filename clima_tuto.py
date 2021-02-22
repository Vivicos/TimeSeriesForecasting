import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/Victor/Documents/00 Trabajo/Programacion/jena_climate_2009_2016.csv')

time = pd.to_datetime(df.pop('Date Time'), format='%d.%m.%Y %H:%M:%S')
series = df['T (degC)']
series.index = time

print(df)

series.plot()
plt.show()