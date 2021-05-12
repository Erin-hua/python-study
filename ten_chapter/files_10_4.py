file_path = "guest_book.txt"

active = True
with open(file_path, "a") as file_object:
    while active:
        user_name = input("请输入你的名字：")
        if user_name != "q":
            hello = "Hello, " + user_name.title() + "!"
            file_object.write(hello + "\n")
        else:
            active = False
            print("输入结束！")
            break;
