import json

def sort_number():
    """得到喜欢的数字并存储到json文件中"""
    try:
        num = int(input("请输入你喜欢的数字："))
    except ValueError:
        print("请输入数字而不是文本！")
        return False
    else:
        file_path = "favorite_number.json"
        with open(file_path, "w") as file_object:
            json.dump(num, file_object)
        return True

def get_number():
    """得到喜欢的数字"""
    file_path = "favorite_number.json"
    try:
        with open(file_path) as file_object:
            number = json.load(file_object)
    except FileNotFoundError:
        print("文件" + file_path + "不存在。")
        return None
    else:
        return number

num = get_number()
# 没有存储喜欢的数字就先存储，有喜欢的数字就输出
if num: 
    print("我知道了你最喜欢的数字是：" + str(num))
else:
    result = sort_number()
    while result == False:
        result = sort_number()