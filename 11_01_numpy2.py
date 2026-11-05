import numpy as np

F ='data/11_diecasting_series.csv'
# ct = np.genfromtxt(F, delimiter= ",", skip_header=1 , usecols= 1)
# print(ct.shape, ct.dtype)

# def col(c):
#     return np.genfromtxt(F, delimiter= ",", skip_header=1 , usecols= 1)

# 자리찾기
# fancy indexing : 여러 위치 한번에 추출 가능 (떨어진 자리도 한번에 가능)
# vib = np.array([2.1, 2.3, 2.0, 5.8])
# pick = np.array([0, 3])
# print(vib[pick]) # [2.1 5.8]

#정렬 과 정렬 순서

# sort, argsort() :원래 자리 번호 돌려줌
# print(np.sort(vib))
# print(np.argsort(vib))

#실습 1
import numpy as np

import numpy as np
f = np.loadtxt('data/11_diecasting_series.csv',
                delimiter=",",
                skiprows=1,
                usecols=(0, 1))

max_index = np.argmax(f[:, 1])
print( max_index)
print("번호:", f[max_index, 0])
print("사이클타임:", f[max_index, 1])