import pandas as pd
data = pd.read_csv("Trial.csv")#import dokumenta
data#print dokumenta
data.columns#funkcja cztoby uznat kakie kolonu w tablice
import matplotlib.pyplot as plt #import paketa dla postrojenia grafika
plt.plot(data['id'], data['wiek'])#postroenie linejnogo grafika gde x = id, y = wozrast
plt.hist(data['wiek']) #gistrograma dla wozrasta
trial = pd.read_excel("Trial.xlsx")#jesli mnogo sheets w faile to dobawit "sheet name = ..."
trial
type(trial)
a = trial["wiek"] #wzal odtelnyje kolony tablic i peredelal tablicu ta kotoraja mnie nuzna
b = trial["id"]
data2 = pd.DataFrame ({
    "Year": a,
    "id": b
})
trial2 = pd.read_excel("Trial.xlsx", index_col= "id")#izbawitsa ot numeracji w tablice
trial2
trial2["wiek"][19]#poisk po indeksam
data2
id_pacjenta = 13 #poisk pacjenta po nomeru identifikatora i poisk wyzyl li on ili net
if trial2["zgon"][id_pacjenta] == "tak":
  print(trial2["interwencja"][id_pacjenta])
#ispolzowanie funkcji loc/iloc
trial.wiek #segragacja wozrasta, filtr toj kolony kotoraja nas interesujet
trial.zgon.value_counts()#podszczot skolko wyzylo a skolko net
trial.loc[0,"wiek"]#najpierw nazwa obserwacji/mozem filtrowat danyje
trial.loc[:5, "wiek"] 
trial.loc[:5,["wiek","id"]] #perwyje 5 pointow obserawcji
trial.loc[10,["interwencja","zgon"]] #10j point, wytianuli nuznuju infu po niem
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
