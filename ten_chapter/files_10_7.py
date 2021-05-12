while True:
    try:
        num_1 = int(input("输入第一个数字："))
    except ValueError:
        print("第一个数不应该输入文本，而是数字！")
    else:
        try:
            num_2 = int(input("输入第二个数字："))
        except ValueError:
            print("第二个数不应该输入文本，而是数字！")
        else:
            count = num_1 + num_2
            print("两个数的和是：" + str(count))
