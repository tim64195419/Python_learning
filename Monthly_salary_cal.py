from abc import ABCMeta, abstractmethod

class Employee(metaclass=ABCMeta):
    """員工(抽象類)"""

    def __init__(self, name):
        self.name = name

    @abstractmethod
    def get_salary(self):
        """結算月薪(抽象方法)"""
        pass

class Manager(Employee):
    """部門經理"""
    def get_salary(self):
        return 15000.0

class Programmer(Employee):
    def __init__(self, name, working_hour = 0):
        self.working_hour = working_hour
        super().__init__(name)

    def get_salary(self):
        return 200.0 * self.working_hour

class Saleman(Employee):
    """銷售員"""
    def __init__(self, name, sales=0.0):
        self.sales = sales
        super().__init__(name)

    def get_salary(self):
        return 1800.0 + self.sales * 0.05

class EmployeeFactory():
    """創建員工的工廠(工廠模式-通過工廠實現對象使用者和對象之間的解耦合)"""

    @staticmethod
    def create(em_type, *arg, **kwargs):
        """創建員工"""
        all_emp_types = {'M': Manager, 'P': Programmer, 'S': Saleman}
        cls = all_emp_types[em_type.upper()]
        print(cls)
        return cls(*arg, **kwargs) if cls else None


def main():
    """主函數"""
    emps = [
        EmployeeFactory.create('M', '曹操'),
        EmployeeFactory.create('P', '荀彧', 120),
        EmployeeFactory.create('P', '郭嘉', 85),
        EmployeeFactory.create('S', '典韦', 123000),
    ]
    for emp in emps:
        print(emp)
        print(f'{emp.name}: {emp.get_salary():.2f}元')

if __name__ == '__main__':
    main()

# 介紹Python之面向对象编程：封装、继承、多态
# https://blog.csdn.net/FloraCHY/article/details/78648257