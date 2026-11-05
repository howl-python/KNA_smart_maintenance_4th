import numpy as np

# 인덱싱, 슬라이싱
# a = np.array(0,1,2,3,4)
# print(a[0], a[-1])
# print(a[1:4])
# print(a[::2])

#실습 1
# rpm = np.array([4603, 4200, 4350, 4480, 4520, 4610, 4700, 4650, 4590, 4603])
# print(rpm[0], rpm[9])
# print(rpm[2:4])
# print(rpm[1::])


# 실습 2
import numpy as np

# # 실습 2: 한 시점과 한 센서 따로 꺼내기
# data = np.array([
#     [4603, 2],
#     [58, 5],
#     [1216, 1],
#     [4967, 21]
# ])
# print(data)
# print(data[2])
# print(data[:, 0])
# print(data[:, 1])

#배열 연산
# 배열 연산
# 배열 연산
# a = np.array([1, 2, 3])
# b = np.array([10, 20, 30])
# print(a + b)       # [11, 22, 33]
# 같은 위치 값끼리 계산 (반복문 필요 X)
# 사칙연산 모두 같은 방식으로 계산

#스칼라 연산
# 숫자 하나를 배열 전체에 적용,크기를 맞출필요가없다
#- 연산 숫자는 수학과 같아 곱하기 먼저
# print(a * 10 + 3)

# 브로드캐스팅
# table = np.array([[72, 2.4], [95, 6.8]])
# print(table.shape)  # (2, 2)

# base = np.array([70, 2.0])  # (,2)

# print(table - base)

#[[ 2.   0.4]
# [25.   4.8]]
# 한 줄짜리 기준값이 모든 행에 퍼져서 계산됨
# 조건) 작은쪽에 크기가 1이거나 같아야함

#실습 3
# rpm = np.array([4603, 1241, 1217, 3143, 4697, 1216, 58 , 4987, 3143, 3632])
# print (rpm.min())
# print (rpm.max())
# new_rpm= rpm- rpm.min()
# print(new_rpm)
# normalized_rpm = new_rpm / (rpm.max() - rpm.min())
# print(normalized_rpm)
# print(np.round(normalized_rpm, 2))

# 비교 연산과 불리언 배열
# vals = np.array([70, 95, 71, 88, 73])
# print(vals > 75) #[False  True False  True False]

# # 불리언 인덱싱
# print(vals[vals > 75 ])

# # np.where (조건 , 참일때 값 , 거짓일때 값)
# print(np.where(vals > 85, 1, 0))

# # 다중 조건
# print(vals[(vals > 70) & (vals < 90)])

# 실습 4
# rpm = np.array([58, 4603, 3632, 1217, 4987, 4967, 3143, 4603])
# current = np.array([44, 69, 4, 84, 51, 19, 15, 55])
# low_rpm = rpm < 2000
# cond = (rpm < 2000) | (current > 25)
# print(np.sum(low_rpm), np.mean(low_rpm))
# print(np.sum(cond), np.mean(cond))
# print("------------------")
# #실습 5
# torque = np.array([2, 2, 5, 3, 2, 3, 147, 21, 3, 9])
# condition = torque > 10
# count = np.sum(condition)
# ratio = np.mean(condition) 
# print(count, ratio)

# 통계
# - 정상을 알아야 이상을 알 수 있다
# ex) 평균을 알아야 평균과 크게 차이가 나는 값이 나왔을 때 이상치 판단 가능
# - 평균, 최대/최소, 표준편차, 분산
# Numpy 에서 함수 하나로 계산

# s = np.array([70, 72, 71, 95, 73])
# print("합계:",s.sum())
# print("평균:",s.mean())
# print("중앙값:",np.median(s))
# print("최대:",s.max())
# print("최소:",s.min())

# # 분산
# stable = np.array([70, 71, 70, 72, 71])
# unstable = np.array([60, 85, 65, 95, 70])
# print(round(stable.var(), 1 )) # 0.6
# print(round(unstable.var(), 1 )) #170.0

# #표준편차 
# print(round(stable.std(), 2 )) 
# print(round(unstable.std(), 2 )) 

# # axis 개념 (행/열 방향)
# mat = np.array([[70, 2.1], [72, 2.3]])
# print(mat.mean(axis=0))    # 열별 평균 (센서별)
# print(mat.mean(axis=1))    # 행별 평균 (시점별 ) -> 지금은 큰의미 x
# print(mat.mean())          # 전체 평균

#실습 6
# data = np.array([
#     [4603, 2],
#     [4200, 5],
#     [4350, 21],
#     [4480, 3]
# ])

# m = data.mean(axis=0)
# s = data.std(axis=0)
# print("평균:", round(m[0], 1), round(m[1], 1))
# print("표준편차:", round(s[0], 1), round(s[1], 1))

# 파일에서  배열로 불러오기(nploadtxt)
# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",        # 값을 나누는 기호
#                  skiprows=1,           # 첫 줄(제목)은 제외
#                  usecols=4)            # 5번째 열 데이터만 가져옴 5

# print(rpm.shape,rpm.dtype)

# 실습 7
# rpm = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",
#                  skiprows=1,
#                  usecols= 4
# )

# print("회전수 평균:", round(rpm.mean(), 1))
# print("표준편차:", round(rpm.std(), 1))
# print("최소:", rpm.min())
# print("최대:", rpm.max())

# 실습 8
# t = np.loadtxt('data/10_mct_tool.csv',
#                  delimiter=",",
#                  skiprows=1,
#                  usecols= 5
# )
# print(t[t > 10])
# new_t = (t[t > 10])
# print(new_t)
# print("평균:", round(new_t.mean(), 1))
# print("개수:", new_t.size )

# 실습 9
import numpy as np

data = np.loadtxt('data/10_mct_tool.csv', 
                delimiter=",", 
                skiprows=1,
                usecols=(4, 5))
print(data.shape)
print(data.dtype)

rpm = data[:, 0]
filtered_data = data[rpm <= 2000]

print(filtered_data.shape[0])
print(round(filtered_data[:, 0].mean(), 1))
print(round(rpm.mean(), 1))