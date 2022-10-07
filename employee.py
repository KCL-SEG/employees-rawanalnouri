"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""
from abc import ABC, abstractmethod

'''Commission classes'''

class Commission(ABC):
    @abstractmethod
    def get_commission_pay(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
   

class Bonus_Commission(Commission):
    def __init__(self, bonus):
        self.bonus = bonus
    
    def get_commission_pay(self):
        return self.bonus
    
    def __str__(self):
        return f"a bonus commission of {self.bonus}"


class Contract_Commission(Commission):
    def __init__(self, number_of_contracts, pay_per_contract):
        self.number_of_contracts = number_of_contracts
        self.pay_per_contract = pay_per_contract
    
    def get_commission_pay(self):
        return (self.number_of_contracts * self.pay_per_contract)
    
    def __str__(self):
        return f"a commission for {self.number_of_contracts} contract(s) at {self.pay_per_contract}/contract"


'''Employee classes'''

class Employee(ABC):
    def __init__(self, name, commission=None):
        self.name = name
        self.commission = commission

    @abstractmethod
    def get_pay(self):
        pass
    
    def receives_commission(self):
        return (self.commission is not None)

    def add_commission(self, commission):
        self.commission = commission

    def __str__(self):
        return f"Their total pay is {self.get_pay()}."


class Salary_Contract_Employee(Employee):
    def __init__(self, name, monthly_salary, commission=None):
        super().__init__(name, commission)
        self.monthly_salary = monthly_salary
    
    def get_pay(self):
        if super().receives_commission():
            commission_pay = self.commission.get_commission_pay() 
            return self.monthly_salary + commission_pay
        else:
            return self.monthly_salary
    
    def __str__(self):
        str = f"{self.name} works on a monthly salary of {self.monthly_salary}"
        if super().receives_commission():
            str += " and receives " + self.commission.__str__()
        return str + ".  " + super().__str__()


class Hourly_Contract_Employee(Employee):
    def __init__(self, name, hourly_salary, number_of_hours, commission=None):
        super().__init__(name, commission)
        self.hourly_salary = hourly_salary
        self.number_of_hours = number_of_hours
    
    def get_pay(self):
        pay = self.number_of_hours * self.hourly_salary
        if super().receives_commission():
            commission_pay = self.commission.get_commission_pay()
            return pay + commission_pay
        else:
            return pay
    
    def __str__(self):
        str = f"{self.name} works on a contract of {self.number_of_hours} hours at {self.hourly_salary}/hour"
        if super().receives_commission():
            str += " and receives " + self.commission.__str__()
        return str + ".  " + super().__str__()


'''Test'''
# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Salary_Contract_Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Hourly_Contract_Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Salary_Contract_Employee('Renee', 3000)
renee.add_commission(Contract_Commission(4, 200))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Hourly_Contract_Employee('Jan', 25, 150)
jan.add_commission(Contract_Commission(3, 220))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Salary_Contract_Employee('Robbie', 2000)
robbie.add_commission(Bonus_Commission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Hourly_Contract_Employee('Ariel', 30, 120)
ariel.add_commission(Bonus_Commission(600))
