import pandas as pd
FF = 'data/14_hydraulic_qc.csv'
F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'
df = pd.read_csv(F)
qc = pd.read_csv(F_QC)
qd = pd.read_csv(FF)
# 빈도와 그룹 집계
# - 값별로 세기와 그룹별로 집계하기


# print(df.shape, qc.shape)

# # 1. 빈도
# # - value_counts
# # - pd.cut
# print(df['냉각기상태'].value_counts())
# # 냉각기상태
# # 고장    40
# # 저하    40
# # 정상    40
# # Name: count, dtype: int64

# print(df['밸브상태'].value_counts())
# # 밸브상태
# # 정상    61
# # 지연    20
# # 경미    20
# # 심각    19

# # 개수 -> 비율 : normalize
# counts = df["result"].value_counts()
# ratios = df["result"].value_counts(normalize=True)
# print(counts)           #정상    67   고장    53
# print(ratios.round(3))
# print((ratios * 100).round(1))      #정상    55.8  고장 44.2

# 실습 1
# print("전체 데이터 크기:", df.shape)
# print(df['밸브상태'].value_counts())
# print(df['운전부하'].value_counts())
# cc = df["밸브상태"].value_counts(normalize=True)
# cq = df["운전부하"].value_counts(normalize=True)
# print(cc.round(3))
# print((cc * 100).round(1))
# print(cq.round(3))
# print((cq * 100).round(1))
# ct = df["밸브상태"].value_counts()
# print(ct.max())

# ct = df["밸브상태"].value_counts()
# print(ct.min())

# ct2 = df["운전부하"].value_counts()
# print(ct2.min())

# ct2 = df["운전부하"].value_counts()
# print(ct2.max())

# max_items = ct[ct == ct.max()]
# print(max_items)

# max_items2 = ct2[ct2 == ct2.max()]
# print(max_items2)

# min_items = ct[ct == ct.min()]
# min_items2 = ct2[ct2 == ct2.min()]
# print(min_items)
# print(min_items2)

# pd.cut
# band = pd.cut(df["온도"], bins=[0, 40, 50, 200], labels=['낮음', '보통', '높음'], right=True)
# print(band.value_count(sort=False))

#실습 2 
# ct = qd["검사결과"].value_counts()
# print("[건수]")
# print(ct)
# ratios = qd["검사결과"].value_counts(normalize=True).round(3)
# print("[비율]")
# print(ratios)
# print("[백분율]")
# print((ratios * 100).round(1))

#실습 3
# vib = df["진동"].value_counts()
# max_items = vib[vib == vib.max()]
# print(max_items)
# min_items = vib[vib == vib.min()]
# print(min_items)
# band = pd.cut(df["진동"], bins=[0, 0.6, 0.7, 10], labels=['약함', '보통', '강함'], right=True)
# # band = pd.cut(df["진동"], bins=[0, 0.62, 0.7, 10], labels=['약함', '보통', '강함'], right=True)
# print("최솟값:", df["진동"].min())
# print("최댓값:", df["진동"].max())
# print("미지정:", band.isna().sum())

# # 그룹 집계
# # - 분할 -> 적용 -> 결합 구조
# # - groupby

# means = df.groupby("냉각기상태")["온도"].mean()
# print(means.round(2))
# # 고장    54.67
# # 저하    45.46
# # 정상    35.89
# print('--------------------------------')
# print(df.groupby('냉각기상태')['온도'].max())
# # 고장    57.8
# # 저하    51.2
# # 정상    36.4

# keys = ['냉각기상태', '운전부하']
# print(df.groupby(keys)['온도'].mean().round(2))
# # 고장     고부하     55.51
# #        저부하     54.05
# # 저하     고부하     44.07
# #        저부하     45.58
# # 정상     고부하     35.89

# #crosstab
# print(pd.crosstab(df['냉각기상태'], df['운전부하']))

# 실습 4
# df = pd.read_csv(F)
# means = df.groupby("냉각기상태")["온도"].mean()
# print(df)
# print(means.round(2))
# print(df["냉각기상태"].value_counts())
# print(means.min())
# print(means.max())
# print(df.groupby('냉각기상태')['온도'].max())
# print(round(means.max() - means.min(), 2))

# 실습 5
# tt = df["밸브상태"].value_counts()
# print(tt)

# warning = df[df["result"] == "고장"]
# print(warning)

# tf = warning["밸브상태"].value_counts()
# print(tf)

# ratio = tf / tt
# print(ratio.round(3))
# print(ratio.max())
total = df['밸브상태'].value_counts()

broken = df[df['result'] == '고장']
broken_counts = broken.groupby('밸브상태').size()

total = df['밸브상태'].value_counts()

broken_counts = broken_counts.reindex(total.index, fill_value=0)

ratios = broken_counts / total
print(ratios.sort_values(ascending=False).round(3))