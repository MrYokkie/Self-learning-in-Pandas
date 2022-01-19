import pandas as pd
df = pd.read_csv("titanic.csv")
df
df_najstarszych  = df.sort_values(by = "Age", ascending= False) #zadanie 2 sort od najstarszych do najmłodszych
df_najstarszych
df_najmlodszych = df.sort_values(by = "Age")
df_najmlodszych
df_najstarszych[:5] #zadanie 2 pięć najstarszych
df_najmlodszych[:5] #zadanie 2 pięć najmłodszych 
#zadanie 3 policzony procent Survived pasażerów 
first = df.loc[df["Pclass"]== 1,"Survived":"Age"] 
second = df.loc[df["Pclass"]== 2,"Survived":"Age"] #przeprowadziłem segregację po clasie 
third = df.loc[df["Pclass"]== 3,"Survived":"Age"]

first_survived = first.loc[df["Survived"]== 1,"Survived":"Age"] #segregacja liczby Survived w kazdej klasie
second_survived = second.loc[df["Survived"]== 1,"Survived":"Age"]
third_survived = third.loc[df["Survived"]== 1,"Survived":"Age"]

e = ((len(first_survived)*100)/len(first))
print("Procent przerzywszych pasażerów z pierszej klasy = " + str(e))
d = ((len(second_survived)*100)/len(second))
print("Procent przerzywszych pasażerów z drugiej klasy = " + str(d))
f = ((len(third_survived)*100)/len(third))
print("Procent przerzywszych pasażerów z treciej klasy = " + str(f))
 
a = df.loc[df["Sex"] == "female","Pclass":"Sex"] #zadanie 4  imiona i nazwiska wszystkich kobiet podróżujących pierwszą klasą
a
b = a.loc[df["Pclass"] == 1,"Pclass":"Sex"]
b

c = df.loc[df["Age"] >= 70, ["Survived","Name","Pclass","Age"]]#zadanie 5 pasażerów starszych niż 70 lat
c

c.value_counts("Survived")