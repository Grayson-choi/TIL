class Counter:
    """
    시계 클래스의 시,분,초 요소로 사용될 카운터 클래스
    """

    def __init__(self, limit):
        self.value = 0
        self.limit = limit
        
        """
        인스턴스 변수 limit(카운터 제한), value(카운터 값)을 지정해준다.
        인스턴스 변수 limit만 파라미터로 받을 값을 지정하고, value는 초기값을 0으로 지정한다.
        """
        
        # 코드를 쓰세요!

    def set(self, new_value):
        if new_value > 0 or new_value <= self.limit:
            self.value = new_value
        else:
            self.value = 0
        """
        파라미터가 0 이상, 제한 값(limit) 이하면 카운터 값(value)에 지정해준다.
        아닐 경우 value에 0을 지정한다.
        """
        # 코드를 쓰세요!

    def reset(self):
        self.set(0)
        """
        카운터의 값 value에 0를 지정해준다
        """
        # 코드를 쓰세요!

    def tick(self):
        self.value += 1
        if self.value == self.limit:
            self.value = 0
            return True
        else:
            return False
        """카운터 인스턴스의 값을 1 증가시켜준다.
        카운터의 값 value가 인스턴스의 제한 값 limit에 도달하면 value를 0으로 바꾼 뒤 True를 리턴한다.
        value가 limit에 미치지 못했을 경우 False를 리턴한다.
        """
        # 코드를 쓰세요!

    def __str__(self):
        """
        문자열 매소드: 카운터 값 value를 최소 두 자릿수 문자열로 리턴한다.
        예) 만약 value라 1이면 "01"을 리턴하고 두 자릿수 이상이면 value를 그대로 문자열로 변환해서 리턴한다.
        """
        return str(self.value).zfill(2)



# 테스팅 코드

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



class Clock:
    """
    시계 클래스
    """
    HOURS = 24 # 총 시간
    MINUTES = 60 # 총 분
    SECONDS = 60 # 총 초

    def __init__(self, hour, minute, second):
        """
        각각 시, 분, 초를 나타내는 카운터 클래스를 3개를 갖는다.

        현재 시간을 파라미터들 hour시, minute분, second초로 지정한다.
        """
        # 코드를 쓰세요
        self.hour = Counter(Clock.HOURS)
        self.minute = Counter(Clock.MINUTES)
        self.second = Counter(Clock.SECONDS)

        self.set(hour, minute, second)

    def set(self, hour, minute, second):
        """현재 시간을 파라미터 hour시, minute분, second초로 설정한다."""
        # 코드를 쓰세요
        self.hour.set(hour)
        self.minute.set(minute)
        self.second.set(second)

    def tick(self):
        """
        초 카운터의 값을 1만큼 증가시킨다.
        초 카운터를 증가 시킴으로써, 분 또는 시도 바뀌어야되는 경우를 처리한다.
        """
        # 코드를 쓰세요
        if self.second.tick():
            if self.minute.tick():
                self.hour.tick()


    def __str__(self):
        """
        문자열 매소드: 현재 시간을 시간:분:초로 리턴한다. 시간, 분, 초는 각각 2자리수이다.
        예시: "03:11:02"
        """
        # 코드를 쓰세요
        return "{}:{}:{}".format(self.hour, self.minute, self.second)



# 테스트 코드

# 초가 60이 넘을 때 분이 늘어나는지 확인하기
clock = Clock(1, 30, 48)

# 13초를 늘린다
for i in range(13):
    clock.tick()
    print(clock)

# 분이 60이 넘을 때 시간이 늘어나는지 확인
clock.set(2, 3, 58)

# 5초를 늘린다
for i in range(5):
    clock.tick()
    print(clock)

# 시간이 24가 넘을 때 00:00:00으로 넘어가는 지 확인
clock.set(23, 59, 57)

# 5초를 늘린다
for i in range(5):
    clock.tick()
    print(clock)
