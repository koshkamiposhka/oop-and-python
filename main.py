##################################### ООП Python #####################################

# ---------------------- Задание 1. Инкапсуляция ----------------------
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            raise ValueError("Сумма пополнения должна быть положительной")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной")
        if self.__balance < amount:
            raise ValueError("Недостаточно средств на счете")
        self.__balance -= amount

    def get_balance(self):
        return self.__balance


acc = BankAccount(1000)
acc.deposit(500)
print(acc.get_balance())

acc.withdraw(200)
print(acc.get_balance())

# ---------------------- Задание 2. Наследование ----------------------
class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary

    def get_info(self):
        return f"Name: {self.__name}, Position: {self.__position}, Salary: {self.__salary}"


class Developer(Employee):
    def __init__(self, name, salary, programming_language):
        super().__init__(name, "Разработчик", salary)
        self.__programming_language = programming_language

    def get_programming_language(self):
        return self.__programming_language


class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, "Менеджер", salary)
        self.employees = []

    def add_employee(self, employee):
        if isinstance(employee, Employee):
            self.employees.append(employee)
        else:
            raise TypeError("Можно добавлять только сотрудников")

    def get_info(self):
        info = "\n    ".join(emp.get_info() for emp in self.employees)
        return f"{super().get_info()}, Employees:\n    {info}"


dev1 = Developer("Alice", 100000, "Python")
dev2 = Developer("Bob", 120000, "Java")
mgr = Manager("Charlie", 150000)

mgr.add_employee(dev1)
mgr.add_employee(dev2)

print(dev1.get_info())
print(dev2.get_info())
print(mgr.get_info())

# ---------------------- Задание 3. Полиморфизм ----------------------
import math


class Shape:
    def get_area(self):
        return 0

    def get_perimeter(self):
        return 0


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.radius


rect = Rectangle(5, 10)
circle = Circle(7)

print(f"Площадь прямоугольника: {rect.get_area()}")
print(f"Периметр прямоугольника: {rect.get_perimeter()}")
print(f"Площадь круга: {circle.get_area()}")
print(f"Периметр круга: {circle.get_perimeter()}")

# ---------------------- Задание 4. Абстракция ----------------------
from abc import ABC, abstractmethod


class Transport(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass


class Car(Transport):
    def start_engine(self):
        print("Двигатель автомобиля запущен")

    def stop_engine(self):
        print("Двигатель автомобиля остановлен")

    def move(self):
        print("Автомобиль движется")


class Boat(Transport):
    def start_engine(self):
        print("Двигатель лодки запущен")

    def stop_engine(self):
        print("Двигатель лодки остановлен")

    def move(self):
        print("Лодка движется")


def job_transport(transport: Transport):
    transport.start_engine()
    transport.move()
    transport.stop_engine()


car = Car()
boat = Boat()

job_transport(car)
job_transport(boat)

# ---------------------- Задание 5. Множественное наследование ----------------------
class Flyable:
    def fly(self):
        print("I'm flying!")


class Swimmable:
    def swim(self):
        print("I'm swimming!")


class Duck(Flyable, Swimmable):
    def make_sound(self):
        print("Quack!")


donald = Duck()
donald.fly()
donald.swim()
donald.make_sound()

################################ Фишки ООП Python ##################################

# ---------------------- Singleton ----------------------
class Logger:
    _instance = None
    _logs = []

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Logger, cls).__new__(cls)
        return cls._instance

    def log(self, message: str):
        self._logs.append(message)

    def get_logs(self):
        return self._logs


logger1 = Logger()
logger2 = Logger()

logger1.log("First message")
logger2.log("Second message")

assert logger1 is logger2, "Logger is not a singleton!"
assert logger1.get_logs() == ["First message", "Second message"]

print("Singleton работает корректно")

# ---------------------- Платежные процессоры ----------------------
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass


class PayPalProcessor(PaymentProcessor):
    def __init__(self, email: str):
        self.email = email

    def process_payment(self, amount: float):
        print(f"PayPal оплата {amount:.2f}₽ через PayPal аккаунт {self.email}")


class CreditCardProcessor(PaymentProcessor):
    def __init__(self, card_number: str):
        self.card_number = card_number

    def process_payment(self, amount: float):
        print(f"CreditCard оплата {amount:.2f}₽ с карты: {self.card_number}")


class CryptoProcessor(PaymentProcessor):
    def __init__(self, wallet_address: str):
        self.wallet_address = wallet_address

    def process_payment(self, amount: float):
        print(f"Crypto оплата {amount:.2f}₽ через кошелек {self.wallet_address}")


processors: list[PaymentProcessor] = [
    PayPalProcessor("user@example.com"),
    CreditCardProcessor("4111 1111 1111 1111"),
    CryptoProcessor("0xABCDEF1234567890"),
]

for processor in processors:
    processor.process_payment(2500.00)

# ---------------------- Птицы ----------------------
class Bird:
    def fly(self):
        print("I'm flying!")


class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")


class Penguin(Bird):
    def fly(self):
        print("Penguin is swimming")


def birds_fly(bird: Bird):
    bird.fly()


sparrow = Sparrow()
penguin = Penguin()

birds_fly(sparrow)
birds_fly(penguin)

# ---------------------- Абстрактные способности ----------------------
class FlyableAbstract(ABC):
    @abstractmethod
    def fly(self):
        pass


class Runnable(ABC):
    @abstractmethod
    def run(self):
        pass


class SwimmableAbstract(ABC):
    @abstractmethod
    def swim(self):
        pass


class Lion(Runnable):
    def run(self):
        print("Lion is running")


lion = Lion()
lion.run()

# ---------------------- Температура ----------------------
class Temperature:
    def __init__(self, celsius: float):
        self.celsius = celsius

    @classmethod
    def from_fahrenheit(cls, fahrenheit: float):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)

    @property
    def kelvins(self):
        return self.celsius + 273.15

    @staticmethod
    def is_freezing(temp: float):
        return temp <= 0


t1 = Temperature(25)
print(t1.kelvins)
