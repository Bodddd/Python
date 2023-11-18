from abc import ABC, abstractmethod

class Staff(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Employee(Staff):
    def __init__(self, name, salary, worked_days, bonus_percentage=0):
        self._name = name
        self._salary = salary
        self._worked_days = worked_days
        self._bonus_percentage = bonus_percentage

    def calculate_salary(self):
        return (self._salary / 30) * self._worked_days

    def calculate_bonus(self):
        return (self.calculate_salary() / 100) * self._bonus_percentage

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

class Manager(Employee):
    bonus_size = 100

    def __init__(self, name, salary, worked_days, num_subordinates, bonus_percentage=0):
        super().__init__(name, salary, worked_days, bonus_percentage)
        self._num_subordinates = num_subordinates

    def report(self):
        return f"Manager {self._name} manages {self._num_subordinates} employees."

    def calculate_bonus(self):
        return super().calculate_bonus() + self._num_subordinates * Manager.bonus_size

employees = [
    Employee("John", 3000, 20),
    Manager("Alice", 5000, 22, 5)
]

for emp in employees:
    print(f"{emp.name}'s Salary: {emp.calculate_salary()}, Bonus: {emp.calculate_bonus()}")
