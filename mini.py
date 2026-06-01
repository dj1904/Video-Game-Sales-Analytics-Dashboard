import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
fig, ax = plt.subplots(figsize=(14,8))
ax.axis("off")
border=Rectangle((0.02,0.02),0.96,0.96,fill=False,linewidth=5,edgecolor='Black',transform=ax.transAxes)
ax.add_patch(border)
title = "VIDEO GAME SALES ANALYSIS REPORT"
content = """
1. Top 10 Highest Selling Games
   -> Displays games with highest global sales.

2. Regional Sales Distribution
   -> Shows sales percentage by region.

3. Top Platforms by Worldwide Sales
   -> Compares total platform sales.

4. Regional Sales by Platform
   -> Shows platform-wise regional performance.
"""
ax.text(0.5, 0.9, title,
        fontsize=25,
        fontweight='bold',
        ha='center')
ax.text(0.05, 0.75, content,
        fontsize=17,
        va='top')
plt.savefig("introduction.png",bbox_inches='tight')
plt.show()

df=pd.read_csv("Video game sales.csv")
print(df)
b=df.drop("Game Name.1",axis=1)
a=b.drop_duplicates(subset="Game Name")
a.to_csv("updated.csv")
a[" Platform"]=a[" Platform"].str.split(":").str[1].str.strip()
a=a.head(2000)
a.to_csv("updated csv")
print(a[" Platform"])
print(a)
#print(df.columns)
#print(a.duplicated(subset=" Platform").sum())
#plt.figure(figsize=(10,6))
plt.xticks(rotation=90)
bars=plt.bar(a.sort_values(by="Total Worldwide Sales(millions)",ascending=False).head(10)["Game Name"],
             a.sort_values(by="Total Worldwide Sales(millions)",ascending=False).head(10)["Total Worldwide Sales(millions)"])
plt.bar_label(bars)
#plt.tight_layout()
plt.xlabel("Game Name")
plt.ylabel("Worldwide Sales")
plt.title("Top 10 Highest Selling Games Worldwide")
#print(a.columns)
plt.savefig("Topsellinggames.png",bbox_inches='tight')
plt.show()
total_country=[a[ 'Sales in Europe(millions)'].sum(),
                   a['Sales in Japan(millions)'].sum(),
                   a['Sales in North America(millions)'].sum(),
                   a['Sales in the rest world(millions)'].sum()]
labels=["Europe","Japan","North America","Rest World"]
plt.pie(total_country,labels=labels,autopct="%1.1f%%")
plt.title("Top 5 countries by worldwide")
plt.savefig("Topsalescountries.png",bbox_inches='tight')
plt.show()
bar1=a.groupby(" Platform")["Total Worldwide Sales(millions)"].sum().sort_values(ascending=False).head(10)
bar2=plt.bar(bar1.index, bar1.values)
plt.bar_label(bar2)
plt.xlabel("platform")
plt.ylabel("Total worldwide sales(millions)")
plt.title("Top platform company")
plt.xticks(rotation=90)
plt.savefig("highestplatform.png",bbox_inches='tight')
plt.show()
c=a.groupby(" Platform")[["Sales in Europe(millions)","Sales in Japan(millions)","Sales in North America(millions)","Sales in the rest world(millions)"]].sum()
ax=c.plot(kind="bar", figsize=(12,12))
plt.xlabel("Platform")
plt.ylabel("Sales(Millions)")
plt.title("Regional Sales by platform")
plt.xticks(rotation=90)
plt.savefig("alloversalesbyregional.png",bbox_inches='tight')
plt.show()
fig,ax=plt.subplots(figsize=(14,8))
ax.axis("off")
border=Rectangle((0.02,0.02),0.96,0.96,fill=False,linewidth=5,edgecolor="blue",transform=ax.transAxes)
ax.add_patch(border)
ax.text(0.5,0.90,"CONCLUSION",fontsize=24,fontweight='bold',ha='center')
conclusion=("""
1)In top 10 high selling games worldwide WII sports has 87.74% out of 100

2)Among the top 5 countries North America has the highest sales.

3)Among the Top platform company Playstation 2 has dominated
    the highest worldwide sales(millions) around 620.92

4)By the comparison of countries and the platforms North America is
    the highest in each gaming and platform of the sales

5)Regional Prefernce vary across different platforms and games
""")
ax.text(0.05,0.75,conclusion,fontsize=14,va="top")
plt.savefig("Conclusion_Page.png", bbox_inches='tight')
plt.show()
