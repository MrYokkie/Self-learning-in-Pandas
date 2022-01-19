#import neobchodimych paketow
import pandas as pd
import matplotlib.pyplot as plt
#sozdanie list dla tablicy (daliee DataFrame)
a = (12523,32525,236264,96454234,124719820)
b = ("Ukrain","Poland","Germany","USA","China")
c = (2019)
d = (42000000,32000000, 83000000,328000000,170000000)
#Pokaz wsech listow
print(a)
print(b)
#sozdanie tablicy pri ispolzowanii funkcjii n = pd.DataFrame({})
df = pd.DataFrame({
    "GDP": a,
    "Country": b,
    "Year":c,
    "Population":d
})

print(df)
#osnownyje danyje otnositelno tablicy
df.describe()
#postrojka linejnogo grafika
plt.plot(df['Country'],df["GDP"])