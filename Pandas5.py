
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("titanic.csv")
df

#https://seaborn.pydata.org/generated/seaborn.clustermap.html?highlight=sns%20clustermap

#info for whole df
df.info()

a = df["Survived"]
a
#df creating for mapping
survived_r =  {
    "0":"no",
    "1":"yes"
}
survived_r
#replace data as we need
a.replace(survived_r)

df
#package instalation for statistycal analysis
!pip install pingouin
#import as png
import pingouin as png
df.Age

df.info()
#joinplot with seaborna
sns.jointplot( x = "Age", y = "Fare",kind = "hex" ,data = df )
#correlation checking between features
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
df.iloc[:10,[0,2]]#search the indexs we need, in case we dont know the name of searases
a = "Poland"
df["Country name"]=="Poland"#search accordingly to vfeature
df.loc[:,"Country name"]
b = df.loc[df.loc[:,"Country name"]== a,"Country name"] 
df.loc[df.loc[:,"Country name"]== a,"Country name":"Ladder score"]
df.loc[df.loc[:,"Country name"]== a,"Country name":]# whole info towards to our indexes
df["Regional indicator"]=="Central and Eastern Europe"
df.loc[df["Regional indicator"]=="Central and Eastern Europe","Country name":"Ladder score"]
df.sort_values(by = "Logged GDP per capita")
df.sort_values(by = "Logged GDP per capita", ascending = False #ascending for reversable sorting
df_gdp = df.sort_values(by = "Logged GDP per capita", ascending = False)
df["Logged GDP per capita"] > 10
df.loc[df["Logged GDP per capita"] > 10, ["Country name","Ladder score"]]
df.loc[df["Logged GDP per capita"] > 10, ["Country name","Ladder score"]].sort_values(by = "Logged GDP per capita", ascending = False)
df["Logged GDP per capita"]>10 & df["Ladder score" < 6]
df["Ladder score"].mean()
df.groupby("Regional indicator")["Ladder score"].mean()
df.groupby("Regional indicator")["Ladder score"].describe()
