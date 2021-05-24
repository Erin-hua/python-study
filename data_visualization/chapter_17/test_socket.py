import requests
import time

url = 'https://bbs.csdn.net/topics/391929842'
try:
    r = requests.get(url)
except requests.exceptions.ConnectionError:
    time_sleep = 0

    while True:
        time.sleep(1) # 自己随便定义多少秒
        try:
            r = requests.get(url)
        except requests.exceptions.ConnectionError:
            time_sleep = time_sleep + 1

            if time_sleep == 10:
                print("Your Internet connect error!!")
                break

            else:
                print("max connect try: " + str(time_sleep) + ", error")
                break