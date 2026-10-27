# while 조건이  참인 동안 반복
# 형식 :
# while 조건식:     (조건이 거짓인 순간 멈춤)
#for - '몇번이 정해졌을때', while은 '언제 끝날지 모르지만 조건으로 멈출때' 사용

# count = 1
# while count <= 3:
#     print(count)
#     count += 1
 #주의) 무한 루프를 막으려면 (1) 언젠가 거짓이될것 , (2) 반복문 안에서 그조건 갱신
 # 처음부터 조건이 거짓이면 한번도 실행되지않는다

#  #실습 1
# start = 1
# goal = 7
# while start != goal:
#     start += 1
#     print(start)

#break - 반복 도중에 완전히 멈추기
# for i in range(1, 11):
#     if i == 5:
#         break   # 5를 만나면 반복 즉시 종료
#     print(i)

# for i in  range(1, 7):
#     if i % 2 == 0:
#         continue
#     print(i)

#실습 2
count = int(input("횟수: "))
found = False
for i in range(count):
    v = int(input("측정값: "))
    if v > 80:
        found = True
        break
if found:
    print("발견")
else:
    print("없음")

