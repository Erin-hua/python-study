file_path = "learning_python.txt"

"""第一次打印"""
with open(file_path) as file_object:
    print(file_object.read().strip())
print("------")

"""第二次打印"""
with open(file_path) as file_object:
    for line in file_object:
        print(line.strip())
print("------")

"""第三次打印"""
with open(file_path) as file_object:
    file_text = file_object.readlines()

for text in file_text:
    print(text.strip())
print("------")
