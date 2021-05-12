user_name = input("请输入你的姓名：")
file_path = "guest.txt"

with open(file_path, "w") as file_object:
    file_object.write(user_name + "\n")
