# def outer_func(): #1
#     message = 'Hi' #3

#     def inner_func(): #4
#         print(message) #6
    
#     return inner_func() #5

# outer_func() #2

# 프로그램을 실행하니 "Hi"라는 문자가 출력되었습니다. 
# 간단한 구문이지만 클로저를 설명하기 위해 "Hi"가 출력되기까지의 프로세스를 하나씩 확인해 보겠습니다.

#  1. #1에서 정의된 함수 outer_func를 #2에서 호출을 합니다. 물론 outer_func는 어떤 인수도 받지 않습니다.
#  2. outer_func가 실행된 후, 가장 먼저 하는 것은 messge 라는 변수에 'Hi'라는 문자열을 할당합니다. #3입니다.
#  3. #4번에서 inner_func를 정의하고 #5번에서 inner_func를 호출하며 동시에 리턴합니다.
#  4. #6에서 message 변수를 참조하여 출력합니다. 여기서 message는 inner_func 안에서 정의되지는 않았지만, 
#  inner_func 안에서 사용되기 때문에 프리변수라고 부릅니다.
#  "Hi"가 출력되기까지의 일련의 프로세스는 위와 같습니다. 

# def outer_func1(): #1
#     message = 'Hi' #3

#     def inner_func(): #4
#         print(message) #6
    
#     return inner_func #5 <- ()를 지우면 실행이 안되는데, #1이 함수를 실행하지않고, 함수 오브젝트를 리턴했기 때문이다.

# outer_func() #2


# def outer_func2(): #1
#     message = 'Hi' #3

#     def inner_func(): #4
#         print(message) #6
    
#     return inner_func #5 <- ()를 지우면 실행이 안되는데, #1이 함수를 실행하지않고, 함수 오브젝트를 리턴했기 때문이다.

# my_func = outer_func2() #2

# print(my_func)

# my_func()
# my_func()
# my_func()

# #2 outer_func는 분명히 #2에서 호출된 후, 종료되었습니다. 그런데 #7, #8, #9에서 
# 호출된 my_func(*여기서 my_func은 inner_func와 같음) 함수가 outer_func 함수의 로컬변수인 message를 참조했다는 겁니다.
# 이것이 가능한 이유는 클로저 때문이다. 클로저는 함수의 프리변수 값을 어딘가에 저장한다고 했던것 같습니다.

# def outer_func2(): #1
#     message = 'Hi' #3

#     def inner_func(): #4
#         print(message) #6
    
#     return inner_func #5 <- ()를 지우면 실행이 안되는데, #1이 함수를 실행하지않고, 함수 오브젝트를 리턴했기 때문이다.

# my_func = outer_func2() #2

# print(my_func) #7 결과: my_func에 inner_func 함수 인스턴스 할당
# print()
# print(dir(my_func)) #8 결과 클로저가 어디에 데이터를 숨기는지 확인 __closure__ 라는 속성이 있음
# print()
# print(type(my_func.__closure__)) #9 __closure__는 튜플
# print()
# print(my_func.__closure__) #10 튜플에는 아이템이 하나 들어있음
# print()
# print(my_func.__closure__[0])
# print()
# print(dir(my_func.__closure__[0])) #11 #10에 cell object에는 뭐가 있는지 확인한다. 
# print()
# print(my_func.__closure__[0].cell_contents) #13 cell_contents에 hi라는 글자가 들어있음

def outer_func(tag): #1
    text = 'Some text' #5
    tag = tag #6

    def inner_func():
        print('<{0}>{1}<{0}>'.format(tag, text))

    return inner_func

h1_func = outer_func('h1') #2
p_func = outer_func('p') #3

h1_func()
p_func()

# 클로저를 활용하여 여러가지 함수를 간단히 만들수도 있고, 기존에 함수나 모듈을 등을 수정하지 않고도 
# wrapper 함수를 이용해 커스터마이징 할 수 있게 해준다.


