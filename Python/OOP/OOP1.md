추상화 : 내용을 설명쓰지 않고, 정보를 숨기고, 내용을 모르고도 사용할 수 있는 것이다.
객체지향 : 변수, 함수, 클래스
High level overview (큰틀을 보여준다.)

User라는 타입을 만든다고 할 수있다.

pass를 쓰면 다 지나간다.
for instance 예를들어 instance 설명

dunder __init__같은 변수

Class 
변수 : attribute
함수 : method

파이썬 클래스와 연관 되어 있지 않으면 function
변수 : variable

생성자 : __init__ 이 생성자를 뜻한다.  
클래스에 기본적인 세팅을 한다.
__add__ 덮어 쓸 수 있다.

User.say_my_name()
u1.say_my_name()

User("jiwoong","yoonso@email.com") 생성자를 하고, 인스턴스를 생성하고, 그다음 파라미터를 넣는다.

클래스는 타입으로 볼 수 있다.

print(type(u1))
print(type(1))
print(type('hello'))

print(2 + 5) +는 integer class의 method이다. 


파이썬은 모든 값이 인스턴스다.
자바는 기본 자료형이 직접 메모리에 저장되는데, 파이썬에서는 기본 자료형이 없어서 클래스 타입에 인스턴스다. 
루비에서는 1이 인스턴스이기때문에 method를 쓸 수 있다.

u1 = User("Yoonsoo", "yoonsoo@codeit.kr")
u2 = User("Young", "young@email.kr")