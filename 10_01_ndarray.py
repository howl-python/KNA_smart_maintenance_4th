import numpy as np

temp = np.array
# 리스트 vs 배열
# 1) 리스트
# - 서로 다른 자료형도 같이 존재 가능
# # - 계산이 느리고 반복문을 돌아야 한다

# list = [70, 72, 71]
# print(list * 2)  #    
# print( [v * 2  for  v in list])

# #2)배열
# # - 같은 자료형만 존재가능
# # - 계산이 빠르다

# temp = np.array([70 , 72, 71]) 
# print(temp)   # [70 72 71]
# print(temp + 2) # [72, 74 73] 반복문 없는 묶음 계산

# 튜플로 배열 만들기
# print(np.array(1, 2, 3)) 

#실습 1
# temps =np.array ([70 , 72 , 80 , 85, 62, 92])

# print(temps)
# print("화씨 온도:", temps * 1.8 + 32)

# #배열 생성
# # np.arange(시작, 끝 ,간격): 연속 된 정수로 만듬
# # - 끝값은 포함안됨 
# print(np.arange(5))
# print(np.arange(0,10,2 ))

# #np.linspace(시작, 끝 ,개수 ) : 균등 분할 
# print(np.linspace(0, 1 ,5 ))
# print(np.linspace(0, 10 ,5 ))

#실습 2
# temps = np.linspace(0, 70, 8)
# print(temps)
# print(temps.shape)

# #실습 3
# number = np.arange(0, 45, 5)
# print(number)

# 배열 속성 
# ndim, shapem, size, dtype
# - 속성은 괄호X

# a = np.array([1.2,3])
# b = np.array([[1.2, 3], [4, 5]])

# print("dim:" , a.ndim, b.ndim)
# print("shape:", a.shape, b.shape)
# print("size:", a.size, b.size)

#실습 4

# temp =np.array([
#         [10,20],
#         [30, 40],
#         [50, 60],
#         [70, 80]
# ])
# elec = np.array([
#                 [1, 2],
#                 [3, 4],
#                 [5, 6],
#                 [7, 8]])
# print("dim:", temp.ndim ,elec.ndim)
# print("shape:", temp.shape, elec.shape)
# print("size:", temp.size, elec.size)

# 실습 5
# current = np.array([12.35, 18.69, 24.82, 31.47])
# print(current.dtype)
# new_current = current.astype(int)
# print(new_current)


# # reshape ()로 형태 바꾸기
# c = np.arange(12)
# print(c.reshape(3,4))
# # [[0 1 2 3]]
# # [ 4 5 6 7]
# # [8 9 10 11]

# # flatten() -> 1차원 만듦
# b3 = np.array([[1, 2, 3], [4, 5, 6]])
# print(b3.flatten())     # [1 2 3 4 5 6]

#실습 6
# cycle = np.array([
#     12.4, 13.1, 11.8, 12.9,
#     14.2, 13.7, 12.6, 11.9,
#     13.5, 14.1, 12.2, 13.0
# ])
# print(cycle)
# new_cycle = cycle.reshape(3 , 4)
# print(new_cycle)
# print("size:", cycle.size, new_cycle.size)
# print("======================")
# #실습 7
# data = np.array(
#     [30, 15.44, 1200, 31, 18.69, 1250, 32, 17.82, 1300, 33, 19.25, 1350]
# )
# print(data)
# new_data = data.reshape(4, 3)
# print(new_data)
# restored_data = new_data.flatten()
# print(restored_data)

import numpy as np

# 인덱싱, 슬라이싱
a = np.array(0,1,2,3,4)
print(a[0], a[-1])
print(a[1:4])
print(a[::2])