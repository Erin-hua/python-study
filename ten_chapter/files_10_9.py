def file_not_found(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.readlines()
    except FileNotFoundError:
        # print("Can not find the file " + filename)
        pass
    else:
        for name in contents:
            print(name.strip())
        print("------")

file_names = ["cats.txt", "dogs.txt"]
for file_name in file_names:
    file_not_found(file_name)

