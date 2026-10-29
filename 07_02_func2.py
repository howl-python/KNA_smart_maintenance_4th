#실습 1
# def check():
#     print("점검을 시작합니다")
# check()
# # check()
#실습 2
# def guide():
#     print("[설비 점검 안내]")
#     print("상태: 점검 예정 ")
#     print("위치:제강공장 가열로-2 ")
# guide()
# guide()


# def notice():
#     print("[설비 점검 안내]")
#     print("[상태: 점검 예정]")
#     print("[위치: 압연공장 압연로-2]")
# notice()
# notice()

#실습 3
# hello() #name 에러 발생
# def hello():
#     print("안녕하세요")
# hello()
# hello()

#실습 4
# def line():
#     print("=" * 10)

# def check():
#     print("점검을 시작합니다")
#     print("기록을 준비하세요")

# line()
# check()

# line()
# check()

# def check(name):
#     print(name + "점검을 시작합니다") # name 매개 변수

# check("압축기1")
# check("펌프1")
# # check() #type error check()
# check("A", "B") # TypeError: check() takes 1 positional

#실습 2
# def check_sensor(name, value):
#     print(name, value,"도")

# check_sensor("모터",78)
# check_sensor("펌프", 92)
# check_sensor(78,"모터")

#실습 3
# def sensors(name, value):
#     print(name, value)

# sensors("모터", value=78)
# sensors(name="펌프", value=92)

#return
# - print : 사람이 확인할수 있게 출력 / return  : 값을 프로그램에게 돌려줘서 이어쓸수있게한다
# def add(a, b):
#     return a+b
# print("실행안됨") # 이줄은 실행안됨
# total = add(3, 4)
# print(total) 

#실습 4
# def temperature(temp , sec):
#     second_temp = temp + sec
#     return second_temp

# result = temperature(80, 5)
# print(result)
# print(result + 5.0)

# 여러 값 반환 / 언패킹[cite: 1]
# - 쉼표로 여러 값을 return 하면 튜플로 묶여서 돌아옴 -> 언패킹 가능[cite: 1]
# def min_max(values):
#     return min(values), max(values)

# print(min_max([75, 10, 100]))
# low, high = min_max([75, 10, 100])
# print(low,high)
# def report(name, value):
#     return f"{name}: {value}"

# none = report("펌프", 10)
# print(none)

#실습 5
# values = [78, 92, 85.0]
# def sensor_stats(values):
#    avg = sum(values) / len(values)
#    low = min(values)
#    high = max(values)
#    return low, high ,avg
# low, high, avg = sensor_stats(values)
# print(low, high, avg)