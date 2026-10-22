# 문자열 연산과 검색
# - 문자열 연결(+), 반복(*)

# len() - 글자수를 알수있게 해준다
# 형식 :  len(문자열)
print(len('PYTHON'))
print(len('AI 분석')) # 공백도 글자수에 포함
print(len(''))

# in / not in - 포함 / 불포함 여부(결과 bool)
# 형식 : '찾을것 ' in 문자열
print('고장' in '설비 고장 발생') #True
print('정상' not in '고장 발생') #True

# count
# 형식 : 문자열 .count('x') -> 개수
print('banana'.count('a')) # 3개

#find 
# 형식 : 문자열.find('x') -> 처음 나오는 위치
print('banana'.find('a')) # 찾을경우 1
print('banana'.find('t')) # 못찾을경우 -1

# #실습
# word = "01012345678"
# print(len(word))

#실습2
# word = '설비 고장 발생'
# print('고장'in word)
# print('정상'in word)

#실습 3
word = 'sensor-01-temp'
print('sensor-01-temp'.count('-'))

#실습 4
word = 'temp_2024'
print('temp_2024'.find('_'), 'temp_2024'.find('o'))
# index
# 주의) 위치를 반환 하지만 없으면 오류 발생
email = 'hong@compnay.com'
at = email.index('@')
print(at)
print(email[:at]) # hong

#startswith/ endswith
# 형식: 문자열.startswith('x') --> bool
# print('EQP-001'.startswith('EQP'))
# print('cmapss.scv'.endswith('scv'))

#실습5
letter ='sensor_log.scv'
print('sensor_log.scv'.startswith('sensor'),('sensor_log.scv'.endswith('.scv')))

#실습6

