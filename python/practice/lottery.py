from random import randint

# 무작위로 정렬된 1 - 45 사이의 숫자 여섯개 뽑기


def generate_numbers():
    number = []
    while len(number) < 6:
        random_number = randint(1, 45)
        if random_number in number:
            continue
        else:
            number.append(random_number)
    number.sort()
    return number


# 보너스까지 포함해 7개 숫자 뽑기
# 정렬된 6개의 당첨 번호와 1개의 보너스 번호 리스트를 리턴
# 예: [1, 7, 13, 23, 31, 41, 15]
def draw_winning_numbers():
    win = generate_numbers()
    while len(win) < 7:
        bonus = randint(1, 45)
        if bonus in win:
            continue
        else:
            win.append(bonus)
    return win


# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
# 두 리스트에서 중복되는 숫자가 몇개인지 구하기
def count_matching_numbers(list1, list2):
    count = 0
    print(list1)
    print(list2)
    for i in range(len(list1)):
        if list1[i] in list2:
            count = count + 1
    return count


# 로또 등수 확인하기
def check(numbers, winning_numbers):
    prize = 0
    #일반 번호 뽑아내기
    general_nubmer = winning_numbers[0:6]
    #확인
    if count_matching_numbers(numbers, winning_numbers) == 6 and numbers == general_nubmer:
        prize = 1000000000
    elif count_matching_numbers(numbers, winning_numbers) == 6:
        prize = 50000000
    elif count_matching_numbers(numbers, winning_numbers) == 5 and numbers == general_nubmer:
        prize = 1000000
    elif count_matching_numbers(numbers, winning_numbers) == 4 and numbers == general_nubmer:
        prize = 50000
    elif count_matching_numbers(numbers, winning_numbers) == 3 and numbers == general_nubmer:
        prize = 5000
    return prize