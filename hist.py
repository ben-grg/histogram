'''
Finding the Frequency of people born
on different months of a year Jan-Dec
and mapping the data to visual form Histogram
For this https://www.statista.com/chart/5814/the-months-of-the-year-with-the-most-births/
is being used as statistics
'''
from matplotlib import pyplot as plt
import numpy as np

from encryption import alpha

#mth = np.array(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
my_dict = {"jan" : 54951, "feb" : 51826, "mar" : 53561, "apr" : 53264, "may" : 56071
        ,"jun" : 55027,"jul" : 57754, "aug" : 56773,"sep" :57035
                   ,"oCt" : 55169,"nov" : 54054, "dec" :54754}

jan, feb, mar, apr, may, jun, jul, aug, sep, oCt, nov, dec = [],[],[],[],[],[],[],[],[],[],[],[]
jn,fb,mr,ap,my,ju,jl,ag,sp,ot,nv,dc = (np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([]),
                                       np.array([]),np.array([]),np.array([]),np.array([]),np.array([]),np.array([]))

def iteration(num,x,l):
    for i in range(0,l):
         num.append(x)

for j in my_dict:
    if j == "jan":
        iteration(jan,"Jan",my_dict["jan"])
        jn = np.array(jan)
    elif j == "feb":
        iteration(feb, "Feb", my_dict["feb"])
        fb = np.array(feb)
    elif j == "mar":
        iteration(mar, "Mar", my_dict["mar"])
        mr = np.array(mar)
    elif j == "apr":
        iteration(apr, "Apr", my_dict["apr"])
        ap = np.array(apr)
    elif j == "may":
        iteration(may, "May", my_dict["may"])
        my = np.array(may)
    elif j == "jun":
        iteration(jun, "Jun", my_dict["jun"])
        ju = np.array(jun)
    elif j == "jul":
        iteration(jul, "Jul", my_dict["jul"])
        jl = np.array(jul)
    elif j == "aug":
        iteration(aug, "Aug", my_dict["aug"])
        ag = np.array(aug)
    elif j == "sep":
        iteration(sep, "Sep", my_dict["sep"])
        sp = np.array(sep)
    elif j == "oCt":
        iteration(oCt, "Oct", my_dict["oCt"])
        ot = np.array(oCt)
    elif j == "nov":
        iteration(nov, "Nov", my_dict["nov"])
        nv = np.array(nov)
    elif j == "dec":
        iteration(dec, "Dec", my_dict["dec"])
        dc = np.array(dec)
    else:
        pass

mth_nump_array = np.concatenate((jn,fb,mr,ap,my,ju,jl,ag,sp,ot,nv,dc))
plt.figure(figsize=(14,7))
plt.style.use("seaborn-v0_8-whitegrid")
#print(plt.style.available)
bins, counts,patches = plt.hist(mth_nump_array,alpha=0.5, bins= 12 ,label="1995-2016",color="#2ab0ff")
plt.legend()
plt.ylim(50000,60000)
plt.xlabel("Months")
plt.ylabel("Daily birth per months")
plt.title("Avg numbers of daily birth per month in UK since 1995-2016")
for count, biN, patch in zip(bins,counts,patches):
    plt.text(biN, count, f'{count:.0f}' )
plt.show()

