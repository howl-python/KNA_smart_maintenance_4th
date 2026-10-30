import os
import csv

# 파일 입출력
# open()
# 형식: open(파일명, 모드, encoding)
# - 모드 : r =읽기 , w = 새로쓰기 , a = 이어쓰기
# - encoding = "utf-8" => 한글이 꺠지지않도록 하는것

FILE = "data/08_press.csv"

# f = open(FILE, "r", encoding="utf-8")
# text = f.readlines()
# print(type(text), len(text))
# f.close() #파일을 열고 닫기까지

# #with opne - 블록이 끝나면 자동 닫힘
# with open(FILE, "r", encoding="utf-8") as f:
#     for line in f:
#         print(line)

# write()
# with open("data/test.text", "w",encoding="utf-8") as f:
#     f.write("쓰기 테스트")

#실습 2
# with open("data/test.text", "w", encoding="utf-8") as f:
#     f.write("texting in file\n test again")
# with open("data/test.text", "r", encoding="utf-8") as f:
#      print(f.read())

#실습 3
# with open("data/test.text", "a", encoding="utf-8") as f:
#     f.write("\n 마지막 내용")
# with open("data/test.text", "r", encoding="utf-8") as f:
#     print(f.read())

#csv.reader
# with open(FILE, "r" ,encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)

# 실습 4
# import csv
# with open(FILE, "r" ,encoding="utf-8") as d:
#     reader = csv.reader(d)
#     for row in reader:
#         print(row)

#csv.wrtier
# import csv
# with open("data/08_summery.csv", "w", uncoding="utf-8", newline="") as f:
#     writer = csv.writer(f)
#     writer.writerow(["설비ID", "상태"])
#     writer.writerow("PRESS-01, 1")
#     writer.writerow("PRESS-02, 2")
# with open("data/08_summery.csv", "r", encoding="utf-8") as f:
#     reader = csv.reader(f)
#     for row in reader:
#         print(row)
#실습 5
import csv
with open("data/08_summery.csv", "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["설비ID", "상태"])
    writer.writerow(["PRESS-01", 1])
    writer.writerow(["PRESS-02", 2])
