import matplotlib.pyplot as plt

# 绘制前5个整数的立方图
x_values = [1, 2, 3, 4, 5]
y_values = [x**3 for x in x_values]

# 设置参数
plt.scatter(x_values, y_values, c=(0, 0.8, 0), edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Cubic Graph", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()

# 显示前5000个整数的立方,关闭第一个图后显示第二个图
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]

# 设置参数
plt.scatter(x_values, y_values, c=(0, 0.8, 0), edgecolors='none', s=40)

# 设置图表标题并给坐标轴加上标签
plt.title("Cubic Graph", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cube of Value", fontsize=14)

# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)

plt.show()
