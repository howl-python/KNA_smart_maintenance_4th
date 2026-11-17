import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df =pd.read_csv(F_PROC)
dd =pd.read_csv(F_LOG)

#dropna : 행 삭제 , 열삭제
# axis : 제거할 축을 선택 , axis = 1 > 열 전체가 빠지게 됨
# rows_removed = df.dropna()
# cols_removed = df.dropna(axis=1)
# print(rows_removed.shape)  # (76, 22)
# print(cols_removed.shape)  # (250, 10)
# print(df.shape)  # (250, 22)

# - how: 하나라도 비면('any'), 전부 비면('all')

# print(df.dropna(how='any').shape)
# print(df.dropna(how='all').shape)

# # - thresh: 유효값 최소 개수 지정
# print(df.dropna(thresh=20).shape) #(162, 22)

# #subset : 중요한 열만 검사
# # ㄴ 다른열의 결측이 남아있어도 지정한 조건을 충족하면 유지한다
# print(df.dropna(subset=['배럴온도']).shape)

#실습 1
# df.shape
# rows_del = df.dropna()
# cols_del = df.dropna(axis=1)
# print(rows_del.shape) 
# print(cols_del.shape)
# print(df.shape)

# #실습 2
# df.shape
# row_missing = (df.dropna())
# print(df.dropna(how='any').shape)
# print(df.dropna(how='all').shape)
# print(df.dropna(thresh=20).shape)
# print(df.dropna(subset=['불량여부']).shape)

#실습 3
feature_cols = list(df.columns[3:])
print(len(feature_cols))

rate = df[feature_cols].isna().sum() / len(df) * 100
print(rate[rate >= 40])
remove_cols = list(rate[rate >= 40].index)
print(remove_cols)
clean_df = df.drop(columns=remove_cols)
print(clean_df.shape)
print(clean_df.columns)