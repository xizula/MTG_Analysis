import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math
import matplotlib.dates as mdates

# *************************************************************************************************************** 
# Ceny dla całego zakresu czasowego
# Dla innej karty zmienić plik :)
data = pd.read_csv('cards/single/Tarmogoyf [FUT].csv', header=None, names=["Date", "Price"])
data["Date"] =  data["Date"].astype('datetime64[ns]')

# cena max
ymax = max(data["Price"])
x_max = list(np.where(data["Price"] == ymax))[0][0]
xmax = data["Date"][x_max]
txt_max = "max value ("+str(ymax)+")"

# cena min
ymin = min(data["Price"])
x_min = list(np.where(data["Price"] == ymin))[0][0]
xmin = data["Date"][x_min]
txt_min = "min value ("+str(ymin)+")"

plt.figure(figsize=[15,8])
plt.plot(data["Date"], data["Price"])

# adnotacja max
bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec="k", lw=0.72)
arrowprops=dict(arrowstyle="->",connectionstyle="angle3,angleA=0,angleB=60")
kw = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
plt.annotate(txt_max, xy=(xmax, ymax), xytext=(1,1), **kw)
plt.ylim(top=ymax+ymax/5)

# adnotacja min
kw = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="center", va="bottom")
plt.annotate(txt_min, xy=(xmin, ymin), xytext=(0.2,-0.1), **kw)
plt.ylim(bottom=ymin - ymin/5)

plt.title("Zmiany cen")
plt.xlabel("Data")
plt.ylabel("Cena")
plt.show()

# *****************************************************************************************************************
# Wykresy dla poszczególnych lat

years = data["Date"].dt.year
min_year = min(years)
max_year = max(years)
n = max_year - min_year + 1
col = int(math.ceil(n/4))
row = int(math.ceil(n/col))
elem = 1
plt.figure(figsize=[20,12])
for i in range(min_year, max_year+1, 1):
    data_year = data[data["Date"].dt.year == i]
    data_year = data_year.reset_index()

    # cena max
    if not data_year.empty:
        ymax = max(data_year["Price"])
        x_max = list(np.where(data_year["Price"] == ymax))[0][0]
        xmax = data_year["Date"][x_max]
        txt_max = "max value ("+str(ymax)+")"

        # cena min
        ymin = min(data_year["Price"])
        x_min = list(np.where(data_year["Price"] == ymin))[0][0]
        xmin = data_year["Date"][x_min]
        txt_min = "min value ("+str(ymin)+")"

    plt.subplot(row, col, elem)
    plt.plot(data_year["Date"], data_year["Price"])
    plt.xticks(rotation=30)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%b'))
    if not data_year.empty:      
        kw = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
        plt.annotate(txt_max, xy=(xmax, ymax), xytext=(1,1), **kw)
        plt.ylim(top=ymax+ymax/5)

        kw = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="center", va="center")
        plt.annotate(txt_min, xy=(xmin, ymin), xytext=(0.5,0.1), **kw)
        plt.ylim(bottom=ymin - ymin/5)

    plt.title("Zmiany cen dla roku " + str(i))
    plt.xlabel("Data")
    plt.ylabel("Cena")
    elem += 1
plt.tight_layout()
plt.show()

