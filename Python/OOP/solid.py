"""
Single Resonsibility Principle
Open-Closed Principle
Liskov Substitution Principle

단일 책임 원칙
클래스가 변할 이유 2014년에 책임이 무엇인가에 대한 글을 씀
변할 이유가 코드와 관련된 

개방 폐쇄 원칙
리스코프 치환 원칙  
인터페이스 분리 원칙 
의존 관계 역전 원칙

Single Resonsibility Principle
Open-Closed Principle
Open-Closed Principle
Open-Closed Principle
Open-Closed Principle
Open-Closed Principle
"""


# 2. 개방 폐쇄 원칙

from math import pi

class Circle:
    def __init__(self, radius):
        self.radius = radius

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width

circle_1 = Circle(2)
circle_2 = Circle(3)

rectangle_1 = Rectangle(2, 4)
rectangle_2 = Rectangle(2, 6)


