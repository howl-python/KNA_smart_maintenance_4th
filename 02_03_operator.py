# 연산자
# 산술 ,비교 , 논리 연산자

#산술 연산자
# 형식 : + , -, *,/ // (몫) % 나머지 **거듭제곱
#- 곱셈 , 나눗셈 ,등이 우선 순위 괄호이용 변경가능

#복합 할당
# 형식 : score += 10 <-> score = score + 10
score = 100
score += 10 
print(score)
# + - * / =붙여서 

#문자열 연산
# +,* 가능
print("안녕"+"하세요") # 안녕하세요
print("-" * 4) # ----
# 자료형이 같은거끼리만 연결가능 문자+숫자 x

# 비교 연산자 
# 형식 : == (같다) != (다르다) <> <= >=
print("정상" == "정상") #True
print("A" == "a") #False 

#논리 연산자 
# and: 모두 참이어야함 ,or : 하나만 참이어도 참 ,not :반대
print (True and False) #False
print (True or False) #True
print(not True) #False