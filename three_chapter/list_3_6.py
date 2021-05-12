friends_names = ["huwenjiao","hujimei","zhaojiarong","luozhen"]
message = ", would you like to have dinner with me?"
print(friends_names[0]+message)
print(friends_names[1]+message)
print(friends_names[2]+message)
print(friends_names[3]+message)
print("friend "+friends_names[2]+" can not come")
friends_names[2]="jianglinyu"
print(friends_names[0]+message)
print(friends_names[1]+message)
print(friends_names[2]+message)
print(friends_names[3]+message)
print("I find a bigger dinner desk!")
friends_names.insert(0,"wang")
friends_names.insert(2,"qian")
friends_names.append("sun")
for name in friends_names:
    print(name+message)
