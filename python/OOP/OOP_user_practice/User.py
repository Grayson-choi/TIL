
"""
User

variable:

email
id
pw
friend_list = []

method
add_friend(self, friend) --> None
verify(email, pw) --> Bool

(class variable)
number_of_user

class method
how_many_users(cls) --> int


"""

class User(object):
    number_of_user = 0
    
    def __init__(self, email, id, pw, follower_list = None):
        if follower_list == None:
            follower_list = []
        self.email = email
        self.id = id
        self.__pw = pw
        self.follower_list = follower_list
        User.number_of_user += 1

    
    def __str__(self):
        return '이메일:{} 아이디:{} 비밀번호:{} 친구목록{}입니다.'.format(self.email, self.id, self.__pw, self.follower_list)

    def __len__(self):
        return self.number_of_user

    def add_follower(self, friend):
        self.follower_list.append(friend.id)
        if friend == self:
            print('[경고] 스스로 친구가 될 수 없습니다.')
        return None
    
    def verify(self, email, pw):
        if self.email == email and self.__pw == pw:
            return True
        else:
            return False
    
    def more_followers(self, other_user):
        if len(self.follower_list) > len(other_user.follower_list):
            return True
        else:
            return False


    @classmethod
    def how_many_users(cls):
        return cls.number_of_user

    def change_password(self, id, current_pw, new_pw):
        if self.id == id and self.__pw == current_pw:
            self.__pw = new_pw
        return None
        

print(User("wldnd@email.com", "choijiwoong", "pw11"))
print(User("taeho@email.com", "taeho", "pw12"))
print(User("kyoosik@email.com", "kyoosik", "pw13"))

jiwoong = User("wldnd@email.com","choijiwoong","pw11")
taeho = User("taeho@email.com","taeho","pw12")
kyoosik = User("kyoosik@email.com","kyoosik","pw13")

jiwoong.add_follower(taeho)
print(jiwoong.verify("wldnd@email.com","pw11"))
print(jiwoong.change_password("choijiwoong", "pw11", "pw22"))
print(jiwoong.verify("wldnd@email.com","pw11"))
print(jiwoong.follower_list)
print(User.how_many_users())


