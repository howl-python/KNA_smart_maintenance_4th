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
p = np.array([[4603, 15.2], [4200, 18.4], [4350, 20.1], [4480, 17.8]])
print(p[2])
print(p[:, 0])
print(p[:, 1])