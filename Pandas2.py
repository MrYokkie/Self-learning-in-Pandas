import pandas as pd #Import Pandas
data = pd.read_csv("Trial.csv") #import csv file
data
data.columns
import matplotlib.pyplot as plt #import matplotlib
plt.plot(data['id'], data['wiek'])
plt.hist(data['wiek']) 
trial = pd.read_excel("Trial.xlsx")
trial
type(trial)
a = trial["wiek"] #extract a series for df creation
b = trial["id"]
data2 = pd.DataFrame ({
    "Year": a,
    "id": b
})
trial2 = pd.read_excel("Trial.xlsx", index_col= "id")
trial2
trial2["wiek"][19]
data2
id_pacjenta = 13 #search of patient number 13
if trial2["zgon"][id_pacjenta] == "tak":
  print(trial2["interwencja"][id_pacjenta])
#loc/iloc functions use
trial.wiek 
trial.zgon.value_counts()
trial.loc[0,"wiek"]
trial.loc[:5, "wiek"] 
trial.loc[:5,["wiek","id"]] 
trial.loc[10,["interwencja","zgon"]] 
trial.loc[4:10:2,["interwencja","zgon"]]
trial.loc[5:10, "wiek":"zgon"]
trial.loc[trial.zgon == "tak","wiek"]
trial.loc[trial.zgon == "tak","wiek"].mean()
trial.loc[trial.zgon == "tak","wiek"].describe()
trial.loc[4,"wiek"]
trial[4:10, "wiek"]
trial.loc[4:10, ["wiek","id"]]
trial[["wiek","zgon"]]
trial.loc[:,["zgon","wiek"]]#obratnaja posledowatelnost
