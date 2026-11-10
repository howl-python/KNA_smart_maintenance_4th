import pandas as pd

F_SMALL = 'data/13_diecasting_small.csv'
F_SHOT = 'data/13_diecasting_shot.csv'
dd = pd.read_csv(F_SHOT)
# 열 골라내기
# - 열 이름
# 단일 열 선택
# - df["실린더압력"]
df = pd.read_csv(F_SMALL)
# print("이름으로 앞 3개:", df["실린더압력"].head(3).tolist())  # [214.0, 217.0, 215.0]
# print(df["실린더압력"])
# # 214.0
# # 217.0
# 215.0

# 복수열 선택 
# - 여러 열은 이름들을 리스트로 묶어서 넣는다
# - 결과값은 DataFrame
# print(df[["형체력", "실린더압력"]])

# 실습 1
# df = pd.read_csv(F_SMALL)
# print(df.head())
# print(type(df["형체력"]))
# print(df["형체력"].head(3))
# print(df[["형체력", "실린더압력"]])
# print(df[["형체력"]])

# 행 선택
# - 라벨과 위치 번호의 차이
# - 라벨: 그 행에 붙은 이름표 = 인덱스 값
# - 위치 번호: 맨 위에서부터 몇 번째인지, 항상 0부터
# sorted = df.sort_values("형체력", ascending=False)
# print("정렬 후 인덱스 앞 4개:", sorted.index[:4].tolist()) # 정렬 후 인덱스 앞 4개: [22, 17, 27, 12]
# print("정렬 후 iloc[0] 샷:", int(sorted.iloc[0]['샷'])) # 정렬 후 iloc[0] 샷: 23
# print("정렬 후 loc[0] 샷:", int(sorted.loc[0, '샷'])) # 정렬 후 loc[0] 샷: 1

# 행, 열 동시 선택
# df.loc[행,열] - 열이름 사용O / df.iloc[행,열] - 열이름 사용X -> 숫자로 접근
# print(df.loc[0:4, ['실린더압력', '형체력']].shape)
# print(df.iloc[0:5, [2, 6]]).shape

#실습 2
# df = pd.read_csv(F_SMALL)
# print(" 원본 데이터")
# print(df.head())
# print("② 정렬 전 샷 번호")
# print(df.loc[0, "샷"])
# print(" 형체력 내림차순 정렬")
# sort_values = df.sort_values("형체력", ascending=False)
# print(sort_values)
# print(" 정렬 후 샷 번호")
#  
# print(sort_values.iloc[0]["샷"])

#실습 3
# df = pd.read_csv(F_SMALL)
# print(df.head())
# print(df.loc[0:4, ['실린더압력', '형체력']].shape)
# print(df.iloc[0:5, [2, 6]].shape)

#실습 4
dd = pd.read_csv(F_SHOT)
print("전체 데이터 크기:", dd.shape)
print(dd.loc[0:9 , ['설비ID', '비스킷두께']].shape)
print(dd.iloc[0:10, [1, 5]].shape)