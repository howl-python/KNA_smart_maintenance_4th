#실습 1
# temps = [25, 32, 28, 35, 19, 31]
# for t in temps:
#     if t >= 30:
#         print("고온:", t)

#실습 2
# work = [3, 8, 6, 10, 9, 11]
# for t in work:
#     if t >= 5 and t <= 10:
#         print(t)

# 최대, 최소
# temps = [25, 32, 28, 36, 27, 31]
# biggest = temps[0]

# for t in temps:
#     if t > biggest:
#         biggest = t    # 더 큰값일 때 갱신
# print(biggest)

#빈 리스트 채우기
# doubled = []
# for t in temps:
#     doubled.append(t * 2)
#     print(doubled) #[50, 64, 56, 72, 54, 62]

#실습 3
# temps = [25, 32, 28, 36, 27, 31]
# total = 0
# count = 0
# for t in temps:
#     if t > 30:
#         total = total + t
#         count = count + 1
# average = total / count
# print("고온 평균:", average) 

#실습 4
# temps = [29, 30,32 , 31, 35, 33]
# high = []
# for t in temps:
#     if t > 30:
#         high.append(t)
# print(high)
# print(len(high))

#실습 5
# temps = [25, 26, 24, 28, 27]
# converted = []
# for t in temps:
#     result = round(t * 1.8 + 32, 1)
#     converted.append(result)
# print(converted)
# print(temps)

# 중첩 리스트 - 리스트 안에 리스트
# - 표(행, 열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
# rows = [["펌프", 25], ["모터", 32], ["압축기", 28]]
# for row in rows:
#     print(row[0], "온도", row[1])

#실습 6
temps = [20, 29, 31, 32, 33, 35, 36, 24]
total = 0
for t in temps:
    total = total + t
average = total / len(temps)
print("평균:", average)

high = []
for t in temps:
    if t > 30:
        high.append(t)
print("고온 개수:", len(high))

high_total = 0
for t in high:
    high_total = high_total + t
average = high_total / len(high)
print("고온 평균:", average)