#import of nescessary packages
import pandas as pd
import matplotlib.pyplot as plt
#within first lessone as a homework DataFrame has been created
a = (12523,32525,236264,96454234,124719820)
b = ("Ukrain","Poland","Germany","USA","China")
c = (2019)
d = (42000000,32000000, 83000000,328000000,170000000)
#To check all lists applied for dataframe creating
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
#extract all info tpwards to df
df.describe()
#plotting a lineplot with Pandas
plt.plot(df['Country'],df["GDP"])
