import pandas as pd
F_SHOT = 'data/13_diecasting_shot.csv'
F_MASTER = 'data/13_diecasting_master.csv'

log = pd.read_csv(F_SHOT)
master = pd.read_csv(F_MASTER)

# print(log.shape)
# print(master.shape)

# three = log.head(3)[['샷', '설비ID', '비스킷두께']]
# print(three.to_string(index=False))

# print(three.merge(master, on='설비ID').to_string(index=False))
#  샷     설비ID  비스킷두께 라인  도입연도  정격형체력 담당반
#  1 DIE-A-01    10.0   A  2018    280  1반
#  2 DIE-B-01    11.0   B  2020    320  2반
#  3 DIE-B-01    11.0   B  2020    320  2반
# merge 기본 사용법
# - on: 두 표를 잇는 키 열
# - 행은 예측불가, 열수는 예측가능 

# - how: 어느쪽을 다 남길 것인가
#   - (기본) how='inner'
#   - how='left' : 왼쪽은 다 남기고 짝 없으면 빈 칸
#   - how='outer' : 양쪽 다 남김

# m_inner = log.merge(master, on ='설비ID')
# m_left = log.merge(master, on='설비ID', how='left')
# m_outer = log.merge(master, on='설비ID', how='outer')

# print(log.merge(master, on='설비ID', how='inner').shape, log.merge(master, on='설비ID', how='left').shape, log.merge(master, on='설비ID', how='outer').shape)

# 실습 1
# print("로그 크기:", log.shape)
# print("대장 크기:", master.shape)

# print("로그 컬럼:", log.columns.tolist())
# print("대장 컬럼:", master.columns.tolist())

# df_merged = pd.merge(log, master, on="설비ID", how="left")
# print("합친 표 크기:", df_merged.shape)

# print(df_merged.head(2))

# # 합치기 전후 점검 코드

# print(len(log))    # 200
# print(len(master), master["설비ID"].nunique())   # 5 5
# m_left = log.merge(master, on="설비ID", how="left")
# print(len(m_left))       # 200 
# print(m_left["라인"].isna().sum())   # 15 

# unmatched = m_left[m_left['라인'].isna()]
# print(unmatched['라인'].head(1).tolist(), len(unmatched))

# 실습 2

merged_inner = log.merge(master, on="설비ID", how="inner")
print(merged_inner.shape)

merged_left = log.merge(master, on="설비ID", how="left")
merged_outer = log.merge(master, on="설비ID", how="outer")

print(merged_left.shape)
print(merged_outer.shape)

print(merged_left[merged_left["라인"].isna()]["설비ID"].value_counts())
print(merged_outer[merged_outer["샷"].isna()]["설비ID"])