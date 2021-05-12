"""例题11.3 雇员"""

class Employee():
    """存储雇员的信息并对信息进行修改等操作"""

    def __init__(self, first_name, last_name, annual_pay):
        """初始化雇员的信息"""
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.annual_pay = annual_pay

    def give_raise(self, raise_pay = 5000):
        """增加年薪"""
        self.annual_pay += raise_pay
