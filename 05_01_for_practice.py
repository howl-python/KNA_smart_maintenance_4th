 # 실습 1
# N = int(input("끝 숫자 N을 입력하세요: "))

# for i in range(1, N + 1):
#     print(i)

# for i in range(2, N + 1, 2):
#     print(i)

# for i in range(N, 0, -1):
#     print(i)


# # 실습 2
# N = 10
# total = 0

# for i in range(1, N + 1):
#     total += i

# print("합계:", total)


# # enumerate 실습
# temps = [25, 26, 24]

# for idx, t in enumerate(temps):
#     print(idx + 1, "번째:", t)
#실습 3
for dan in range(2, 10):
    print(dan)
    for su in range(1, 10):
        print(su)
        print("---------")
        print(f"{dan} x {su} = {dan * su}")
# 실습 4
# N = int(input("측정 횟수: "))
# count = 0

# for i in range(N):
#     value = int(input("측정값: "))
#     if value > 80:
#         count += 1

# print(count)
    
