import glob
import matplotlib.pyplot as plt
import pandas as pd
from saxs_plots import real_space_plotter

dats = glob.glob('./*dat')
diffs = [item for item in dats if "diff" in item]
sums = [item for item in dats if "sum" in item]
avgs = [item for item in dats if "diff" not in item]
spfs = [item for item in dats if "spf" in item]


low = [item for item in diffs if "3C" in item]
med = [item for item in diffs if "11C" in item]
high = [item for item in diffs if "19C" in item]

pc0s = [item for item in dats if "PC0" in item]


subselection = ["-10.1us", "562ns", "750ns", "1us", "1.33us", "1.78us", "2.37us", "3.16us", "4.22us", "5.62us"]



DATAA = []
labels = []
ii = -1
for item in spfs:
    # for sub in subselection:
        # if sub in item:
    # d1, samp, temp, dtype,d5,d6,d7 = item.split('_')
    # labels.append(temp)
    if ii < 0:
        ii=0
        nii = ii
    else:
        N = plt.cm.inferno.N
        ii += int(N/len(subselection))
        nii = N-ii    
    data = pd.read_table(item,skiprows=1,names=['q','SA','sigSA'],delim_whitespace=True,engine='python')
    DATAA.append(data)
    labels.append(item)
#             plt.plot(data.q,data.I,label=item.split('_')[-1].replace('.dat',''),color=plt.cm.inferno(nii))
# plt.legend()
# plt.xscale('log')
# plt.show()

real_space_plotter(DATAA, name='output', labels=labels)
