from abc import *

class Report(Ship):

    @abstractmethod
    def report_crew(self):
        """선박 인스턴스의 선원 보고 메소드"""
        print("현재 선원 {}명이 있습니다".format(self.num_crew))

    @abstractmethod
    def report_supplies(self):
        """선박 인스턴스의 물자 보고 메소드"""
        print("현재 물자는 {}명 분이 남아 있습니다".format(self.supplies))
    
    def report_fuel(self):
        """선박 인스턴스의 연료 보고 메소드"""
        print("현재 연료는 {}l 남아 있습니다".format(self.fuel))



class Ship:
    def __init__(self, fuel, fuel_per_hour, supplies, num_crew):
        self.fuel = fuel
        self.fuel_per_hour = fuel_per_hour
        self.supplies = supplies
        self.num_crew = num_crew
    

class AbstractShip(metaclass = ABCMeta):
    fuel = "연료"
    fuel_per_hour = "연료 소비율"
    supplies = "물자"
    num_crew = "선원" 

class Distribute(self):

	def distribute_supplies_to_crew(self):
		"""선박 인스턴스의 물자 분배 메소드"""
		self.supplies -= self.num_crew

class Load(self):
    def load_crew(self, amount):
        self.num_crew += amount

    def load_fuel(self, amount):
        self.fuel += amount

    def load_supplies(self, amount):
        self.supplies += amount

class Supply:
    def refill(self, amount):
        pass        


class Engine(Ship):

    def run_engine_for_hour(self):
        """선박 인스턴스의 엔진을 한 시간 돌리는 메소드"""
        if self.fuel > self.fuel_per_hour:
            self.fuel -= self.fuel_per_hour
            print("엔진을 한 시간 동안 돌립니다!")
        else:
            print("연료가 부족하기 때문에 엔진을 시작할 수 없습니다")
    


# 선박 인스턴스 정의
ship = Ship(400, 10, 1000, 50)

# 선원 승선, 물자 및 연료 재보급
ship.load_crew(10)
ship.load_fuel(10)
ship.load_supplies(10)

# 엔진 1시간 동안 운행
ship.run_engine_for_hour()

# 선박의 상태 보고
ship.report_fuel()
ship.report_supplies()
ship.report_crew()

