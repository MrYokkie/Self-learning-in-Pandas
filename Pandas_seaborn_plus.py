import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_csv("titanic.csv")
sns.relplot( x = "Age", y = "Fare",,data = df ) # lets check dependence between passangers age and tickets price
sns.relplot( x = "Age", y = "Fare",kind = "line", data = df ) 
sns.catplot( y = "Fare", x = "Survived", kind = "violin", data = df) #Exer. 2
#Density plot creation for certain data|the goal was to check data distribution
sl = df.loc[df["Survived"]==1,"Survived":"Age"] #Excer. 2 - first oppr.
sns.displot(data = sl, x = "Age",kind = "kde")
sl1 = df.loc[df["Survived"]==0,"Survived":"Age"]
sns.displot(data = sl1, x = "Age",kind = "kde")
#Density plot creation for certain data|the goal was to check data distribution
sns.displot(data = df, x = "Age",hue = df["Survived"]== 1, kind = "kde")#Excer. 2 - secon oppr.
sns.displot(data = df, x = "Age",hue = df["Survived"]== 0, kind = "kde")
sns.boxplot(y = "Pclass", x = "Sex", data = df) #zadanie 4 


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy
df = pd.read_csv("stroke.csv")
df.head() # 5 perwych punktuw
#pearson (df.age, df.avg_glucose_level) posmotert bystro korreliaciju mezdu czem to a czem to
png.corr(df.age, df.avg_glucose_level)
!pip install pingouin
sns.jointplot(x = "age", y = "avg_glucose_level",kind = "hex", data = df) 
sns.relplot(x = "age", y = "avg_glucose_level", hue = "stroke",data = df,alpha = .5 ) # wyzow funkcji plo
# tak kak korelacja rabotat liniowo to korelacja ne wsegda mozet pokazywat nastojasciu korelacjiu
sns.relplot(x = "age", y = "avg_glucose_level", kind = "line",data = df)# wykres liniowy z przedzialem ufnosci
sns.relplot(x = "age", y = "avg_glucose_level", kind = "line", hue = "stroke",data = df) # z podzialem dla ludzi ktore mieli udar a ktore nie
sns.displot(data = df, x = "bmi") #Lets receive histogram
sns.displot(data = df, y = "bmi")
#Extract data with feture bmi > 60 value
df[df.bmi>60]
udary = df[df.stroke == "yes"]
#strockes 
sns.displot(data = udary, x="bmi", binwidth = 2)
sns.displot(data = df, x="bmi", kind = "kde")
sns.displot(data = df, x="age",hue = "stroke", kind = "kde")
sns.scatterplot(x = "age", y = "avg_glucose_level", hue = "stroke", data = df) # density on axes 
sns.rugplot(x = "age", y = "avg_glucose_level", data = df)
sns.catplot(x="stroke",y = "avg_glucose_level",kind = "bar", data =df)
sns.catplot(x="stroke",y = "age", data =df)
sns.catplot(x = "stroke", y = "age", kind= "point", data= df)
sns.catplot(x = "stroke", y = "age", kind= "swarm", data= df)
sns.catplot(x = "stroke", y = "" data=df)
sns.catplot(x = "stroke", y = "avg_glucose_level", kind= "violin", data= df) # two hists preparation with the reasone to compare them (data) taking into account different features
sns.catplot(y = "stroke", x = "avg_glucose_level", kind= "box", data= df)
sns.catplot(x = 'gender', y = "avg_glucose_level", data= udary, kind = "swarm")
sns.set_palette("twilight")
sns.catplot(x = 'stroke', y = "bmi", hue= "hypertension", kind = "violin", data = df)
g = sns.FacetGrid(df, col = "stroke")
g.map(sns.histplot, "bmi")
g = sns.FacetGrid(df, col = "stroke") #Practice for FacetGrid preparation
g.map(sns.scatterplot, "bmi", "age")
g = sns.FacetGrid(df, col = "stroke", row="hypertension")# beret kolunmu kak os i potom na osnowe toj osi delaet grafik zawisimosti ot drugich weleczin
g.map(sns.scatterplot, "bmi", "avg_glucose_level", alpha= .5) 
g = sns.FacetGrid(df, col = "stroke", row="hypertension")
g.map(sns.scatterplot, "age", "avg_glucose_level", alpha= .3) 
# save received figures
plt.savefig("wykres2.png", dpi = 300)
