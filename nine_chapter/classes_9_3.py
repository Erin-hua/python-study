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


one = User("erin", "sakura", "femal", 19) 
one.describe_user()
one.greet_user()

two = User("hua", "wang", "femal", 23)
two.describe_user()
two.greet_user()

three = User("jiao", "zhao", "male", 25) 
three.describe_user()
three.greet_user()
