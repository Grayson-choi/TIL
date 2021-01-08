class MessageNotificationManager:
    """메시지 알림 기능을 담당 클래스"""
    def __init__(self):
        self.message_notifications = []

    def add_new_message(self, new_message):
        """새로온 메시지 추가"""
        self.message_notifications.append(new_message)

    def display_message_notifications(self):
        """모든 새로온 메시지 확인"""
        print("새로 온 메시지들:")

        for message in self.message_notifications:
            print(message.short_message() + "\n")


class KakaoTalkMessage:
    """카카오톡 메시지 클래스"""
    notification_message_max_len = 10

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def short_message(self):
        """메시지를 짧은 형태로 리턴함"""
        message_str = "{}\n{}\n".format(self.time, self.sent_by)
        message_str += self.content if len(self.content) <= KakaoTalkMessage.notification_message_max_len else self.content[:KakaoTalkMessage.notification_message_max_len] + "..."

        return message_str


class TextMessage:
    """문자 메시지 클래스"""
    notification_message_max_len = 12

    def __init__(self, sent_by, time, content):
        self.sent_by = sent_by
        self.time = time
        self.content = content

    def notification_string(self):
        """메시지를 짧은 형태로 리턴함"""
        noti_string = "{}, {}\n".format(self.sent_by, self.time)
        noti_string += self.content if len(self.content) <= TextMessage.notification_message_max_len else self.content[:TextMessage.notification_message_max_len] + "..."
        return noti_string


# 메시지 알림 관리 인스턴스 생성
message_notification_manager = MessageNotificationManager()

# 카카오톡 메시지 세 개 생성
kakao_talk_message_1 = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 30분", "나 오늘 놀러 못갈 거 같애 미안!")
kakao_talk_message_2 = KakaoTalkMessage("고대위", "2019년 7월 1일 오후 11시 35분", "아니다 갈게 너네 어디서 놀고 있어?")
kakao_talk_message_3 = KakaoTalkMessage("이영훈", "2019년 7월 2일 오전 12시 30분", "나도 놀러 갈게 나 지금 출발")

# 카카오톡 메시지 알림 관리 인스턴스에 추가
message_notification_manager.add_new_message(kakao_talk_message_1)
message_notification_manager.add_new_message(kakao_talk_message_2)
message_notification_manager.add_new_message(kakao_talk_message_3)

# 메시지 알림 관리 인스턴스에 있는 모든 메시지 출력
message_notification_manager.display_message_notifications()


