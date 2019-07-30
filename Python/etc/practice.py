def some_of_range(start, end):
    if start == end:
        return start

    return end + some_of_range(start, end - 1)


print(some_of_range(2, 10)) # 출력: 54
print(some_of_range(11, 16)) # 출력: 81
print(some_of_range(1, 5)) # 출력: 15


def calorie_of_today(stairs, step):
    calorie = stairs * 0.11 + step * 0.033
    return calorie

print(calorie_of_today(97,8000))
print(calorie_of_today(300,6000))

def find_number(num_list):
    over_50_list = []
    # 이곳에 코드를 작성하세요.
    for i in num_list:
        if i > 50:
            over_50_list.append(i)
    return over_50_list
            
print(find_number([3, 14, 57, 200, 87, 34]))
print(find_number([33, 314, 7, 10, 47, 74]))

    
    answer = list.sort()
    print(answer[1])
    
print(second_number())
print(second_number([-1, 3, 45, 78, 12, 56]))
print(second_number([1]))


[3, 14, 57, 200, 87, 34].sort()


def rock_paper_Scissors(jiwoong,taeho):
    if jiwoong == taeho:
        return "Draw"
    if jiwoong == "가위":
        if taeho == "바위":
            return "Lose"
        else:
            return "Win"
    if jiwoong == "바위":
        if taeho == "보":
            return  "Lose"
        else:
            return "Win"
    if jiwoong == "보":
        if taeho == "가위":
            return  "Lose"
        else:
            return "Win"
    

print(rock_paper_Scissors("가위","바위"))
print(rock_paper_Scissors("바위","바위"))
print(rock_paper_Scissors("보","바위"))
