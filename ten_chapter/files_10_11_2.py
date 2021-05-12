import json

file_path = "favorite_number.json"

try:
    with open(file_path) as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    print("文件" + file_path + "不存在。")
else:
    print("I know your favorite number! It's " + number)
