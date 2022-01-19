import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("titanic.csv")
sns.relplot( x = "Age", y = "Fare",data = df )# zależność pomiędzy wiekiem a ceną na bilet/zadanie 1
sns.relplot( x = "Age", y = "Fare",kind = "line", data = df ) 
sns.catplot( y = "Fare", x = "Survived", kind = "violin", data = df) #Zadanie 2
sl = df.loc[df["Survived"]==1,"Survived":"Age"] #zadanie 3 - podejście 1
sns.displot(data = sl, x = "Age",kind = "kde")
sl1 = df.loc[df["Survived"]==0,"Survived":"Age"]
sns.displot(data = sl1, x = "Age",kind = "kde")
sns.displot(data = df, x = "Age",hue = df["Survived"]== 1, kind = "kde")# zadanie3 podejście 2 
sns.displot(data = df, x = "Age",hue = df["Survived"]== 0, kind = "kde")
sns.boxplot(y = "Pclass", x = "Sex", data = df) #zadanie 4 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy
df = pd.read_csv("stroke.csv")
df.head() # 5 perwych punktuw
#pearsonr(df.age, df.avg_glucose_level) posmotert bystro korreliaciju mezdu czem to a czem to
png.corr(df.age, df.avg_glucose_level)
!pip install pingouin
sns.jointplot(x = "age", y = "avg_glucose_level",kind = "hex", data = df) 
sns.relplot(x = "age", y = "avg_glucose_level", hue = "stroke",data = df,alpha = .5 ) # wyzow funkcji plo
# tak kak korelacja rabotat liniowo to korelacja ne wsegda mozet pokazywat nastojasciu korelacjiu
sns.relplot(x = "age", y = "avg_glucose_level", kind = "line",data = df)# wykres liniowy z przedzialem ufnosci
sns.relplot(x = "age", y = "avg_glucose_level", kind = "line", hue = "stroke",data = df) # z podzialem dla ludzi ktore mieli udar a ktore nie
sns.displot(data = df, x = "bmi") #dostajemy histogram
sns.displot(data = df, y = "bmi")
df[df.bmi>60]
udary = df[df.stroke == "yes"]
udary
sns.displot(data = udary, x="bmi", binwidth = 2)
sns.displot(data = df, x="bmi", kind = "kde")
sns.displot(data = df, x="age",hue = "stroke", kind = "kde")
sns.scatterplot(x = "age", y = "avg_glucose_level", hue = "stroke", data = df) # gestosc na osi 
sns.rugplot(x = "age", y = "avg_glucose_level", data = df)
sns.catplot(x="stroke",y = "avg_glucose_level",kind = "bar", data =df)
sns.catplot(x="stroke",y = "age", data =df)
sns.catplot(x = "stroke", y = "age", kind= "point", data= df)
sns.catplot(x = "stroke", y = "age", kind= "swarm", data= df)
sns.catplot(x = "stroke", y = "" data=df)
sns.catplot(x = "stroke", y = "avg_glucose_level", kind= "violin", data= df) # srawnenie gustosti danych w 2ch histogramach/rozklad danych
sns.catplot(y = "stroke", x = "avg_glucose_level", kind= "box", data= df)
sns.catplot(x = 'gender', y = "avg_glucose_level", data= udary, kind = "swarm")
sns.set_palette("twilight")
sns.catplot(x = 'stroke', y = "bmi", hue= "hypertension", kind = "violin", data = df)
g = sns.FacetGrid(df, col = "stroke")
g.map(sns.histplot, "bmi")
g = sns.FacetGrid(df, col = "stroke")# beret kolunmu kak os i potom na osnowe toj osi delaet grafik zawisimosti ot drugich weleczin
g.map(sns.scatterplot, "bmi", "age")
g = sns.FacetGrid(df, col = "stroke", row="hypertension")# beret kolunmu kak os i potom na osnowe toj osi delaet grafik zawisimosti ot drugich weleczin
g.map(sns.scatterplot, "bmi", "avg_glucose_level", alpha= .5) #wielokrotne wykresy
g = sns.FacetGrid(df, col = "stroke", row="hypertension")# beret kolunmu kak os i potom na osnowe toj osi delaet grafik zawisimosti ot drugich weleczin
g.map(sns.scatterplot, "age", "avg_glucose_level", alpha= .3) #wielokrotne wykresy
# zapis grafika kak fail
plt.savefig("wykres2.png", dpi = 300)