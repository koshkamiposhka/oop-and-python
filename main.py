########### Задание 1. Инкапсуляция ###########

# class BankAccount:
#     def __init__(self, balance=0):
#         self.__balances = balance
        
#     def deposit(self, summa):
#         if summa > 0:
#             self.__balances += summa
#         else:
#             raise ValueError("Сумма пополнения должна быть положительной")
        
#     def withdraw(self, summa):
#         if self.__balances < summa:
#             raise ValueError("Недостаточно средств на счете")
#         elif summa <= 0:
#             raise ValueError("Сумма снятия должна быть положительной")
#         else:
#             self.__balances -= summa
#     def get_balance(self):
#         return self.__balances

# acc = BankAccount(1000)
# acc.deposit(500)
# print(acc.get_balance())

# acc.withdraw(200)
# print(acc.get_balance())
# print(hasattr(acc, '__balance'))
###############################################


