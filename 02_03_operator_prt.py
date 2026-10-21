a ,b = 17, 5
print(a + b, a - b, a * b, a / b, a // b, a % b, a ** b)
score1 = 80
score2 = 90
score3 = 91

평균 = (score1 + score2 + score3) / 3

가로 = 7
세로 = 7
넓이 = 가로 * 세로

길이 = 3
너비 = 4
높이 = 5
부피 = 길이 * 너비 * 높이

print("평균 =", 평균)
print("넓이 =", 넓이)
print("부피 =", 부피)

temp = 85
pressure = 5
temp_ok = temp >= 60 and temp <= 90
pressure_ok = pressure >= 3 and pressure <= 7
print("온도정상" , temp_ok)
print("압력정상" , pressure_ok)
print("모두정상" , True)

#실습 5
count = 100
print(count)

count += 50
print(count)

count -= 30
print(count)

count += 5
print(count)

total = 500
defect = 23
defect_rate = defect / total * 100
print("불량률:", defect_rate, "%")

operating_time = 21
total_time = 24
operation_rate = operating_time / total_time * 100
print("가동률:", operation_rate, "%")

total = 500
hours = total // 60
minutes = total % 60

print(hours, "시간", minutes, "분")


