#함수 설계와 활용

# 기본값 인자
# 형식:
# def 함수(매개변수, 선택=기본값):

# 거의 항상 같은 값을 매번 적는 번거로움을 줄임 ,필요할때만 덮어쓴다
# def report(name, value, unit="도"):
#     print(f'{name}:{value},{unit}')

# report("압축기1", 75.3) # 압축기1:75.3,도
# report("펌프1", 7.2, "bar") #펌프1:7.2,bar

#실습 1
# def status(temp, limit=90):
#     if temp > limit:
#         print("경고")
#     else:
#         print("정상")
# status(78)
# status(95)
# status(50, 40)

# 지역변수와 범위(스코프)
# - 함수 안 변수, 함수 바깥 변수를 읽을수 있지만 , 바깥에서는 함수 안 지역변수를 읽을수 X
# def calc():
#     result = 10 + 5 # 지역변수
#     return result # 밖에서 사용 하려면 return 으로 내보내야함

# print(calc())

# x = 10
# def change():
#     x = 20 # 함수 내부의 지역변수
# change()
# print(x) # 10 (함수 바깥의 x 값 변경 x )
# 함수 선언
# 지역변수 생성
# 함수 밖에서 해당 지역변수 호출, 결과 확인

#실습 2
# def numbering():
#     x = 30
# print(x)

# 함수 조합(함수 설계: 입력/ 처리/출력)
# def get_avg(values):
#     return sum(values) / len(values)

# def judge(avg, limit=80):
#     if avg > limit:
#         return "위험"
#     else:
#         return "정상"
    
# temps = [75, 88 ,91]
# avg = get_avg(temps)
# print(round(avg, 1),judge(avg))

#실습 3
def pump(values):
  avg = sum(values) / len(values)
  if avg <= 85.0:
    return "정상"
  else:
    return "위험"
temps = [75, 89, 91]
avg = sum(temps) / len(temps)
print("평균", avg, pump(temps))