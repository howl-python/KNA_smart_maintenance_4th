import numpy as np
import pandas as pd
F = 'Data/12_metro_compressor.csv'
# Pandas
# - 표 형태의 데이터를 잘 다루기 위해
# - Series
# - DataFrame :  series 가 모여서  합쳐진것 , 표구조 (df)

# 앞 단원 형식  -> 숫자 열만 골라야함 
# pandas 방식 -> 글자열까지 그대로 , 열은 이름으로

# df = pd.read_csv(F)
# print("데이터크기:", df.shape)
# print(df.head)

#실습 1
t = pd.read_csv(F)
