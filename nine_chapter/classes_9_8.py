class User():
    """存储用户的信息"""

    def __init__(self, first_name, last_name, gender, age):
        """初始化用户的属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        self.age = age

    def describe_user(self):
        """打印用户的信息"""
        print("The user's first name is " + self.first_name.title() +
            ", last name is " + self.last_name.title() + ", gender is " +
            self.gender + ", age is " + str(self.age))

    def greet_user(self):
        """打印个性化信息"""
        print("Hello, " + self.first_name.title() + " " + 
            self.last_name.title() + "!")


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



admin = Admin("erin", "sakura", "femal", 19) 
admin.privileges.show_privileges()
