# 연산 부호
# 연산자	뜻
# +	덧셈 (addition)
# -	뺄셈 (subtraction)
# *	곱셈 (multiplication)
# /	나눗셈 (division)
# %	나머지 (modulo)
# **	거듭제곱 (exponentiation)

# 파이썬 자료형 - 숫자 ,문자 , 불린

print(4 + 7)          # 4 더하기 7
print(2 - 4)          # 2 빼기 4
print(5 * 3)          # 5 곱하기 3
print(7 % 3)          # 7을 3으로 나눈 나머지
print(2 ** 3)         # 2의 3제곱

print(2 + 3 * 2)      # 덧셈보다 곱셈을 먼저 계산
print(2 * (2 + 3))    # 괄호안의 수식을 먼저 계산

# 정수형 (Integer)
# 파이썬의 규칙상, 정수형과 정수형 간의 연산 결과는 정수형으로 나옵니다.

# 그러나 '나눗셈' 연산에는 예외가 적용됩니다. 나눗셈의 경우에는, 
# 정수형과 정수형 간의 연산이더라도 결과값이 항상 소수형(floating point)입니다. 
# 예를 들어 print(8 / 2)의 결과값은 소수형 4.0인 거죠.

# 결과값이 정수형으로 나옴
print(1 + 2)        # 1 더하기 2
print(6 - 2)        # 6 빼기 2
print(3 * 4)        # 3 곱하기 4
print(11 % 4)       # 11을 4로 나눈 나머지
print(3 ** 2)       # 3의 2제곱

# 나눗셈 예외: 결과값이 소수형으로 나옴
print(7 / 2)        # 7 나누기 2
print(8 / 2)        # 8 나누기 2

# 문제 : print(10 / (10 % 6)) 는 어떤 값을 출력할까요?
# 답 : 2.5

# 문자열 포맷팅
# print("1 나누기 3은 %.4f" % (1.0 / 3))
# %d 는 10진수 %s 는 string
# 문자열 .4f은 소수점 4번째 까지만 나타낸다는 뜻이다.

# 불 대수 진리값
# True and True = True
# True and False = False
# True or True = True
# True or False = True
# not False = True

# type 타입을 확인하는 method

# print(1/10)

# def x_is_one():
#         global x
#         x = x + 1

# x = 5
# x_is_one()
# print(x)