def make_shirt(size, sample):
    print("The size of T-shirt is " + size + ", sample is " + sample)

# 传递位置实参
make_shirt("small", "python")

# 传递关键字实参
make_shirt(sample="c", size="big")
