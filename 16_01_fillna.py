import pandas as pd

# 실습 1
F_F = 'data/16_diecasting.csv'

qq = pd.read_csv(F_F)

# print(qq.head())
# print(qq.shape)
# print(qq.columns)
# qq.info()

# 실습 2
# print(qq.columns)
# print(qq["실린더압력"].min(), qq["실린더압력"].max())
# print(qq["실린더압력"].max() - qq["실린더압력"].min())

# 실습 3
# print(qq.sort_values(by='사이클타임', ascending=False).head(5))
# print(qq[qq["사이클타임"] > 35])

# print(qq[(qq["사이클타임"] >= 20) & (qq["사이클타임"] <= 35)])
# print("-------------------------------")
# print(qq[qq["사이클타임"] > 35].sort_values("사이클타임", ascending=False).head(10))

# 실습 4
# print(qq["사이클타임"].mean())
# print('--------------------------')
# print(qq["사이클타임"].median())
# print(qq[qq["상태"] == 0]["사이클타임"].mean())

# 실습 5
# print(qq["실린더압력"].quantile(0.25))
# print(qq["실린더압력"].quantile(0.50))
# print(qq["실린더압력"].quantile(0.75))

#실습 6
# summary = qq.describe()
# print(summary)
# print(summary.columns)
# print(summary.loc["mean"])
# print( summary.loc["50%"])
# gap = summary.loc["mean"] - summary.loc["50%"]
# print('----------------------')
# print(gap)
# print(gap.abs().sort_values(ascending=False))

#실습 7
s = qq[["실린더압력", "사이클타임", "비스킷두께"]]
print(qq[['실린더압력','사이클타임','비스킷두께']].quantile(0.25))
print(qq[['실린더압력','사이클타임','비스킷두께']].quantile(0.50))
print(qq[['실린더압력','사이클타임','비스킷두께']].quantile(0.75))
print(s.quantile(0.75) - s.quantile(0.25))