import pandas as pd
F = 'data/14_hydraulic.csv'
F_QC = 'data/14_hydraulic_qc.csv'
df = pd.read_csv(F)
qc = pd.read_csv(F_QC)

# 그룹 통계와 상관관계
# - 그룹 통계 -> 원본 행과 그룹 기준 비교 -> 두 기준 표 -> 상관관계

'print(round(df["온도"].mean(), 2))'
'print(round(df["온도"].std(), 2))'

# print(df.groupby("냉각기상태")["온도"].mean().round(2))
# # 냉각기상태
# # 고장    54.67
# # 저하    45.46
# # 정상    35.89
# print(df.groupby("냉각기상태")["온도"].std().round(2))
# 냉각기상태
# 고장    3.76
# 저하    1.47
# 정상    0.36

# 분산 / 표준편차
# v = df.groupby("냉각기상태")["온도"].var()
# std = df.groupby("냉각기상태")["온도"].std()
# print(v.round(2))
# 냉각기상태
# 고장    3.76
# 저하    1.47
# 정상    0.36
# print((std **2).round(2))
# 냉각기상태
# 고장    14.13
# 저하     2.15
# 정상     0.13

# agg - 여러 통계 한번에 표로 모으기
# ㄴ 리스트 : 같은대상에 여러 통계
# ㄴ 딕셔너리 : 여러 통계
# ㄴ named aggregation: 결과 열의 이름까지 지정

# print(df.groupby("냉각기상태")["온도"].agg(["mean", "std", "max"]).round(2))
# print(df.groupby("냉각기상태")[["온도", "진동"]].agg(["mean", "std", "max"]).round(2))


#이름붙이기
# summary = df.groupby("냉각기상태").agg(
#     평균온도=("온도", "mean"),
#     평균진동=("진동", "mean")
# )
# print(summary.round(2))
# transform - 그룹 통계를 원래 행에 붙이기
# - 원래 행 인덱스와 모양을 유지한다


# # 열별로 다른 통계 목록 지정
# summary2 = df.groupby("냉각기상태").agg({
#     "온도": ["mean", "std"],
#     "진동": ["mean", "max"]
# })
# print(summary2.round(2))

#실습 1
# test = qc.groupby("검사결과").agg(
#     평균온도=("온도", "mean"),
#     평균냉각=("냉각효율", "mean"))
# print(qc.groupby("검사결과")[["온도"]].agg(["mean", "std", "max"]).round(2))
# test = qc.groupby("검사결과").agg(평균온도=("온도", "mean"), 평균냉각=("냉각효율", "mean"),측정수=("온도", "count")
# )
# print(test) # 높은온도 냉각효율이 매우떨어짐
# 항목	        불합격	합격
# 평균온도	    55.84	35.91
# 평균냉각효율	19.65	46.88
# 측정수	        12	188


# 같은 그룹의 평균 붙이기
# print(df.groupby("냉각기상태")["온도"].mean().shape) #(3,)
# print(df.groupby("냉각기상태")["온도"].transform('mean').shape) #(120,)

# marked = df.copy()
# marked["그룹평균"] = marked.groupby("냉각기상태")["온도"].transform("mean")
# marked["편차"] = marked["온도"] - marked["그룹평균"]
# print(marked[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))
# #   냉각기상태    온도   그룹평균     편차
# # 0    고장  35.6  54.67 -19.07
# # 1    고장  47.5  54.67  -7.17
# # 2    고장  50.7  54.67  -3.97

# # pivo_talbe - 두 기준 표를 한번에 봄
# # margins = True - 전체 집계 추가
# # 값이 없는 조합의 평균을 0으로 메우지않도록함 

# temp_table = pd.pivot_table(
#     df, index='밸브상태', columns='운전부하', values='온도', aggfunc='mean', 
#     margins=True, margins_name='전체'
# )
# print(temp_table.round(2))

#실습 2
# copr = df.copy()
# copr["그룹평균"] = copr.groupby("냉각기상태")["온도"].transform("mean")
# copr["편차"] = copr["온도"] - copr["그룹평균"]

# print(copr[["냉각기상태", "온도", "그룹평균", "편차"]].head(3).round(2))

# print(copr[["냉각기상태", "온도", "그룹평균", "편차"]].round(2))
# max_diff = copr["편차"].abs().max()
# result = copr[copr["편차"].abs() == max_diff]
# print(result)
# temp = pd.pivot_table(
#     df,index="밸브상태",columns="운전부하",values="온도",aggfunc="mean",
#     margins=True,
#     margins_name="전체"
# )
# print(temp.round(2))
# print("행 , 열:", temp.shape)
# # - values: 요약 계산을 적용할 열
# # - aggfunc: 그 측정값으로 요약
# # - margins=True: 전체 집계 행.열 추가
# # - margins_name: 추가 집계 이름 표시

# print(temp.round(2))

# # corr - 두 지표의 상관계수 구하기
# print(round(df["온도"].corr(df["진동"]), 3))  #0.931
# print(round(df["온도"].corr(df["냉각효율"]), 3))  #-0.951
# print(round(df["온도"].corr(df["압력"]), 3))    #0.284

# 실습 3
# print(df["온도"].corr(df["진동"]))
# print(df["온도"].corr(df["압력"]))
# print(df["온도"].corr(df["냉각효율"]))
# print(df[["온도", "냉각효율", "압력", "진동"]].corr().round(3))
# 4번
# 가장 강한 관계: 온도 - 냉각효율 (-0.951)
# 가장 약한 관계: 냉각효율 - 압력 (-0.131)

# 실습 4
# t = qc[['온도', '진동', '압력', '냉각효율', '유량', '모터전력',
#         '효율지수', '보조압력', '냉각출력', '배유온도'
# ]].corr().round(10)

# print(t)
# print(t.stack())
# pairs = []
# cols = ['온도', '진동', '압력', '냉각효율', '유량', '모터전력',
#         '효율지수', '보조압력', '냉각출력', '배유온도']
# for i in range(len(cols)):
#     for j in range(i + 1, len(cols)):
#         a = cols[i]
#         b = cols[j]
#         r = t.loc[a, b]
#         pairs.append([a, b, r])

# pair_table = pd.DataFrame(pairs)
# print(pair_table)
# print(len(pair_table))
# print((pair_table[2].abs() >= 0.4).sum())
# print((pair_table[2].abs() >= 0.95).sum())
# print(pair_table[(pair_table[2].abs() >= 0.95)])
# strong = pair_table[pair_table[2].abs() >= 0.95]
# print(strong.sort_values(by=2, key=abs, ascending=False).head(5))

# 실습 5

# 1. 데이터 불러오기
cycle = pd.read_csv("data/14_hydraulic.csv")
spec = pd.read_csv("data/14_hydraulic_std.csv")

print(cycle.shape, spec.shape)  # (120, 8) (4, 5)


# 2. 냉각기상태를 기준으로 병합하고 확인하기
print("기준표 중복 키:", spec["냉각기상태"].duplicated().sum())  # 0

joined = cycle.merge(
    spec,
    on="냉각기상태",
    how="left",
    validate="many_to_one"
)

print(len(cycle), len(joined), joined.shape)  # 120 120 (120, 12)

added_cols = ["상태설명", "권장점검주기", "담당팀", "위험도"]
print(joined[added_cols].isna().sum())  # 네 열 모두 0

work = joined.copy()


# 3. 온도 구간 만들기
# 낮음: 0 초과 ~ 40 이하
# 보통: 40 초과 ~ 50 이하
# 높음: 50 초과 ~ 200 이하
work["온도구간"] = pd.cut(
    work["온도"],
    bins=[0, 40, 50, 200],
    labels=["낮음", "보통", "높음"],
    right=True
)

print(work["온도구간"].value_counts(sort=False))  # 41 / 40 / 39
print("온도 구간 미지정:", work["온도구간"].isna().sum())  # 0


# 4. 냉각기 상태별 진단표 만들기
diagnosis = work.groupby("냉각기상태").agg(
    측정수=("온도", "size"),
    평균온도=("온도", "mean"),
    온도표준편차=("온도", "std"),
    평균냉각효율=("냉각효율", "mean"),
    위험도=("위험도", "max"),
    점검주기=("권장점검주기", "max"),
)

print(diagnosis.round(2))
print(diagnosis.shape, diagnosis["측정수"].sum())  # (3, 6) 120


# 5. 냉각기 상태와 온도 구간의 교차표 확인하기
print(pd.crosstab(work["냉각기상태"], work["온도구간"]))

# 온도구간   낮음  보통  높음
# 냉각기상태
# 고장        1     1    38
# 저하        0    39     1
# 정상       40     0     0


# 6. 온도와 다른 지표의 상관계수 계산하기
print(round(work["온도"].corr(work["냉각효율"]), 3))  # -0.951
print(round(work["온도"].corr(work["진동"]), 3))      # 0.931


# 7. 위험도와 평균온도를 기준으로 내림차순 정렬하기
# 위험도와 점검주기는 교육용 기준표의 값입니다.
priority = diagnosis.sort_values(
    ["위험도", "평균온도"],
    ascending=[False, False]
)

print(priority.round(2))


# 8. 발견·해석·행동 작성하기
print("\n[발견]")
print("냉각기 고장 라벨 40건의 평균 온도는 54.67도, 표준편차는 3.76도이다.")
print("38건은 50도 초과이며, 온도-냉각효율 상관은 -0.951이다.")

print("\n[해석]")
print("이 자료에서는 고장 라벨 그룹의 온도 수준과 흩어짐이 더 크다.")
print("운전 조건과 라벨 정의가 충분하지 않아 원인과 실제 위험도를 단정하지 않는다.")

print("\n[행동]")
print("교육용 기준표로는 고장 그룹을 우선 검토 대상으로 정렬한다.")
print("실제 점검 전 현장 기준을 확인하고, 고장 라벨의 35.6도 행은 원자료를 확인한다.")
