# 메서드 - 점 (.) 문법
# 형식 : 문자열.메서드이름(--> 꼭 괄호를 붙여야함)
# word = 'python'
# #upper (): 모두 대문자
# print(word.upper()) #  PYTHON
# print(word.count('p')) # 1
# # lower () : 모두 소문자
# print('NOMAL'.lower())

# print('python is'.capitalize())
# print('hong gil dong'.title())

#실습 1
# word ='ready'
# print('ready'.upper())
# #실습
# status ='WARNING'
# print('WARNING'=='WARNING','WARNING'=='warning')
# #실습
# status ='WARNING'
# print('WARNING'.lower())
# #실습3
# word = 'NOMAL'
# print('NOMAL'.lower())
# #실습4
# word ='kim chul soo'
# print(word.title())
#실습
word = 'falut' == 'FALUT'
print(word)
word = 'fault'.lower() == 'FAULT'.lower()
print(word)

#확인 메서드 : (is *** 메서드는 참/거짓만 반환
print('ABC'.isupper(), 'abc'.islower())
# 공백 정리 - strip
# 형식: .strip() = 앞뒤 공백 제거
raw = '  정상  '
print('[' + raw + ']')              # [  정상  ]
print('[' + raw.strip() + ']')      # [정상]

#.lstrip() -> 왼쪽 공백을 제거/ .rstrip() -> 오른쪽 공백 제거
# 주의) strip은 '앞뒤'공백만 제거 , 가운데 공백제거 x 
#strip()으로 특정 문자 제거할경우 ->strip('문자')
# s = "###정상###"
# print(s.strip("#")) #정상

# #실습5
# word = 'ABC','abc','Abc'
# print('ABC'.isupper()),print('abc'.islower()),print('Abc'.islower())

#실습6
word = 'Sensor_LOG.CSV'
word = word.lower()
print(word)
print(word.startswith('sensor'))
print(word.endswith('.csv'))
#실습7
text = ' 가동중'
text = text.strip()
print('[' + text + ']')

#실습8
text = ' 대기 '
print('[' + text.lstrip() + ']')
print('[' + text.rstrip() + ']')

#실습9
word = '***경고***'
clean = word.strip('*')
print(clean)  # 경고

# 체이닝 - 메서드 이어 붙이기
# 형식 : 문자열 .strip().lower() -> 왼쪽부터 차례대로 적용
clean = '   NORMAL  '.strip().lower()
print(clean)

#실습10
word = 'WARNING'
print('WARNING'.strip().lower())

#실습11
word = "  경보  "
word.strip()
print("[" + word + "]")
word = word.strip()
print("[" + word + "]")

