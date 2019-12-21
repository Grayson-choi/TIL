# def is_palindrome(word):
#     for left in range(len(word) // 2):
#         # 한 쌍이라도 일치하지 않으면 바로 False를 리턴하고 함수를 끝냄
#         right = len(word) - left - 1
#         if word[left] != word[right]:
#             return False

#     # for문에서 나왔다면 모든 쌍이 일치
#     return True

# def is_palindrome(word):
#     # 코드를 입력하세요.
#     for i in range(int(len(word) / 2)):
#         left = word[i]
#         right = word[len(word) - i - 1]
#         if left != right:
#             return False
#     return True

def is_palindrome(word):
    # 코드를 입력하세요.
    for i in range(int(len(word) // 2)):
        if word[i] != word[len(word) - i - 1]:
            i += 1
            if word[i] == word[len(word) - i - 1]:
                return True
            else:
                return False


print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))