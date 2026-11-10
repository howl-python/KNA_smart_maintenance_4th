import pandas as pd
import numpy as np
F = 'Data/12_metro_compressor.csv'
FD = 'data/12_metro_digital.csv'
FF = 'Data/12_metro_compressor_semicolon.csv'
F4 = 'Data/12_metro_small.csv'
df = pd.read_csv(F)
df2 = pd.read_csv(FD)
df3 = pd.read_csv(FF)
df4 = pd.read_csv(F4)
# 데이터 미리보기 및 구조 파악

# # 1) 앞부분 미리보기
# - df.head() > 위에서 5줄 숫자 지정가능
# print(df.head()) 
# 2) 뒷부분 미리보기
# - df tail)() > 밑에서 5줄 숫자 지정가능
# print(df.tail())  

# 3) 열 이름 목록
# - df.shape
# print(df.shape)

# # 4) 열 이름 목록
# # - df.columns
# # - df.columns.tolist( ) > 목록으로 보기쉽게
# print(df.columns.tolist())
# # ㄴ 여기서 나오는 값으로 특정 열의 데이터값 추출

# # 5) 행번호표
# # - df.index
# print(df.index)
# # ㄴ 0부터 시작해서 199 까지 1씩 증가

# # 6) 열별 자료형
# # - df.dtypes
# print(df.dtypes)
# print("---------------------------")
# print(pd.read_csv(FD).dtypes)
# # 측정시각       str
# # 압축기         int64
# # 타워         int64
# # 저압스위치     int64
# # dtype: object
# df2 = pd.read_csv(FD, dtype={"압축기": str})

# 7) 전체구조
# - df.info()
# print(df.info())
# <class 'pandas.DataFrame'>
# RangeIndex: 200 entries, 0 to 199       > 200행
# Data columns (total 7 columns):          > 7열
# #   Column      Non-Null Count  Dtype
# ---  ------      --------------  -----
# 0   측정시각    200 non-null    str
# 1   압축압력    200 non-null    float64
# 2   배출압력    200 non-null    float64
# 3   저장압력    200 non-null    float64
# 4   오일온도    199 non-null    float64
# 5   모터전류    200 non-null    float64
# 6   가동상태    200 non-null    str
# dtypes: float64(5), str(2)
# memory usage: 11.1 KB
# None
# 기초 통계 요약
# - 숫자 열들의 평균/최대/최소 등을 한번에 자동 계산. 글자 열은 자동으로 빠짐
# print(df.describe().round(2))

# #특정 조건에서의 통계 필요시
# state = df["가동상태"].values
# cur = df["모터전류"].values
# print(round(float(np.mean(cur[state == "가동"])),2))

# 실습 1
# print(df.head)
# print(df.head1(3))
# print(df.tail)
# print(df.tail(10))
# print(df.head())

# 실습 2
# df2 = pd.read_csv('data/12_metro_digital.csv')
# print(df2.shape)  # 120 4
# print(df2.dtypes)
# print(df2.columns.tolist()) #['측정시각', '압축기', '타워', '저압스위치']
# print(df2.head()) # 이표는 압축기 설비의 데이터 전체 크기는 120행 4열 0과 1로 이루어져있음  
# 측정시각     str
#압축기      int64
# 타워       int64
# 저압스위치    int64

#실습 3
# print(df.info())
# missing = 200 - 199
# print(missing)

#실습 4
# print(df.describe())
# print(df.dtypes)
# current = df["모터전류"]
# status = df["가동상태"]
# print(current[status == "가동"].mean())
# print(current[status == "정지"].mean())

# print(current.mean())
# print(current.median())

# 실습 5
# df = pd.read_csv(F)
# df2 = pd.read_csv(FD)
# print(df.shape)
# print(df2.shape)

# print(df.dtypes)
# print(df2.dtypes)

# df.info()
# df2.info()
# print(np.unique(df2["압축기"]))
# print(np.unique(df2["타워"]))
# print(np.unique(df2["저압스위치"]))

#실습 6
df4 = pd.read_csv(F4)
print(df4.head())

print(df4.shape)
df4.info()

null_counts = 30 - df4.count()
print(null_counts)

print(df4.describe())

mean_current = round(df4["모터전류"].mean(), 2)
median_current = round(df4["모터전류"].median(), 2)
print("모터전류 평균:", mean_current)
print("모터전류 중앙값:", median_current)