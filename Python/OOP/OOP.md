클래스와 객체


class 이름 .
Person.say_hello(young, 5)
# syntetic honey
young.say_hello(5)
사실은 같은 코드이다.

#instance method 
특정 methond에 관련있는 instance이다.

파이썬에서는 숨겨진거보다 대놓고 하는게 낫다는 철학

self는 instance를 넘겨줄때는 그것을 씁니다.

#class variable

변수를 변경할 때 
인스턴스 -> 클래스를 본다. 

#class method
@classmethod 데코레이터
Class에 해당하는 파라미터로는 cls이고, class method에서는 

def disaster(cls, n):
    Person.population -= n
Person.say_hello(young)

print(Person.population)

young.disater()

1. cls 

#static method
@staticmethod
def hello():
    print("Hello world")


#Special Method
인스턴스와 클래스와 연관이 없으면

독립적인 함수를 생성하고 싶을때 사용한다.

#
def __str__:
객체에 대한 정보를 출력
먼저 def __repr__를 찾고

객체 지향 프로그램

객체와 객체 사이에 어떤 상호작용을 하는 방식에 대한 철학
키워드나 언어 자체적으로 객체를 만들수 있고, class method 같은 메소드를 만들어서 쓸 수 있다.

파이썬은 모든게 객체이다.

자바에는 
primitive data type // boolean, int, char, long, short
reference type // 

python에는 muttable 타입과 immutable 데이터 타입이 있다.
muttable references
immutable primitive


# 상속
# 추상화의 장점 

# MRO 란 METHOD order
# isinstance(class, instance)
# 인스턴스가 클래스의 인스턴스인지 확인하는 method 
# issubclass(subclass, class)
# class가 subclass인지 확인하는 method

interface 추상화된 행위들을 정의해둔다.
추상화 클랜스는 instance를 만들 수 없다.

interface는 모든게 추상화된 class
추상화 클래스는 구현이 된 class도 있고, 추상화된 class가 있다.



