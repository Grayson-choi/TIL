class User:
    # 인스턴스 변수 설정
    def __init__(self, user_name, email, password):
        self.name = user_name
        self.email = email
        self.password = password

        self.following_list = []    # 이 유저가 팔로우하는 유저 리스트
        self.followers_list = []    # 이 유저를 팔로우하는 유저 리스트


    # 팔로우
    def follow(self, another_user):
        # 코드를 입력하세요
        self.following_list.append(another_user.name)
        another_user.followers_list.append(self.name)

    # 내가 몇 명을 팔로우하는지 리턴
    def num_following(self):
        # 코드를 입력하세요
        return len(self.following_list)

    # 나를 몇 명이 팔로우하는지 리턴
    def num_followers(self):
        # 코드를 입력하세요
        return len(self.followers_list)

    def show_following(self):
        return self.followers_list

    def show_followers(self):
        return self.followers_list

# 유저들 생성
user1 = User("Young", "young@codeit.kr", "123456")
user2 = User("Yoon", "yoonsoo@codeit.kr", "abcdef")
user3 = User("Taeho", "taeho@codeit.kr", "123abc")
user4 = User("Lisa", "lisa@codeit.kr", "abc123")

# 유저마다 서로 관심 있는 유저를 팔로우
user1follow()
user1.follow()
user2.follow()
user2.follow()
user2.follow()
user4.follow()

# 유저 이름, 자신의 팔로워 수, 자신이 팔로우하는 사람 수를 출력합니다
print(user1.name, user1.num_followers(), user1.num_following(), user1.followers_list)
print(user2.name, user2.num_followers(), user2.num_following(), user2.followers_list)
print(user3.name, user3.num_followers(), user3.num_following())
print(user4.name, user4.num_followers(), user4.num_following())

