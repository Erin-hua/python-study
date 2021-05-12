import matplotlib.pyplot as plt

from random_walk import RandomWalk

# 只要程序处于活动状态，就不断地模拟随机漫步
while True:
    # 创建一个RandomWalk实例，并将其包含的点都绘制出来
    rw = RandomWalk()
    rw.fill_walk()

    # 设置绘图窗口的尺寸,dpi是分辨率
    plt.figure(dpi=100, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, c='blue', linewidth=1)

    # 突出起点和终点
    plt.plot(0, 0, c='green', marker='^', markersize=10)
    plt.plot(rw.x_values[-1], rw.y_values[-1], c='red', marker='^', markersize=10)

    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    plt.show()

    keep_running = input("Make another walk?(y/n): ")
    if keep_running == 'n':
        break