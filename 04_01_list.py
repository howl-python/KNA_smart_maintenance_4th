# 리스트 
#  형식 : 이름 = [값1,값2 ...]
# 리스트는 여러 값을 '순서대로 하나의 이름에 담는다'

temps = [25, 26 ,27, 28] # 숫자 리스트
machines = ["펌프","모터","압축기"]
mixed = ["펌프",87,True] #종류가 달라도 한 리스트에 담을수있다

# print(len(temps)) # 개수를 얼마나 담았는지 보여줌
# print(len([]))

# #실습1
# box = [25,26,24,27,26]
# print(len(box))
# print(box)
# print(len([]))

# #실습2
# temps = [22, 25, 27, 24, 28, 23]
# print(temps[0],temps[2],temps[-1])

# #실습3
# line = [100, 110, 105, 120, 115, 122]

# first = line[0]
# last = line[-1]

# total = first + last

# print(total)
# print(total / 2)

# #실습4
# temps = [22, 24, 27, 28, 30, 21, 25, 26, 29, 23]
# print(temps[:3])
# print(temps[3:6])
# print(len(temps[:3]))

# #실습5
# number = [3, 4, 5, 6, 5, 4, 6, 7, 8, 7, 5, 3]
# first = number[:6]
# second = number[6:]
# print(first)
# print(second)
# print(len(first))
# print(len(second))

#값 바꾸기 / in  존재 확인 
# 형식 : 리스트 [번호] = 새로운 값 넣기/ 값 in 리스트
# nums = [25, 26, 24, 28, 27]
# nums[2] = 99
# print(nums)
# print("모터"in machines)

# # 값 추가 - append, insert,extend
# # 형식: 리스트.append(값)/ 리스트(insert(위치,값) /리스트 .extend(다른리스트)
# data = [25,26,24]
# # data.append(28) 
# # data.insert(1, 99)
# # data.extend([30, 31])
# print(data)

# #실습6
# temps = [25, 26, 24, 28, 27, 240]

# print(240 in temps)
# print(temps.index(240))

# temps[5] = 24

# print(temps)
# print(240 in temps)

# #실습7
# list = []
# list.append(30)
# print(list)
# list.insert(0,28)
# print(list)
# list.extend([31,32])
# print(list)

#값 삭제  - remove , pop, del
# 형식 :리스트 . remove(값) / 꺼낸값 = 리스트.pop(위치)/ del 리스트[위치]
# d = [25,26,24,28,27]
# d.remove(24)
# print(d)
# got = d.pop(1)
# print(got,d)
# del d[0]
# print(d)

# # 정렬,탐색 -sort,reverse / count , index
# # 형식 : 리스트 .sort() .reverse() count(값) .index(값)
# l = [27,24,30,22,26]
# l.sort()
# l.sort(reverse=True)
# l.reverse()
# print(l)

# r = ["정상", "이상", "정상", "이상"]
# print(r.count("정상"), r.index("이상"))

# #실습8
# list = [25,26,24,28,26,999]
# list.remove(999)
# print(list)
# got= list.pop(1)
# print(got)
# del list[0]
# print(list)

#실습9
temps = [28, 24, 30, 22, 26, 24, 27]
temps.sort()
print(temps)

temps.reverse()
print(temps)

print(temps.count(24))

temps.index(24)
print(temps.index(24))