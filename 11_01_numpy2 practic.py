import numpy as np

F ='data/11_diecasting_series.csv'
# f = np.loadtxt('data/11_diecasting_series.csv',
#                 delimiter=",",
#                 skiprows=1,
#                 usecols=(0, 1))

# max_index = np.argmax(f[:, 1])
# print( max_index)
# print("번호:", f[max_index, 0])
# print("사이클타임:", f[max_index, 1])

# diff
vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
change = np.diff(vib)

print(np.round(change, 1))
print(np.argmax(change))

#실습 2
t = np.loadtxt('data/11_diecasting_series.csv',
                delimiter=",",
                skiprows=1,
                usecols=(0, 1))
cyc = t[:, 0]
ct = t[:, 1]
diff = np.diff(ct)
change = np.abs(diff)
idx = np.argmax(change)
print(idx)
print(cyc[idx] , cyc[idx+1] , change[idx])