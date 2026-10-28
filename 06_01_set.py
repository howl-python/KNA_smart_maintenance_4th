#셋 - 중복 자동 제거 , 순서 없음
# 형식 : {값1, 값2} 또는set (리스트)
# 빈셋 set()
# logs = ["s01", "s02","s01" ,"s03"]
# unique_logs = set(logs)
# print(unique_logs) #{'s02', 's01', 's03'} #셋은 순서가 없어 인덱싱 불가
# print(sorted(unique_logs)) # ['s01', 's02', 's03']


# #add - 값 추가
# alerts = {"s01", "s02"}
# alerts.add("s03")
# print(alerts)
# alerts.add("s01")
# print(alerts)

#실습 4
# sensor = {"S01","S02", "S03", "S02"}
# s_sensor = set(sensor)
# print(sorted(s_sensor))
# print("종류 수:", len(s_sensor))

#집합 연산 -union(전체) / intersection(공통) / difference(차이)
# line_a = {"s01","s02", "s03"}
# line_b = {"s03","s04"}
# print(line_a.union(line_b))
# print(line_a.intersection(line_b))
# print(line_a.difference(line_b))

#실습 5
# line_a = {"S01", "S02", "S03","S05"}
# line_b = {"S03","S04","S05"}
# print(line_a.union(line_b))
# print(line_a.intersection(line_b))
# print(line_a.difference(line_b))
# print(line_b.difference(line_a))

#실습 6 
ysday = {'S01', 'S02', 'S03'}
today = {'S02', 'S03', 'S05'}
print(today.union(ysday))
print(today.intersection(ysday))
print(today.union(ysday))
print("지속 이상:", today.intersection(ysday))
print("신규 이상:", today.difference(ysday))

#