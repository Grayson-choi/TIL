class Person:

    def __init__(self, last_name, first_name, age):
        self.last_name = last_name
        self.first_name = first_name
        self.age = age
        self.full_name = first_name + ' ' + last_name


young = Person()
captain = Person()

# person에 해당하는 인스턴스를 2개 만든 것
young.last_name = "Kang"
young.first_name = "Young"
young.age = 25

print(young.last_name)
print(young.first_name)
print(young.age)

print(young.age)
print(young.age)
