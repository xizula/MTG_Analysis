import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# Sheoldred, the Apocalypse _phyrexian_ [DMU] (F) - phyrexin foil
# Sheoldred, the Apocalypse _showcase_ [DMU] - showcase
# Sheoldred, the Apocalypse [DMU] - normal

# Vampiric Tutor _J18_ [PRM-JUD] (F) - Foil, J18 (Judge Promos)
# Vampiric Tutor [CMR] - normal (Commander Tutor)
# Vampiric Tutor [6ED] - normal (Classic Sixth Edition)

def plot_card(data, col, lab, x, y):
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

    
    plt.plot(data["Date"], data["Price"], color=col, label = lab)

    # adnotacja max
    bbox_props = dict(boxstyle="square,pad=0.3", fc="w", ec=col, lw=0.72)
    arrowprops=dict(arrowstyle="->",connectionstyle="angle3,angleA=0,angleB=60", color=col)
    kw = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="right", va="top")
    plt.annotate(txt_max, xy=(xmax, ymax), xytext=(1-2*y,1), **kw)

    # adnotacja min
    kw = dict(xycoords='data',textcoords="axes fraction", arrowprops=arrowprops, bbox=bbox_props, ha="left", va="bottom")
    plt.annotate(txt_min, xy=(xmin, ymin), xytext=(2*y,-0.1), **kw)



plt.figure(figsize=[15,8])

# Sheoldred, the Apocalypse
data1 = pd.read_csv('cards/comparison/Sheoldred, the Apocalypse [DMU].csv', header=None, names=["Date", "Price"])
data1["Date"] =  data1["Date"].astype('datetime64[ns]')
data2 = pd.read_csv('cards/comparison/Sheoldred, the Apocalypse _showcase_ [DMU].csv', header=None, names=["Date", "Price"])
data2["Date"] =  data2["Date"].astype('datetime64[ns]')
data3 = pd.read_csv('cards/comparison/Sheoldred, the Apocalypse _phyrexian_ [DMU] (F).csv', header=None, names=["Date", "Price"])
data3["Date"] =  data3["Date"].astype('datetime64[ns]')

plot_card(data1, 'blue', 'Normal', 0.5, 0.1)
plot_card(data2, 'red', 'Showcase', 0.6, 0.2)
plot_card(data3, 'green', 'Foil, Phyrexin', 0.7, 0.3)


# Lightning Bolt
# data1 = pd.read_csv('cards/comparison/Lightning Bolt [LEA].csv', header=None, names=["Date", "Price"])
# data1["Date"] =  data1["Date"].astype('datetime64[ns]')
# data2 = pd.read_csv('cards/comparison/Lightning Bolt [4ED].csv', header=None, names=["Date", "Price"])
# data2["Date"] =  data2["Date"].astype('datetime64[ns]')
# data3 = pd.read_csv('cards/comparison/Lightning Bolt [M10].csv', header=None, names=["Date", "Price"])
# data3["Date"] =  data3["Date"].astype('datetime64[ns]')
# data4 = pd.read_csv('cards/comparison/Lightning Bolt [2X2].csv', header=None, names=["Date", "Price"])
# data4["Date"] =  data4["Date"].astype('datetime64[ns]')

# plot_card(data1, 'blue', 'Limited Edition Alpha', 0.5, 0)
# plot_card(data2, 'red', 'Fourth Edition', 0.6, 0.1)
# plot_card(data3, 'green', 'Magic 2010', 0.7, 0.2)
# plot_card(data4, 'orange', 'Double Masters 2022', 0.8, 0.3)




# Vampiric Tutor
# data1 = pd.read_csv('cards/comparison/Vampiric Tutor _J18_ [PRM-JUD] (F).csv', header=None, names=["Date", "Price"])
# data1["Date"] =  data1["Date"].astype('datetime64[ns]')
# data2 = pd.read_csv('cards/comparison/Vampiric Tutor [CMR].csv', header=None, names=["Date", "Price"])
# data2["Date"] =  data2["Date"].astype('datetime64[ns]')
# data3 = pd.read_csv('cards/comparison/Vampiric Tutor [6ED].csv', header=None, names=["Date", "Price"])
# data3["Date"] =  data3["Date"].astype('datetime64[ns]')

# plot_card(data1, 'blue', 'Judge Promos (Foil, J18)', 0.5, 0.1)
# plot_card(data2, 'red', 'Commander Tutor (normal)', 0.6, 0.2)
# plot_card(data3, 'green', 'Classic Sixth Edition (normal)', 0.7, 0.3)



plt.ylim(bottom=0)
plt.legend()
plt.title("Porównanie cen")
plt.xlabel("Data")
plt.ylabel("Cena")
plt.show()