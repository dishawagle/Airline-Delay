from pandas import *
#import pandas as pd
#import seaborn as sns
import matplotlib.pyplot as plt
#%matplotlib inline
import collections
#sns.set_style("whitegrid")
auto = read_csv('C:/Users/Arihant/Downloads/2008.csv', nrows = 400000) 
d = collections.Counter(auto["Origin"]) + collections.Counter(auto["Dest"])
'''
auto1 = read_csv('C:/Users/Arihant/Downloads/1988.csv', nrows = 50000)
auto2 = read_csv('C:/Users/Arihant/Downloads/1989.csv', nrows = 50000) 
auto3 = read_csv('C:/Users/Arihant/Downloads/1990.csv', nrows = 50000) 
auto4 = read_csv('C:/Users/Arihant/Downloads/1991.csv', nrows = 50000) 
auto5 = read_csv('C:/Users/Arihant/Downloads/1992.csv', nrows = 50000) 
auto6 = read_csv('C:/Users/Arihant/Downloads/1993.csv', nrows = 50000) 
auto7 = read_csv('C:/Users/Arihant/Downloads/1994.csv', nrows = 50000)
auto8 = read_csv('C:/Users/Arihant/Downloads/1995.csv', nrows = 50000)
auto9 = read_csv('C:/Users/Arihant/Downloads/1996.csv', nrows = 50000)
auto10 = read_csv('C:/Users/Arihant/Downloads/1997.csv', nrows = 50000)
auto11 = read_csv('C:/Users/Arihant/Downloads/1998.csv', nrows = 50000)
auto12 = read_csv('C:/Users/Arihant/Downloads/1999.csv', nrows = 50000)
auto13 = read_csv('C:/Users/Arihant/Downloads/2000.csv', nrows = 50000)
auto14 = read_csv('C:/Users/Arihant/Downloads/2001.csv', nrows = 50000)
auto15 = read_csv('C:/Users/Arihant/Downloads/2002.csv', nrows = 50000)
auto16 = read_csv('C:/Users/Arihant/Downloads/2003.csv', nrows = 50000)
auto17 = read_csv('C:/Users/Arihant/Downloads/2004.csv', nrows = 50000)
auto18 = read_csv('C:/Users/Arihant/Downloads/2005.csv', nrows = 50000)
auto19 = read_csv('C:/Users/Arihant/Downloads/2006.csv', nrows = 50000)
auto20 = read_csv('C:/Users/Arihant/Downloads/2007.csv', nrows = 50000)
auto21 = read_csv('C:/Users/Arihant/Downloads/2008.csv', nrows = 50000)
'''



'''
+ collections.Counter(auto1["Origin"]) + collections.Counter(auto1["Dest"]) + collections.Counter(auto2["Origin"]) + collections.Counter(auto2["Dest"]) + collections.Counter(auto3["Origin"]) + collections.Counter(auto3["Dest"]) + collections.Counter(auto4["Origin"]) + collections.Counter(auto4["Dest"]) + collections.Counter(auto5["Origin"]) + collections.Counter(auto5["Dest"]) + collections.Counter(auto6["Origin"]) + collections.Counter(auto6["Dest"] + collections.Counter(auto7["Origin"]) + collections.Counter(auto7["Dest"]) + collections.Counter(auto8["Origin"]) + collections.Counter(auto8["Dest"]) + collections.Counter(auto9["Origin"]) + collections.Counter(auto9["Dest"]))
'''
airport = []
acount = []
airport = d.keys()
acount = d.values()

# get the size in inches



# plot and save in the same size as the original
fig = plt.figure(dpi = 100)
tick = xrange(len(airport))
LABELS = airport
plt.plot(tick,acount)
plt.xticks(tick,LABELS)
plt.tick_params(axis='x', labelsize=6)
plt.xticks(rotation='vertical')
plt.title("Most Crowded and Least Crowded Airports for years 1987-2008")
plt.ylabel("Frequency")
plt.xlabel("Airports")

#plt.show()
plt.savefig('airport.png')