file_path = "learning_python.txt"

with open(file_path) as file_object:
    for line in file_object:
        line.replace("Python", "C")
        print(line.strip())

