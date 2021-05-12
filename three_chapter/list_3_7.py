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
print("I can only invite two friends.")
sorry=", I am sorry that I can not invite you."
s_name=friends_names.pop()
print(s_name+sorry)
s_name=friends_names.pop()
print(s_name+sorry)
s_name=friends_names.pop()
print(s_name+sorry)
s_name=friends_names.pop()
print(s_name+sorry)
s_name=friends_names.pop()
print(s_name+sorry)
ok=", you can have dinner with me."
s_name=friends_names[0]
print(s_name+ok)
s_name=friends_names[1]
print(s_name+ok)
del friends_names[1]
del friends_names[0]
print(friends_names)