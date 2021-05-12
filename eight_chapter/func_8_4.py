def make_shirt(size, sample="I love Python"):
    print("The size of T-shirt is " + size + ", sample is " + sample)

# 默认字样的大号T恤
make_shirt("big")

# 默认字样的中号T恤
make_shirt(size="medium")

# 印有其他字样的T恤
make_shirt(sample="Hello", size="small")
