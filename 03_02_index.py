#   인덱싱 - 위치번호로 글자하나 꺼내기
# 형식 : 문자열 [번호] (첫글자 = 0번)
#  word = 'PYTHON'
# print(word[0], word[2], word[5]) #P T N
# # 음수 인덱스 : 뒤에서부터 -1 -2 ...
# print(word [-1],word [-2])  #N O
# # (word[6])

#실습1
# word = "SIGNAL"
# print(word[0],"/",word[2],"/",word[5])

#실습2

# word = "SIGNAL"
# print(word[-1],"/",word[-2])

#슬라이싱 - 구간으로 잘라내기
#형식 : 문자열[시작:끝] (시작포함, 끝 제외)
# - 시작생략 = 처음부터 (0번부터)
# - 끝 생략 = 끝까지
# - 둘 다 생략 =전체
# print(word[:3])
# print(word[3:])
# print(word[:])

# #음수
# print(word[-3:])
# print(word[:-1])

# #실습 3
# word = "SIGNAL"
# # print(word[0:3],word[3:0],word[3:0],word[2:5])

# 실습 4
# word = "temp_sensor"
# # print(word[:4])
#실습 5번
# print(word[5:])

#실습 6 
# word = "sensor_01"
# print(word[-2:])

# #STEP 간격 주기
# # 형식 : 문자열[시작:끝:간격]
# word = "PYTHON"
# print(word[::2])
# print(word[1::3])

#실습 7
word = "SIGNAL"
print(word[::2])
print(word[::-1])
