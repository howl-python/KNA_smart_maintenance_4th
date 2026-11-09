import numpy as np
import pandas as pd
F = 'Data/12_metro_compressor.csv'
FS = 'Data/12_metro_compressor_semicolon.csv'
# Pandas
# - 표 형태의 데이터를 잘 다루기 위해
# - Series
# - DataFrame :  series 가 모여서  합쳐진것 , 표구조 (df)

# 앞 단원 형식  -> 숫자 열만 골라야함 
# pandas 방식 -> 글자열까지 그대로 , 열은 이름으로

df = pd.read_csv(F)
# print("데이터크기:", df.shape)
# print(df.head)

#실습 1
# df = pd.read_csv(F)

# print(df.shape)
# # print(df.head())

# print(df.dtypes)

# state = df["가동상태"].values
# print("가동상태 종류 개수:", np.unique(state, return_counts = True))

# cur = df["모터전류"].values
# print("모터전류 평균 %.2f / 가운데값 %.2f" % (np.mean(cur), np.median(cur)))
# #모터전류 평균 2.06 / 가운데값 0.04

# s = df["오일온도"]
# print(s.head(3))

# #Pandas
# new = pd.read_csv(F, usecols=["오일온도", "모터전류"])
# print(new.shape)
# new = pd.read_csv(F, usecols=["오일온도", "모터전류"])
# print(new.shape)  # (200, 2)
# #행 수를 제한하는 설정
# print(pd.read_csv(F, nrows=10).shape)  # (10, 7)
# read_csv 옵션
# - usecols, nrows, encoding, sep(구분자)

# 실습 2
# df = pd.read_csv(F, usecols=["측정시각", "오일온도", "모터전류"])
# print(df)
# print(pd.read_csv(F , nrows= 20).shape)
# print("--------------------------")
# df = pd.read_csv(F, usecols=[0, 4, 5])

# 실습 3
# df = pd.read_csv(F)

# print(df.shape)
# print(df.head())

# df = pd.read_csv(F, sep=';', encoding='utf-8')

# print(df.shape)
# print(df.head())

#
# 실습 4
dt = pd.read_csv(FS,sep=";",encoding="utf-8",usecols=[2, 3, 4],nrows=50)
print(dt.shape)
print(dt.head())