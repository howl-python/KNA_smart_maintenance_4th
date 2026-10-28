# 튜플
# 형식: (값, 값2, 값3,....)
# 좌표, (이름, 값) 처럼 짝지어진 값을 하나로 묶을떄
# sensor = ("모터온도", 78)
# print(sensor) #값이 한개라도 , 표시해야 튜플로 인지
# one = (78,)
# not_tuple = (78)
# print(type(one), type (not_tuple))

# # 튜플 인덱싱, 슬라이싱
# s = ("모터온도", 78, "C")
# print(s[0], s[-1])
# readings =(78, 80 , 79, 95, 77) 
# print(readings[1:4]) #(80, 79, 95)

#실습 1
# sensor = ("모터온도", 78)
# print(sensor)
# print(sensor[0],sensor[1])
# print(sensor[0])
# print(sensor[1])
# name, value = sensor
# print(name,value)

# 튜플 리스트 + 반복문(언패킹)
# - (이름, 값) 튜플들을 리스트로 모아 for 순회하면 이름, 값이 자동 분리
# sensors = [("모터온도", 78), ("펌프압력", 95)]
# for name, value in sensors:
#     # print(s)
#     if value > 90:
#         print(name, "경고")

#실습 2
# sensors = [("회전속도", 100), ("펌프압력", 95)]
# for name, value in sensors:
#     # print(name, value)
#     if value >90:
#         print(name, "경고")

#중첩 튜플
# sensors =('모터온도', 78, (3,5))
# print(sensors[2][0])

# #튜플 리스트 정렬
# print(sensors[2][0])

# 튜플 리스트 정렬
# sensors = [(78, "모터온도"), (95, "베어링진동"), (32, "펌프압력")]
# hot = sorted(sensors, reverse=True)
# print(hot)

#실습 3
sensors = [
    ("모터온도", 30, (2, 3)),
    ("베어링진동", 4, (8, 4)),
    ("펌프압력", 30, (5, 7))]
for name, value, (x, y) in sensors:
    print(name,(x,y))
    if x <= 5:
        print(name)

