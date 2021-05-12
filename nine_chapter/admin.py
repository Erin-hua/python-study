"""权限、管理员类"""
from user import User

class Privileges():
    """存储权限"""

    def __init__(self):
        """初始化权限"""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",       
            ]

    def show_privileges(self):
        """显示权限"""
        print("The Administrater have some privileges:")
        for privilege in self.privileges:
            print("-" + privilege)


class Admin(User):
    """管理员类"""

    def __init__(self, first_name, last_name, gender, age):
        """初始化管理员的属性"""
        super().__init__(first_name, last_name, gender, age)
        self.privileges = Privileges()