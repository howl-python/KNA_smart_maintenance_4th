import pandas as pd

F_SHOT = 'data/13_diecasting_shot.csv'

log = pd.read_csv(F_SHOT)
#실습 3
log_first = log.iloc[:100].reset_index(drop=True)
log_second = log.iloc[100:].reset_index(drop=True)

log_concat = pd.concat([log_first, log_second])
print("합친 모양:", log_concat.shape)

print((log_concat.index == 0).sum())

log_concat_fixed = pd.concat([log_first, log_second], ignore_index=True)

print("마지막 인덱스 번호:", log_concat_fixed.index[-1])

# print(df.shape)

# # 배열에서 하던 것
# arr = df["비스킷두께"].values
# print("배열에서 조건 참 개수:", int((arr >= 16).sum()))  # 74

# # 표에서 하는 것
# print("표에서 조건 참 개수:", int((df["비스킷두께"] >= 16).sum()))

# # 조건 -> boolean Series
# s = df["비스킷두께"] >= 16
# print(s.head(3).tolist())      # [False, False, False]

# print(int((df["비스킷두께"].isna()).sum()))
# print(int((df["비스킷두께"] < 16).sum()))    # 200- 74 = 112

# 복합 조건
# both = df[(df["비스킷두께"] >= 16) & (df["사이클타임"] >= 25)]
# either = df[(df["비스킷두께"] >= 16) | (df["사이클타임"] >= 25)]
# print(len(both), len(either))

# # 부정 조건 : %, ㅣ 
# print(len(df[df["품질등급"] == "불량"]))

# #isin : 값이 포함되어 있는지
# print(len(df[df["품질등급"].isin(["주의", "불량"])]))

# # between : 사이를 의미(양쪽 경계 모두 포함)
# print(len(df[df["비스킷두께"].between(10, 16)]))

# #문자열 조건 
# # - 숫자열에서는 쓸수없음
# # - str .contains : 해당문자열을 포함하는값
# print(len(df[df["설비ID"].str.contains("A")]))

# # - str.split, str.replace, str.strip ..
# print(df["설비ID"].head(1).tolist())   # ['DIE-A-01']
# print(df["설비ID"].str.split("-").head(1).tolist())

#  실습 1
# print("전체 데이터 크기:", df.shape)
# cond1 = df['비스킷두께'] >= 16
# print("조건 True 개수:", cond1.sum())
# df_2 = df[cond1]
# print("추출된 행 개수:", len(df_2))

# cond2 = df['비스킷두께'] < 16
# print("16 미만 개수:", cond2.sum())

# print("합계 확인:", cond1.sum() + cond2.sum())

# # 실습 2
# print("전체 데이터 크기:", df.shape)

# con = (df['비스킷두께'] >= 16) & (df['사이클타임'] >= 25)
# con2 = (df['비스킷두께'] >= 16) | (df['사이클타임'] >= 25)

# print("& 결과:", con.sum())
# print("| 결과:", con2.sum())

# con3 = df['품질등급'] == '불량'
# print("불량이 아닌 행:", (~con3).sum())

# #실습 3
# quailty = df['품질등급'].isin(['주의', '불량'])
# cc = df['설비ID'].str.contains('A')
# cc2 = df['설비ID'] == 'DIE-A-01'
# print(len(df[df["비스킷두께"].between(10, 16)]))
# print("전체 데이터 크기:", df.shape)
# print("조건 True 개수:", cc2.sum())
# print("A 포함 개수:", cc.sum())
# print("주의 또는 불량 개수:", quailty.sum())
# print(df['설비ID'].unique())

# 정렬, 
# 정렬 - sort_values
# - 기본값은 작은 값부터인 오름차순
# - 한 열로 정렬해도 모든 열이 행 단위로 함께 이동한다
# asc = df.sort_values("비스킷두께")
# print(asc["비스킷두께"].head(3).tolist())          # [2.0, 2.0, 4.0]

# # 다중키 정렬, 내림차순 
# # 다중 키 정렬, 내림 차순
# dec = df.sort_values("사이클타임", ascending=False)
# print(dec["사이클타임"].head(3).tolist()) #[6170.0, 652.3, 125.9]

# #다중키 정렬 
# two = df.sort_values(["품질등급", "비스킷두께"], ascending=[True, False])
# print(two["샷"].head(3).tolist())

# # copy
# x = df[df["품질등급"] == "불량"].copy()
# print(x.shape)       # (20, 8)
# x["위험등급"] = "높음"
# print(x.shape )       # (20, 9)

#실습 3
# quality = df['품질등급'].isin(['주의', '불량'])
# print(quality.sum())
# print("검사:", len(df[df['비스킷두께'].between(10, 16)]))
# cc = df['설비ID'].str.contains('A')
# print("글자:", cc.sum())
# cc2 = df['설비ID'] == 'DIE-A-01'
# print("일치:", cc2.sum())

#실습 4
# print("전체 데이터 크기:", df.shape)
# thc = df.sort_values("비스킷두께", ascending=False)
# print(thc["비스킷두께"].head(5).tolist())
# t = df.sort_values(["품질등급", "사이클타임"], ascending=[True, False])
# print(t.head(5))

# 실습 5
# print (df.head())
# qual = (df['비스킷두께'] >= 16)
# print(qual)
# big = df[qual].sort_values("비스킷두께", ascending=False)
# print(big.head(5))
# thre = df[qual].sort_values(["품질등급", "비스킷두께"], ascending=[True, False])
# print(thre["샷"].head(3).tolist())
# print(thre.head(5))
# good = df[df['품질등급'] != '양품']
# # print(good['비스킷두께'].isna().sum())