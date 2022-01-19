import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("titanic.csv")#zadanie 1 i zadanie 2 

data.columns

a = data.Survived

len(a)

data.Survived.value_counts()#zadanie 3

data2 = pd.read_csv("titanic.csv", index_col = "PassengerId")
data2

b = data2.loc[data2.Survived == 1]
c = data2.loc[data2.Survived == 0]

print("Amout of passengers:",int(len(a)))
print("Amount of survived passengers:",int(len(b)))
print("The percent of victims:",int(len(c)))
d = (len(b)/len(a))*100
print("The percent of survived passengers equals:",int(d),"%")#próba procentowego obliczenia, ale 100% jest rozwiązanie w jedną linię :)

plt.hist(data["Age"])#zadanie 4

data.Age.mean()#srednia z Age 

data.Age.describe()# druga metoda obliczeń 

temp1 = data2.loc[:20,["Survived","Sex", "Name"]]#zadanie 5
temp1

temp1.describe()

temp2 = temp1.loc[temp1.Survived == 1]
temp2.Survived.value_counts()
temp3 = temp1.loc[temp1.Survived == 0]
temp3.Survived.value_counts()