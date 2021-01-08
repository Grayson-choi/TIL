class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.following_list = []
        self.followers_list = []

    def follow(self, other_user):
        self.following_list.append(other_user)
        other_user.followers_list.append(self)

    # follow 기능을 만드세요.


u1 = User("young", "young@email.kr")
u2 = User("sineui", "sineui@codeit.kr")
u3 = User("captaion", "captain@codeit.kr")
u4 = User("jiwoong", "jiwoong@codeit.kr")

u1.follow(u2)
u2.follow(u1)
u3.follow(u1)

print(u1.following_list)
print(u1.followers_list)
