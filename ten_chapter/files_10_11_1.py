import json

num = input("请输入你喜欢的数字：")

file_path = "favorite_number.json"
with open(file_path, "w") as file_object:
    json.dump(num, file_object)
