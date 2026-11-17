import pandas as pd

F_PROC = 'data/15_사출성형_공정.csv'
F_LOG = 'data/15_사출성형_로그.csv'

df =pd.read_csv(F_PROC)
dd =pd.read_csv(F_LOG)

# 결측 처리
# - 종류: NaN, None, NA, NaT
# ㄴ 표현은 달라도 isna()로 결측 여부 확인 가능

# s = pd.Series([10, None, 20])
# print(s.mean())         #Nan 값이 있다고 해서 계산이 멈춘다 X (10 + 20) / 2
# print(s +1 )  # 11.0,NaN, 21.0

# 실습 1
# print(dd.shape)
# count =pd.isna(dd)
# print(dd.isna().sum().sum())
# print((dd["사출압력"] == 0).sum())
# print((dd["스크루속도"] == -999).sum())
# print((dd["배럴온도"] == 999).sum())
# 측정시각     0
# 사출기       1
# 배럴온도     2
# 사출압력     1
# 스크루속도     1
# 누적샷       0
# 불량여부     0

# 실습 2
# print(df.shape)
# print(df.head(3))
# df.info()
# print(df["최대사출속도"].describe())

# 실습 3
# dd = pd.read_csv(F_LOG, na_values={
#     "배럴온도": [999],
#     "스크루속도": [-999],
#     "사출압력": [0]
# })

# print(dd.isna().sum().sum())
# print((pd.read_csv(F_LOG)["불량여부"] != dd["불량여부"]).sum())

#실습 4
# count = df.isna().sum()
# rate = count / len(df) * 100
# print(rate)
# print(rate[count > 0])
# summary = pd.DataFrame({
#     "결측개수": count,
#     "결측비율": rate
# })
# print(summary)
# print(summary[count > 0])

# 실습 5
# count = df.isna().sum()
# rate = count / len(df) * 100

# print(rate.sort_values(ascending=False).head(3))
# row_count = df.isna().sum(axis=1)
# print((row_count == 0).sum())  # 결측 없는 행
# print((row_count > 0).sum())   # 결측 있는 행
# print((row_count >= 5).sum())  # 결측 5개 이상인 행

# 실습 6

cols = ["최대사출속도", "감압시간"]
print(df[cols].isna().sum())
print(df[cols].isna().head(10))
a = df["최대사출속도"].isna()
b = df["감압시간"].isna()
print((a & b).sum() / len(df) * 100 )
print((a & b).sum())
print(df[a & b][['측정시각', '사출기']])
print((~a & ~b).sum())
print(((a & ~b) | (~a & b)).sum())