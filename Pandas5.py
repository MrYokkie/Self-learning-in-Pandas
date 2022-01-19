#import paketow wkluczaja seaborn
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("titanic.csv")
df
#seaborn mozna skripty smotret po ssylke nize
#https://seaborn.pydata.org/generated/seaborn.clustermap.html?highlight=sns%20clustermap

#info na wse df
df.info()

a = df["Survived"]
a
#sozdanie dataframa dla replecji
survived_r =  {
    "0":"no",
    "1":"yes"
}
survived_r
#komanda perenosa danych w drugoj dataframe
a.replace(survived_r)

df
#instalacja pakieta dla statistiki
!pip install pingouin
#import pekata
import pingouin as png
df.Age

df.info()
#joinplot iz seaborna
sns.jointplot( x = "Age", y = "Fare",kind = "hex" ,data = df )
#koleracjia mezdu kolumnami
png.corr(df.Age, df.Fare)

sr =df.loc[df.Survived == "1"]
sr

png.ttest(sr.Survived, sr.Age)

sr1 =df.loc[df.Survived == 0]
sr1

png.ttest(sr1.Survived, sr1.Age)

import pandas as pd
data = pd.read_csv("world-happiness-report-2021.csv")
df["Ladder score"]
df["Ladder score"].describe() 
df["Ladder score"].hist()
df["Country name"]
df["Regional indicator"]
df["Regional indicator"].value_counts()
df.loc[:10,["Country name","Ladder score"]]
df.iloc[:10,[0,2]]#poisk po nomeru indexa, w sluczaje esli ne zamy nazwaniii column
a = "Poland"
df["Country name"]=="Poland"#libo peremennaja #wektorowoje srawnenie
df.loc[:,"Country name"]
b = df.loc[df.loc[:,"Country name"]== a,"Country name"]# poisk opredelionoj peremennoj w kolone,osnownoj sposob ndexirowania w pandase 
df.loc[df.loc[:,"Country name"]== a,"Country name":"Ladder score"]
df.loc[df.loc[:,"Country name"]== a,"Country name":]# wsia info po naszemu indexu
df["Regional indicator"]=="Central and Eastern Europe"
df.loc[df["Regional indicator"]=="Central and Eastern Europe","Country name":"Ladder score"]
df.sort_values(by = "Logged GDP per capita")
df.sort_values(by = "Logged GDP per capita", ascending = False #ascending dla obratnoj sortirowki)
df_gdp = df.sort_values(by = "Logged GDP per capita", ascending = False)
df["Logged GDP per capita"] > 10
df.loc[df["Logged GDP per capita"] > 10, ["Country name","Ladder score"]]
df.loc[df["Logged GDP per capita"] > 10, ["Country name","Ladder score"]].sort_values(by = "Logged GDP per capita", ascending = False)
df["Logged GDP per capita"]>10 & df["Ladder score" < 6]
df["Ladder score"].mean()
df.groupby("Regional indicator")["Ladder score"].mean()
df.groupby("Regional indicator")["Ladder score"].describe()