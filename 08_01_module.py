# 모듈 / 패키지 / 라이브러리
# - 모듈: 기능을 모아둔 .py 파일 하나
# - 패키지: 필요한 모듈을 모아둔 폴더
# - 라이브러리 : 위에 사항들을 통칭

# import 방식
# 형식 : import 모듈 import 모듈명 별칭
# import math  # math라는 모듈을 통째로 불러옴
# print(math.sqrt(16))  #
# from math import sqrt, ceil # 일부만 불러옴 -> 모듈명없이 바로 사용가능 
# print(sqrt(16), ceil(4.2))
# import math as m
# print(m.sqrt(16))

#실습 1
# import math
# print(math.sqrt(16), math.ceil(4.2))
# from math import sqrt, ceil
# print(sqrt(16), ceil(4.2))
# import math as t
# print(t.sqrt(16), t.ceil(4.2))

#표준 라이브러리 -math /random /dattime
# 파이썬 설치 시 함께 깔리는 검증된 모듈들 
# import random
# import datetime

# print(random.randint(1, 100))
# print(datetime.datetime.now())

#실습 2
# import random
# import math
# sensor = random.randint(1, 100)
# print(math.sqrt(sensor))

#//////////
# 경로와 os 모듈
# - 파일을 다루려면 어디에 있는지 경로를 알아야 한다
# 1) 절대경로
#   - 최상위부터 전체 주소
# 2) 상대경로
#   - 지금 실행중인 위치를 기준으로 한 주소
# import os
# cwd = os.getcwd()
# print("현재 실행 위치 (절대경로):", cwd)
# # 폴더 유무 확인 
# print(os.path.exists("data"))

# 폴더 목록 확인 
# files = os.listdir("data")
# print(files)
#폴더명+ 파일명 -> 폴더명과 파일명을 결합하여 파일이 저장된 위치를 나타내는 주소를 **경로(Path)**라고 한다.
#실습 3
# import os
# print(os.getcwd())      # 현재 작업 폴더
# files = os.listdir("data")
# for file in files:
#     print(file)

# print("=========")
# for file in files:
#     if file.endswith(".csv"):
#         print(file)
# #폴더명+ 파일명 -> 경로

#실습 4
# import os
# path = os.path.join("data", "roll.text")
# if os.path.exists(path):
#     print('파일있음:', path)
# else:
#     print('파일없음', path)

#실습 5
# import datetime
# import os
# files = os.listdir("data")
# print(f"파일 수:{len(files)}개,점검 시각: {datetime.datetime.now()}")

#실습 6
# import os
# files = os.listdir("data")
# csv_files = []
# for file in files:
#     if file.endswith(".csv"):
#         csv_files.append(os.path.join("data", file))
# print(csv_files)