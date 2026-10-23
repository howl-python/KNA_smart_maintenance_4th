# f-string 문자열 안에 변수를 바로 끼우기
# 형식 : f"~~~{변수}~~"

name = "홍길동"
age = 25
print(f'{name}님은 {age}살입니다')
# 숫자도 str 변환없이 바로 들어감
print(f'온도:{25.5}')
#중괄호 안에 계산식도 가능
hours = 3
print(f'{hours * 60}분')
#소수점 자리수 조정
# # 형식 : {값(변수):.2f} -> 소수점 두번쨰 자리까지 (자동반올림)
# value = 25.34567
# print(f'측정값: {value:.2f}')
# print(f'측정값: {value:.1f}')

#실습1
card = 'PUMP_A'
temp = '87도'
print('설비'f'{card}',('온도'f'{temp}'))

#실습2
point =80,90,91
print(f'평균{(80+90+91)/3}')

#실습3
point =87.456
print(f' {point:.1f},{point:.2f}')

#실습4
word = '5, sensor_2, WARNING, 0.78912'

parts = word.strip().split(',')

sensor = parts[1].strip()
status = parts[2].strip().lower()
value = float(parts[3].strip())

print(f'[센서 {sensor}] 상태 {status}, 측정값 {value:.2f}')