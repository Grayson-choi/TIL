class Post:
    # 게시글 클래스
    def __init__(self, date, content):
        # 게시글은 속성으로 올린 날짜와 내용을 문자열로 갖는다
        self.date = date
        self.content = content

    def __str__(self):
        # 게시글 문자열 메소드
        return "게시일: {}\n내용: {}".format(self.date, self.content)


class BlogUser:
    # 블로그 유저를 나타내는 클래스
    def __init__(self, name, status_message):
        """
        블로그 유저는 속성으로 이름, 상태 메시지와 게시글들을 갖는다
        게시글들(posts)은 빈 배열로 초기화한다
        """
        self.name = name
        self.status_message = status_message
        self.posts = []

    def add_post(self, date, content):
        # 새로운 게시글 추가
        new_post = Post(date, content)
        self.posts.append(new_post)

    def show_all_posts(self):
        # 블로그 유저의 모든 게시글 출력
        for post in self.posts:
            print(post)

    def __str__(self):
        # 간단한 인사와 상태 메시지 문자열을 리턴
        return "안녕하세요 {}입니다.{}\n".format(self.name, self.status_message)



# 테스트 코드
# 블로그 유저 인스턴스 생성
blog_user_1 = BlogUser("성태호", "친하게 지내요!")

# 블로그 유저 인스턴스 출력(인사, 이름, 상태 메시지)
print(blog_user_1)

# 블로그 유저 게시글 2 개 추가
blog_user_1.add_post("2019년 8월 30일", """
오늘은 내 생일이였다.
많은 사람들이 축하해줬다.
행복했다.
""")

blog_user_1.add_post("2019년 8월 31일", """
재밌는 코딩 교육 사이트를 찾았다.
코드잇이란 곳인데 최고다.
같이 공부하실 분들은 www.codeit.kr로 오세요!
""")

# 특정 블로그 유저의 모든 게시글 출력
blog_user_1.show_all_posts()