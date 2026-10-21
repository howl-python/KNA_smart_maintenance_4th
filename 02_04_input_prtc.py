# name = input("이름:")
# age = input("나이:") #이렇게 되면 나이입력을 못함 int 
# print(name)

# birth = int(input("태어난해:"))
# age = 2026 - birth +1
# print("나이:" , age)
# height = float("173.5")
# print(height , type(height))


# 실습 
print(3>2) #True
print(5 == 5) # True
print(type(3 > 2)) # <class 'bool'>

#실습
# country = input("거주 국가:")
# city = (input("도시:"))
# result = country + "의 " + city + "에서 거주하시는군요"
# print(result)

# a = int(input("첫번째 숫자:"))
# b = int(input("두번쨰 숫자:"))
# print ("덧셈" , a + b)
# print("뻴셈" , a - b)
# print("나눗셈" ,a / b)
# print("곱셈" , a* b)

# temp =float(input("온도을 입력하시오"))
# print("80 초과?", temp > 80)
# print("0이하" , temp <=80)

device_temp = 25.5
check_count = 3
device_name = "센서A"
is_normal = True

print(device_temp)
print(check_count)
print(device_name)
print(is_normal)

print(5 == 5)
print(5 != 3)
print(7 > 10)
print(7 < 10)
print(5 >= 5)
print(4 <= 3)

score1 = int(input("첫번째 점수: "))
score2 = int(input("두번째 점수: "))
score3 = int(input("세번째 점수: "))

total = score1 + score2 + score3
avg = total / 3

print("평균:", avg)
print("평균 60점 이상인가?", avg >= 60)