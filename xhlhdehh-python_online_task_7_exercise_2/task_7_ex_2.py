"""
Task 7_2
Create classes Employee, SalesPerson, Manager and Company with predefined functionality.

Create basic class Employee and declare following content:
• Attributes – `name` (str), `salary` and `bonus` (int), set with property decorator
• Constructor - parameters `name` and `salary`
• Method `bonus` - sets bonuses to salary, amount of which is delegated as `bonus`
• Method `to_pay` - returns the value of summarized salary and bonus.

Create class SalesPerson as class Employee inheritor and declare within it:
• Constructor with parameters: `name`, `salary`, `percent` – percent of plan performance (int, without the % symbol), first two of which are passed from basic class constructor
• Redefine method of parent class `bonus` in the following way: if the sales person completed the plan more than 100%, their bonus is doubled (is multiplied by 2), and if more than 200% - bonus is tripled (is multiplied by 3)

Create class Manager as Employee class inheritor, and declare within it:
• Constructor with parameters: `name`, `salary` and `client_number` (int, number of served clients), first two of which are passed to basic class constructor.
• Redefine method of parent class `bonus` in the following way: if the manager served over 100 clients, their bonus is increased by 500, and if more than 150 clients – by 1000.

Create class Company and declare within it:
• Constructor with parameters: `employees` – list of company`s employees (made up of Employee/SalesPerson/Manager classes instances) with arbitrary length `n`
• Method `give_everybody_bonus` with parameter company_bonus (int) that sets the amount of basic bonus for each employee.
• Method `total_to_pay` that returns total amount of salary of all employees including awarded bonus
• Method `name_max_salary` that returns name of the employee, who received maximum salary including bonus.

Note:
Class attributes and methods should bear exactly the same names as those given in task description
Methods should return only target values, without detailed explanation within `return`
"""


class Employee:
    def __init__(self, name, salary):
        if isinstance(name, str):
            self.__name = name
        else:
            raise TypeError
        if isinstance(salary, int):
            self.__salary = salary
        else:
            raise TypeError
        self.__bonus = 0
        
    @property
    def salary(self):
        return self.__salary
    
    @property
    def name(self):
        return self.__name
    
    @property
    def bonus(self):
        return self.__bonus
    
    @bonus.setter
    def bonus(self, bonus):
        if type(bonus) is int:
            self.__bonus = bonus
        else:
            raise TypeError
    
    def _setbonus(self, bonus):
        self.__bonus = bonus
        
    def to_pay(self):
        return self.__salary + self.__bonus


class SalesPerson(Employee):
    def __init__(self, name, salary, percent):
        super().__init__(name, salary)
        if type(percent) is int:
            self.__percent = percent
        else:
            raise TypeError
    
    @property
    def bonus(self):
        return super().bonus
    
    @bonus.setter
    def bonus(self, bonus):
        #raise RuntimeError("S" + str(bonus))
        super()._setbonus(bonus)
        if self.bonus != 0:
            if self.__percent >= 200:
                super()._setbonus(super().bonus * 3)
            elif self.__percent >= 100:
                super()._setbonus(super().bonus * 2)


class Manager(Employee):
    def __init__(self, name, salary, client_number):
        super().__init__(name, salary)
        if type(client_number) is int:
            self.__client_number = client_number
        else:
            raise TypeError
            
    @property
    def bonus(self):
        return super().bonus
    
    @bonus.setter
    def bonus(self, bonus):
        #raise RuntimeError("M" + str(bonus))
        #print(dir(super()))
        super()._setbonus(bonus)
        if self.bonus != 0:
            if self.__client_number >= 150:
                super()._setbonus(super().bonus + 1000)
            elif self.__client_number >= 100:
                super()._setbonus(super().bonus + 500)


class Company:
    def __init__(self, employees=[], n=0):
        if len(employees) != n:
            raise ValueError
        for employee in employees:
            if not isinstance(employee, Employee):
                raise ValueError
        self.__employees = employees
        self.employees = employees

    def give_everybody_bonus(self, company_bonus):
        if type(company_bonus) is not int:
            raise TypeError
        if company_bonus <= 0:
            raise ValueError
        for employee in self.employees:
            employee.bonus(company_bonus)
    
    def total_to_pay(self):
        total = 0
        for employee in self.employees:
            total += employee.to_pay()
        return total
            
    def name_max_salary(self):
        max_ = 0
        name = ''
        for employee in self.employees:
            if employee.to_pay() > max_:
                max_ = employee.to_pay()
                name = employee.name
        return name
    
    
# a = []
# a.append(Employee('Andy', 1500))
# a.append(Manager('Liza', 200, 300))
# a.append(SalesPerson('Jim', 250, 500))
# c = Company(a, 3)