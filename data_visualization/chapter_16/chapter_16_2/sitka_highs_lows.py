import csv
from matplotlib import pyplot as plt
from datetime import datetime

# 从文件中读取日期、最高气温和最低气温
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # 此时阅读器对象已经指向了第二行

    dates, highs, lows = [], [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low =int(row[3])
        except ValueError:
            # 打印错误消息，指出确实数据的日期之后循环接着处理下一行
            print(current_date, 'missing data')
        else:
            #dates.append(current_date)
            highs.append(high)
            lows.append(low)
    
    # print(highs)

# 根据数据绘制图形
# 设置绘图窗口的分辨率（适合自己电脑的分辨率）和尺寸
fig = plt.figure(dpi=80, figsize=(10, 6))
# plot方法用于画折线，此处画了最高气温和最低气温折线图
# 参数alpha指定颜色的透明度,0表示完全透明，1表示完全不透明
#plt.plot(dates, highs, c='red', alpha=0.5)
#plt.plot(dates, lows, c='blue', alpha=0.5)
plt.plot(highs, c='red', alpha=0.5)
plt.plot(lows, c='blue', alpha=0.5)
# facecoloe指定填充区域的颜色
#plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)
#plt.fill_between(highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
title = "Daily high and low temperatures - 2014\nStika"
plt.title(title, fontsize=20)
# 设置标签和字体的大小
plt.xlabel('', fontsize=16)
# 绘制斜的日期标签
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=16)
# 设置每个坐标轴的取值范围
plt.axis([0, 366, 10, 120])

plt.show()