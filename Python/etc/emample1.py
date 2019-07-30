def rock_paper_scissors(user1, user2):
    if user1 == user2:
        return "Draw"
    elif user1 == "가위":
        if user2 == "바위":
            return "Lose"
        else:
            return "Win"
    elif user1 == "바위":
        if user2 == "보":
            return "Lose"
        else:
            return "Win"
    elif user1 == "보":
        if user2 == "가위":
            return  "Lose"
        else:
            return "Win"
    
print(rock_paper_scissors("가위","바위"))
print(rock_paper_scissors("바위","바위"))
print(rock_paper_scissors("보","바위"))





