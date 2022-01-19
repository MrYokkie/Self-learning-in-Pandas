import pandas as pd
import numpy as np
df = pd.read_csv("forbes_billionaires_geo.csv")
df.rank #na primer tak
df["Residence"].value_counts()
df["Citizenship"].value_counts()
polacy = df[df["Citizenship"] == "Poland"]#poisk i wkidywanie do peremennoj nuznuju nam kolonu
for index, row in df.iloc[:3,:].iterrows():
   #wytiagiwanie kazdogo wiersza po oczeregi czto by ich razdelit, sdelat czto-to s kazdym
   print("Index to", index)
   print("Row to:", row)

for index, row in df.iterrows():
   #wytiagiwanie kazdogo wiersza po oczeregi czto by ich razdelit, sdelat czto-to s kazdym
   print("Index to", index)
   print("Row to:", row)

for index, row in df.iterrows():
   #wytiagiwanie kazdogo wiersza po oczeregi czto by ich razdelit, sdelat czto-to s kazdym
   if row.Citizenship == "Poland":
     print("Yes")

df.loc[polacy,["Name","NetWorth"]]
df[df.Citizenship == df.Residence]
df.Status.value_counts()
sl = {
    "Married":"yes",
    "Divorced":"no",
    "Widowed":"no",
    "Single":"no",
    "In Relatiomship":"yes",
    "Separated":"no",
    "Widowed , Remarried":"yes",
    "Engaged":"yes"
}

df.Status.replace(sl)# peremestili peremennyje s kolon w slowar
def vc(s): # funkcja kotoraja ubirajet braki danych
  return s.value_counts(dropna = False)
vc(df.Status)
df["Relationship"] = df.Status.replace(sl)
vc(df.Relationship)
a
b = ["yes","no","no","no", "yes","no","yes","yes"]
dict(zip(a,b)) # funkcja zip skleiwajet neskolko list w python
#paczka pingouin dla statistiki w python
!pip install pingouin
df.NetWorth
png.corr(df.NetWorth, df.Age)# poisk korelacji mezdu czemto a czemto
self_made = (df.Self_made == "True")
df.Self_made
png.corr(df[self_made].NetWorth, df[self_made].Age)
df.Children == 0 # poisk braka danych
df.Children == 1 
b = (df.loc[df["Children"] >= 1,"NetWorth"])
c = (df.loc[df["Children"].is_na(), "NetWorth"])
png.ttest(dzietni, bezdzietni) #t test dla detnych i bezdetnych
png.chi2_independence(df, "Relationship","Self_made")
e,o png.chi2_independence(df, "Relationship","Self_made")
