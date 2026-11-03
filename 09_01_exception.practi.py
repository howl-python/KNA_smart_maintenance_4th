# 각종 예외 상황
# temp = int("스물")   # ValueError: invalid literal for int() with base 10: '스물'
#  result = 10 / 0    # ZeroDivisionError: division by zero
# print(undefined_variable)  # NameError: name 'undefined_variable' is not defined

# try-except 구조
# try:
#     temp = int("스물")
# except ValueError:
#     print("valueError")

# try:
#     result = 10 / 0
# except ZeroDivisionError:
#     print("ZeroDivisionError")

# try:
#     print(undefined_variable)
# except NameError:
#     print("NameError")

# 실습 2 -
# temp_input = input("온도를 입력하세요: ")
# try:
#     temperature = float(temp_input)
#     print(f"입력된 온도: {temperature}")
# except ValueError:
#     print("유효한 숫자를 입력하세요.")

#실습 3
# try:
#     temp_input = input("온도를 입력하세요: ")
#     temperature = float(temp_input)
#     print("처리된 온도:", 100 / temperature)
# except ValueError:
#     print("잘못된 입력.")
# except ZeroDivisionError:
#     print("0으로 나눌수 없음")
    