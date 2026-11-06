import numpy as np

F ='data/11_diecasting_series.csv'
def col(c):
    return np.genfromtxt(F, delimiter=",", skip_header=1, usecols=c)
# f = np.loadtxt('data/11_diecasting_series.csv',
#                 delimiter=",",
#                 skiprows=1,
#                 usecols=(0, 1))

# max_index = np.argmax(f[:, 1])
# print( max_index)
# print("번호:", f[max_index, 0])
# print("사이클타임:", f[max_index, 1])

# diff
# vib = np.array([2.0, 2.1, 2.2, 7.0, 7.1])
# change = np.diff(vib)

# print(np.round(change, 1))
# print(np.argmax(change))

#실습 2
# t = np.loadtxt('data/11_diecasting_series.csv',
#                 delimiter=",",
#                 skiprows=1,
#                 usecols=(0, 1))
# cyc = t[:, 0]
# ct = t[:, 1]
# diff = np.diff(ct)
# change = np.abs(diff)
# idx = np.argmax(change)
# print(idx)
# print(cyc[idx] , cyc[idx+1] , change[idx])

# cumsum = 누적 합
# defects = np.array([0, 1, 2, 3, 4, 5])
# print(np.cumsum(defects))

#np.where 심화
# vib = np.array([2.1, 3.5, 2.0, 6.2])
# label = np.where(vib >= 5, 2, np.where(vib >= 3, 1, 0))   # 5 이상: 2, 3 이상: 1, 나머지: 0
# print(label)

#  unique - 중복 정리
#  - return_counts 옵션: 각 종류의 개수 확인
# status = np.array([0, 0, 1, 0, 2, 1, 0])
# kinds, counts = np.unique(status, return_counts=True)
# print(kinds)
# print(counts)

# 실습 3
# t = np.loadtxt('data/11_diecasting_series.csv',
#                 delimiter=",",
#                 skiprows=1,
#                 usecols=(2,))
# cyl = t
# cyl[0] = 9999
# mean_before = np.mean(cyl)
# print("보정 전 평균:", round(mean_before, 1))
# fixed = np.clip(cyl, 100, 300)
# mean_after = np.mean(fixed)
# print("보정 후 평균:", round(mean_after, 1))

#실습 4
# t = np.loadtxt('data/11_diecasting_series.csv',
                # delimiter=",",
                # skiprows=1,
                # usecols=(1,))

# ct = t

# state = np.where(ct >= 1000, 2,
#          np.where(ct >= 50, 1, 0))

# normal = (state == 0).sum()
# warning = (state == 1).sum()
# jam = (state == 2).sum()

# print("정상:", normal, round(normal / 50, 2))
# print("경고:", warning, round(warning / 50, 2))
# print("잼:", jam, round(jam / 50, 2))


#실습 5
# ct = col(2,)
# cyl = col(2,)
# ju = col(2,)
# box = col(2,)
# M = np.stack([ct, cyl, ju, box])
# print("전체:", M.shape)

# recent = M[:, -10:]
# print("잘라냄:", recent.shape)

# 실습 6 
time = col(0,)
ct = col(1,)
cypres = col(2,)
M = np.stack([time, ct, cypres])
max_ct = np.argmax(ct)
print(max_ct)
print(time[max_ct], ct[max_ct])
change = np.abs(np.diff(ct))
j = np.argmax(change)
warning = (ct >= 50) | (cypres < 150)

print(warning.sum())

ratio = warning.sum() / ct.size

print(round(ratio, 2))

print(time[j], time[j+1], round(change[j], 1))
order = np.argsort(ct)
top3 = order[-3:][::-1]
print(ct[top3])
print(time[top3])