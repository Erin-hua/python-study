"""例题11.3-Employee类的测试代码"""
import unittest
from employee import Employee

class TestEmployee(unittest.TestCase):
    """测试Employee类"""

    def setUp(self):
        """创建雇员实例，便于测试"""
        self.my_employee = Employee("sakura", "erin", 3000)
        self.employee_name = self.my_employee.first_name + " " + self.my_employee.last_name

    def test_give_default(self):
        """测试默认增加年薪的情况"""
        self.my_employee.give_raise()
        print("\n默认增加" + self.employee_name + "的年薪后年薪是：" +
            str(self.my_employee.annual_pay))

    def test_give_custom_raise(self):
        """测试给定增加的年薪的参数的情况"""
        self.my_employee.give_raise(10000)
        print("\n给定增加的年薪后" + self.employee_name + "的年薪是：" +
            str(self.my_employee.annual_pay))

unittest.main()
