##################################### ООП Python #####################################


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

########### Задание 2. Наследование ###########
# class Employee:
#     def __init__(self, name, position, salary): 
#         self.__name = name
#         self.__position = position
#         self.__salary = salary
#     def get_info(self):
#         return f"Name: {self.__name}, Position: {self.__position}, Salary: {self.__salary}"
        
# class Devoloper(Employee):
#     def __init__(self, name, salary, programming_language):
#         super().__init__(name, "Разработчик", salary)
#         self.__programming_language = programming_language
            
#     def get_programming_languages(self):
#         return self.__programming_language
        
# class Manager(Employee):
#     def __init__(self, name, salary):
#         super().__init__(name, "Менеджер", salary)
#         self.employees = []
        
#     def add_employee(self, employee):
#         if isinstance(employee, Employee):
#             self.employees.append(employee)
#         else:
#             raise TypeError("Можно тобавить только сотрудников")
#     def get_info(self):
#         info = ", ".join([emp.get_info() for emp in self.employees])
#         return f"{super().get_info()}, Employees: [{info}]"
            
# dev1 = Devoloper("Alice", 100000, "Python")
# dev2 = Devoloper("Bob", 120000, "Java")
# mgr = Manager("Charlie", 150000)

# mgr.add_employee(dev1)
# mgr.add_employee(dev2)

# print(dev1.get_info())
# print(dev2.get_info())
# print(mgr.get_info())
##############################################

########### Задание 3. Полиморфизм ###########

# class Shape:
#     def get_area(self):
#         return 0
#     def get_perimeter(self):
#         return 0
    
# class Reactangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
        
#     def get_area(self):
#         return self.width * self.height
    
#     def get_perimeter(self):
#         return 2 * (self.width + self.height)

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
        
#     def get_area(self):
#         return 3.14 * self.radius ** 2
    
#     def get_perimeter(self):
#         return 2 * 3.14 * self.radius
    
# width = 5
# height = 10
# radius = 7
# print(f"Площадь прямоугольника: {Reactangle(width, height).get_area()}")
# print(f"Периметр прямоугольника: {Reactangle(width, height).get_perimeter()}")
# print(f"Площадь круга: {Circle(radius).get_area()}")
# print(f"Периметр круга: {Circle(radius).get_perimeter()}")

##############################################

########### Задание 4. Абстракция и интерфейс ###########

# from abc import ABC, abstractmethod    
# class Transport(ABC):
#     @abstractmethod
#     def start_engine(self):
#         pass
#     @abstractmethod
#     def stop_engine(self):
#         pass
#     @abstractmethod
#     def move(self):
#         pass
# class Car(Transport):
#     def start_engine(self):
#         print("Двигатель автомобиля запущен")
        
#     def stop_engine(self):
#         print("Двигатель автомобиля остановлен")
        
#     def move(self):
#         print("Автомобиль движется")
# class Boat(Transport):
#     def start_engine(self):
#         print("Двигатель лодки запущен")
        
#     def stop_engine(self):
#         print("Двигатель лодки остановлен")
        
#     def move(self):
#         print("Лодка движется")
        
# def job_transport(transport: Transport):
#     transport.start_engine()
#     transport.move()
#     transport.stop_engine()
    
# car = Car()
# boat = Boat()

# job_transport(car)
# job_transport(boat)
##############################################

########### Задание 5. Множественное наследование ###########   
# class Flyable:
#     def fly(self):
#         print("I'm flying!")

# class Swimmable:
#     def swim(self):
#         print("I'm swimming!")

# class Duck(Flyable, Swimmable):
#     def make_sound(self):
#         print("Quack!")       
    
# donald = Duck()
# donald.fly()
# donald.swim()
# donald.make_sound()     
############################################## 

################################ Фишки ООП Python ##################################   


############################ Задание 1 #################################  
# class Logger:
#     _isinstance = None
#     _logs = []
    
#     def __new__(cls):
#         if cls._isinstance is None:
#             cls._isinstance = super(Logger, cls).__new__(cls)
#         return cls._isinstance
    
#     def log(self, message: str):
#         self._logs.append(message)
        
#     def get_logs(self):
#         return self._logs


# logger1 = Logger()
# logger2 = Logger()

# logger1.log("First message")
# logger2.log("Second message")

# assert logger1 is logger2, "Logger is not a singleton!"
# assert logger1.get_logs() == ["First message", "Second message"]

# print("Все работает корректно")

######################################################################## 

############################ Задание 2 #################################  

# class Report:
#     def __init__(self, title: str, content: str):
#         self.title = title
#         self.content = content

# class PDFGe

######################################################################## 

############################ Задание 3 #################################  

# from abc import ABC, abstractmethod

# class PaymentProcessor(ABC):
#     @abstractmethod
#     def process_payment(self, amount: float):
#         pass

# class PayPalProcessor(PaymentProcessor):
#     def __init__(self, email: str):
#         self.email = email
        
#     def process_payment(self, amount: float):
#         print(f"PayPal оплата {amount: .2f}Р через PayPal аккаунт {self.email}")
        

# class CreditCardProcessor(PaymentProcessor):
#     def __init__(self, card_number: str):
#         self.card_number = card_number

#     def process_payment(self, amount: float) -> None:
#         print(f"CreditCard Оплата {amount:.2f}₽ с карты: {self.card_number}")

        
# class CryptoProcessor(PaymentProcessor):
#     def __init__(self, wallet_address: str):
#         self.wallet_address = wallet_address
        
#     def process_payment(self, amount: float):
#         print(f"Crypto оплата {amount: .2f}Р через кошелек {self.wallet_address}")
        
# if __name__ == "__main__":
#     processors: list[PaymentProcessor] = [
#         PayPalProcessor("user@example.com"),
#         CreditCardProcessor("4111 1111 1111 1111"),
#         CryptoProcessor("0xABCDEF1234567890"),
#     ]

#     for processor in processors:
#         processor.process_payment(2500.00)

######################################################################## 