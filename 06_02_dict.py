# 딕셔너리
# 형식 : {키: 값, 키: 값} - 키는 문자열
# 리스트는 번호(인덱스)로 찾지만    딕셔너리는 이름(키)로 찾는다

# sensors = {"모터온도": 78, "진동": 0.5}
# print(sensors)
# print(sensors["모터온도"])
# print(type(sensors)) # class dict
# print(sensors["유량"]) # 없는 키를 조회하면 에러발생

#추가/ 수정 / 삭제
# 형식: 딕셔너리[키] = 값 (없는키 -추가  추가있는키 - 수정)
# 형식 : (삭제) del 딕셔너리[키]

# sensors["펌프압력"] = 95 # 추가
# sensors["모터온도"] = 80 #수정
# del sensors["진동"] # 삭제 없는키 삭제는 오류발생
# print(sensors) 

# # get / in 
# #형식: 딕셔너리.get(키 , 기본값) / 키 in 딕셔너리
# print(sensors.get("유량"))
# print(sensors.get("유량", 0))
# print("모터온도" in sensors)
# print(80 in sensors)

#실습 1
'''
sensors = {"온도": 78, "습도": 45}
print(sensors["온도"])
sensors["기압"] = 100  
sensors["습도"] = 50
print(sensors)
print(sensors.get("이산화탄소",0))
print("온도" in sensors)
'''

#keys / values / items /len
'''
sensors = {"모터온도": 78, "진동": 0.5}
print(list(sensors.keys())) # 모터온도 진동
print(list(sensors.values())) # 78 ,0.5
avg = sum(sensors.values()) / len(sensors) 
print(avg) # 평균값 39.25
# '''
# for name, value in sensors.items():
#     print(name, value)

#for k in sensors.keys()
#for v in sensors.values()
### 2. 키 in 딕셔너리

#기본 형식:** `키 in 딕셔너리`
#예시 코드:
# 재고 관리 예시
'''
inventory = {"사과": 10, "바나나": 5}
item = "포도"

if item in inventory:
  # 이미 존재한다면 기존 값 수정(update)
  inventory[item] += 3
  '''
# 실습 2
# sensors = {"온도": 70, "습도": 50}
# new_data = {"온도": 75, "압력": 90}
# sensors.update(new_data)
# print("new_data:", sensors)
# del sensors["습도"]
# print("센서수:", len(sensors))

#실습 3
# sensor_data = {"온도": 72, "습도": 63, "압력": 95}
# avg = sum(sensor_data.values()) / len(sensor_data)
# print("평균", avg)
# biggest = 0
# biggest_name = ""
# for name, value in sensor_data.items():
#     if value > biggest:
#         biggest = value
#         biggest_name = name

# print("최대값센서", biggest_name, biggest)

# zip : 센서명 - 값 매핑하기
# names = ["온도", "진동", "압력"]
# values = [78, 0.5, 95]
# sensors = dict(zip(names, values))
# print(sensors)       # {'온도': 78, '진동': 0.5, '압력': 95}

# 딕셔너리 값에 리스트 / 딕셔너리 - 중첩 딕셔너리
# plant = {
#     "1번모터": {"온도": 78, "상태": "정상"},
#     "2번펌프": {"압력": 95, "상태": "경고"}
# }

# print(plant["2번펌프"]["압력"])    # 95

#실습 4
# sensors = ['온도', '진동', '압력']
# values = [78, 0.5, 95]
# sensor_dict = dict(zip(sensors, values))
# print(sensor_dict)
# for name, value in sensor_dict.items():
#     print(name, value)

#실습 5
# check = {"온도": 78, "진동": 0.5, "압력": 95}
# limits = {"온도": 70, "진동": 0.8, "압력": 100}
# warning = []
# for name, value in check.items():
#   if value > limits[name]:
#     warning.append(name)
# print("경고 센서:", warning) 

#실습 6
# pumps = {
#     '1번모터': {'온도': 78, '상태': '정상'},
#     '2번펌프': {'압력': 95, '상태': '경고'}
# }
# print(pumps["2번펌프"]["압력"])
# for name, value in pumps.items():
#     if value["상태"] == "경고":
#         print(name, "점검 필요")

#실습 7
# reading = ["온도,78.0", "압력,95.0", "진동,0.5"]
# sensor_dict = {}
# for temp in reading:
#     name, value = temp.split(",")
#     sensor_dict[name] = float(value)
# print(sensor_dict)

#실습 8 
measure = {"온도": 90.0, "압력": 101.0}
limits = {"온도": 80.0, "압력": 100.0}
avg = sum(measure.values()) / len(measure)
print("평균",round(avg,1))
warning = set()
for name , value in measure.items():
    if value > limits[name]:
        warning.add(name)
print("위험센서:", sorted(warning))



    
