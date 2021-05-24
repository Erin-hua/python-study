import requests
from operator import itemgetter
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行API调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
titles, submission_dicts = [], []
for submission_id in submission_ids[:30]:
    # 对于每篇文章，都执行一个API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
        str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
        'label': response_dict['title'],
        'xlink': 'http://news.ycombinator.com/item?id=' + str(submission_id),
        # 如果没有键descendants，则value对应的值是0
        'value': response_dict.get('descendants', 0)
        }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('value'),
                            reverse=True)

for submission_dict in submission_dicts:
    titles.append(submission_dict['label'])

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()
# 横坐标的标签顺时针旋转45度
my_config.x_label_rotation = 45
# show_legend=False隐藏图例，左上角的小方块
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 20
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000

chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most Popular Articles on Hacker News'
chart.x_labels = titles

chart.add('', submission_dicts)
chart.render_to_file('hn_submissions.svg')