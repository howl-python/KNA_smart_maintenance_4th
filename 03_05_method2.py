# #replace - 바꾸기/지우기
# # 형식 : 문자열.replace('바꿀것','새것')
# # - 모두 바꾸기, 결과는 저장 필요

# print('정   상  가  동'.replace(' ','')) #정상가동
# print('010-1234-5678'.replace('-', '')) #01012345678
# print('3,000'.replace(',', '')) #3000
# #체이닝 활용 가능 -> 여러 종류 문자 대체 차례대로 활용가능

# #split - 구분자로 나누기 (결과 -> 리스트
# # 형식 : 문자열.split('구분자') (구분자 생략 = 공백 기준)
# print('A1 A2 A3'.split())
# print('사과,배,감'.split(','))

# #실습1
# word ='설비 정상 가동'
# print('설비 점검 가동'.replace('설비 정상 가동','설비 점검 가동'))

# #실습 2
# word = 'PUMP A 03'
# print(word.split(' '))

# #실습3
# word ='a,b,c,d'
# print(word.split(','))

# #실습4
# word ='a,b,c,d'
# print(word.split(',',1))

# #join 합치기 (리스트 -> 문자열)
# #  형식 : '구분자'.join()
# print('-'.join(['2025', '01', '15']))

# split+ join
# - split : 문자열 -> 리스트
# - join: 리스트 -> 문자열
raw = '사과,배,감'
# p= raw.split(',')
# print(p)          # ['사과', ' 배', ' 감']
# print('/'.join(p))    # 사과/ 배/ 감
# print('/'.join([p[0].strip(), p[1].strip(), p[2].strip()]))  # 사과/배/감

# # #실습5
# date = '2025','01','15'
# print('-'.join(['2025', '01', '15']))

# #실습6
# word = '2025115'
# print('-'.join(['2025','1','15']),','.join(['2025','1','15']))
# 실습6 오답노트
word ='2025115'
print('2025', '1', '15', sep='-')
print('2025', '1', '15', sep=', ')

#실습7
# date = '2025/01/15'
# print(date.split('/'))
# print('-'.join(date.split('/')))
#실습7 오답노트
word = '2025/01/15'
print('-'.join(word.split('/')))

# #실습8
# word = '1, NORMAL ,25.3'
# parts = word.split(',')
# status = parts[1].strip().lower()
# print(status)

