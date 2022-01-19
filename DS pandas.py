import pandas as pd
data = pd.read_csv("Trial.csv")
data
data.columns
import matplotlib.pyplot as plt
plt.plot(data['id'], data['wiek'])
plt.hist(data['wiek'])
trial = pd.read_excel("Trial.xlsx")#jesli mnogo sheets w faile to dobawit "sheet name = ..."
trial
type(trial)
a = trial["wiek"]
b = trial["id"]
data2 = pd.DataFrame ({
    "Year": a,
    "id": b
})
trial2 = pd.read_excel("Trial.xlsx", index_col= "id")#izbawitsa ot numeracji w tablice
trial2
trial2["wiek"][19]#poisk po indeksam
data2
id_pacjenta = 13
if trial2["zgon"][id_pacjenta] == "tak":
  print(trial2["interwencja"][id_pacjenta])

trial.wiek
trial.zgon.value_counts()
trial.loc[0,"wiek"]#najpierw nazwa obserwacji/mozem filtrowat danyje
trial.loc[:5, "wiek"]
trial.loc[:5,["wiek","id"]]
trial.loc[10,["interwencja","zgon"]]
trial.loc[4:10:2,["interwencja","zgon"]]
trial.loc[5:10, "wiek":"zgon"]
trial.loc[trial.zgon == "tak","wiek"]
trial.loc[trial.zgon == "tak","wiek"].mean()
trial.loc[trial.zgon == "tak","wiek"].describe()
trial.loc[4,"wiek"]
trial.loc[4:10, ["wiek","id"]]
trial[["wiek","zgon"]]
trial.loc[:,["zgon","wiek"]]#obratnaja posledowatelnost
