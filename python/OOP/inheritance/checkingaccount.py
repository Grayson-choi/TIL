# class CheckingAccount:
#     """자유 출입금 계좌 클래스"""
#     def __init__(self, name, password, balance, max_spending):
#         """생성자 매소드: 모든 인스턴스 변수의 초기값을 설정해준다"""
#         self.name = name
#         self.password = password
#         self.balance = balance
#         self.max_spending = max_spending

#     def withdraw(self, amount):
#         """돈을 출금한다"""
#         self.balance -= amount

#     def deposit(self, amount):
#         """돈을 입금한다"""
#         self.balance += amount

#     def check_card_use(self, amount):
#         """한 회 사용 한도 초과 이하인 금액 체크 카드 결제시 예치금을 줄여준다"""
#         if amount < self.max_spending:
#                 self.balance -= amount
#         else:
#                 print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))

#     def __str__(self):
#         """문자열 메소드"""
#             return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)
    



# class SavingsAccount:
#     """저축 계좌 클래스"""
#     def __init__(self, name, password, balance, interest_rate):
#         """생성자 매소드: 모든 인스턴스 변수의 초기값을 설정해준다"""
#         self.name = name
#         self.password = password
#         self.balance = balance
#         self.interest_rate = interest_rate

#     def withdraw(self, amount):
#         """돈을 출금한다"""
#         self.balance -= amount

#     def deposit(self, amount):
#         """돈을 입금한다"""
#         self.balance += amount

#     def add_interest(self):
#         """이자를 더해준다"""
#         self.balance *= self.interest_rate

#     def __str__(self):
#         """문자열 메소드"""
#         return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount
    # 코드를 쓰세요 

    def __str__(self):
        return "{}님의 계좌 예치금은 {}원입니다".format(self.name, self.balance)

class CheckingAccount(BankAccount):
    def __init__(self, name, balance, max_spending):
        super().__init__(name, balance)
        self.max_spending = max_spending

    def check_card_use(self, amount):
        """한 회 사용 한도 초과 이하인 금액 체크 카드 결제시 예치금을 줄여준다"""
        if amount < self.max_spending:
                self.balance -= amount
        else:
                print("{}님의 체크 카드는 한 회 {} 초과 사용 불가능합니다".format(self.name, self.max_spending))
    # 코드를 쓰세요

class SavingsAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance)
        self.interest_rate = interest_rate
    # 코드를 쓰세요
    def add_interest(self):
        """이자를 더해준다"""
        self.balance *= self.interest_rate


bank_account_1 = CheckingAccount("성태호", 100000, 10000)
bank_account_2 = SavingsAccount("강영훈", 20000, 1.05)

bank_account_1.withdraw(1000)
bank_account_1.deposit(1000)
bank_account_1.check_card_use(2000)

bank_account_2.withdraw(1000)
bank_account_2.deposit(1000)
bank_account_2.add_interest()

print(bank_account_1)
print(bank_account_2)

bank_accounts = {}

while True:
    user_input = input("메뉴은 계좌 개설, 계좌 조회, 입금, 출금, 종료입니다. \n")
    name = user_input
    interest_rate = 1.5


    if user_input == "계좌 개설":
        user_input = input("이름, 체크or적금, 입금액을 입력하세요.\n\n")
        name = user_input.split(",")[0]
        account_type = user_input.split(",")[1]
        balance = int(user_input.split(",")[2])
        
        if account_type == "체크":
            user_input = input("한도액을 입력하세요")
            limit = user_input
            bank_accounts[name] = CheckingAccount(name, balance, limit)
        else:
            bank_accounts[name] = SavingsAccount(name, balance, interest_rate)


    elif user_input == "계좌 조회":
        print(bank_accounts.keys())
        # for key in bank_accounts:
        #     print(key, end=', ')
        # print()
        user_input = input("이름을 입력하세요.\n\n")
        name = user_input
        print(bank_accounts[name])

    elif user_input == "입금":
        user_input = input("이름,입금액을 입력하세요.\n\n")
        name = user_input.split(",")[0]
        money = int(user_input.split(",")[1])
        bank_accounts[name].deposit(money)
        print(bank_accounts[name].balance , bank_accounts[name].balance)
        break

    elif user_input == "출금":
        user_input = input("이름,출금액을 입력하세요.\n\n")
        name = user_input.split(",")[0]
        money = int(user_input.split(",")[1])
        bank_accounts[name].withdraw(money)
        print(bank_accounts[name].balance , bank_accounts[name].balance)
    
    elif user_input == "종료":
        print("프로그램이 종료됩니다.")
        break
    else:
        print("메뉴은 계좌 개설, 계좌 조회, 입금, 출금, 종료입니다.\n\n")
