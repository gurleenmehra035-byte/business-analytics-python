#GURLEEN 12514824
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=pd.read_csv (r"C:\Users\DELL\Downloads\Punjab & Sind bank BS.csv")
corr=df.corr(numeric_only=True). round(2)
print (corr.to_string())
plt.figure(figsize=(6,4))
sns.heatmap(corr,annot=True, cmap="coolwarm", square=True)
plt.title ("correlation Heatmap")
plt.show()



