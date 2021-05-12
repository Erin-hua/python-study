def make_album(singer, album_name, num=""):
    dic = {"singer_name": singer, "album_name": album_name}
    if num:
        dic["num"] = num

    return dic

dic_one = make_album("Alice", "World")
print("The album belongs to " + dic_one["singer_name"] + ", the name is " + dic_one["album_name"])
dic_two = make_album("Zhao", "Jia")
print("The album belongs to " + dic_two["singer_name"] + ", the name is " + dic_two["album_name"])
dic_three = make_album("SUn", "Yu")
print("The album belongs to " + dic_three["singer_name"] + ", the name is " + dic_three["album_name"])
dic_four = make_album("Hu", "One", num=15)
print("The album belongs to " + dic_four["singer_name"] + ", the name is " + dic_four["album_name"] + ", the number is " + str(dic_four["num"]))
