
class Counter:
    """
    시계 클래스의 시,분,초 하나씩을 나타내는데 사용될 카운터 클래스
    """

    def __init__(self, limit):
        """
        인스턴스 변수 limit(최대값), value(현재까지 카운트한 값)을 지정해준다.
        인스턴스를 생성할 때 인스턴스 변수 limit만 파라미터로 받고, value는 초기값 0으로 지정한다.
        """
        # 코드를 쓰세요
        self.limit = limit
        self.value = 0

    def set(self, new_value):
        """
        파라미터가 0 이상, 최댓값 미만이면 value에 지정해준다.
        아닐 경우 value에 0을 지정한다.
        """
        # 코드를 쓰세요!
        self.value = new_value if 0 <= new_value < self.limit else 0

    def tick(self):
        """value를 1 증가시킨다.
        카운터의 값 value가 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit보다 작은 경우 False를 리턴한다.
        """
        # 코드를 쓰세요!
        self.value += 1
        if self.value == self.limit:
            self.value = 0
            return True
        else:
            return False

    def __str__(self):
        """
        문자열 메소드: value를 최소 두 자릿수 문자열로 리턴한다.
        예) 만약 value가 1이면 "01"을 리턴하고 두 자릿수 이상이면 value를 그대로 문자열로 변환해서 리턴한다.
        """
        return str(self.value).zfill(2)


# 제한 값 30까지 셀 수 있는 카운터 인스턴스 생성
counter = Counter(30)

# 0부터 10까지 센다
for i in range(10):
    counter.tick()
print(counter)

# 타이머를 리셋시킨다
counter.reset()

print(counter)

# 카운터 값 27로 설정
counter.set(27)

# 카운터 값이 30이 넘어가면 0으로 바뀌는지 확인
for i in range(5):
    counter.tick()
print(counter)