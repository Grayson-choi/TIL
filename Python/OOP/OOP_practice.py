class User:
    def __init__(self, name, email):
        print(self)
        print(name)
        print(email)
    
    def say_my_name(self):
        print(self.name)

User("Yoonsoo", "yoonsoo@codeit.kr")

u1 = User()
u1.name = "Yoonsoo"
u1.email = "YYY@codeit.kr"
