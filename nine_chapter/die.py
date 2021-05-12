"""模拟掷骰子"""
from random import randint

class Die():
    """一次掷骰子"""

    def __init__(self, sides=6):
        """初始化骰子的属性"""
        self.sides = sides

    def roll_die(self):
        """打印随机数"""
        num = randint(1, self.sides)
        print("The random number is " + str(num))
