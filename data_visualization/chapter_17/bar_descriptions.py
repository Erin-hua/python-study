import pygal

from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

chart.title = 'Python Projects'
chart.x_labels = ['system-design-primer', 'public-apis', 'Python']

plot_dicts = [
    {'value': 132419, 'label': 'Description of system-design-primer.'},
    {'value': 125056, 'label': 'Description of public-apis.'},
    {'value': 108081, 'label': 'Description of Python.'},
    ]

# add函数只会接受字符串和列表作为参数
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg') 