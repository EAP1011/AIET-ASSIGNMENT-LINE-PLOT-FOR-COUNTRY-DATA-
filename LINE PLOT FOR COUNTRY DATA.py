import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("CountryGrp.csv")
camt=df.groupby("Name")
oamtc=camt.get_group("China")
oamti=camt.get_group("India")
oamtj=camt.get_group("Japan")
month=df["Month"].unique().tolist()
plt.plot(month,oamtc["Order Amount"])
plt.plot(month,oamti["Order Amount"])
plt.plot(month,oamtj["Order Amount"])
plt.legend(["China","India","Japan"])
plt.xlabel("Month")
plt.ylabel("Order Amount")
plt.title("Country Orders")
plt.show()
