import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS 

def get_status_code(url):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError:
        return -1
    else:
        return r.status_code

def main():
    # 执行API调用并存储响应
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    status_code = get_status_code(url)
    if status_code != -1:
        print('Status code:', status_code)

        # 将API响应存储在一个字典变量中
        response_dict = r.json()
        print("Total repositories:", response_dict['total_count'])

        # 探索有关仓库的信息
        repo_dicts = response_dict['items']
        # print("Repositories returned:", len(repo_dicts))
        names, plot_dicts = [], []
        for repo_dict in repo_dicts:
            names.append(repo_dict['name'])
    
            plot_dict = {
                'value': repo_dict['stargazers_count'],
                'label': str(repo_dict['description']),
                'xlink': repo_dict['html_url'],
                }
            plot_dicts.append(plot_dict)

        # 可视化
        my_style = LS('#333366', base_style=LCS)
    
        my_config = pygal.Config()
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
        chart.title = 'Most-Starred Python Projects on GitHub'
        chart.x_labels = names
    
        chart.add('', plot_dicts)
        chart.render_to_file('python_repos.svg')
    else:
        print("Connection refused")
    
    # 17.1.5研究第一个仓库
    """repo_dict = repo_dicts[0]
    print("\nSelected information about first repository:")
    print('Name:', repo_dict['name'])
    # 键login获取所有者的登录名
    print('Owner:', repo_dict['owner']['login'])
    print('Stars:', repo_dict['stargazers_count'])
    print('Repository:', repo_dict['html_url'])
    print('Created:', repo_dict['created_at'])
    print('Updated:', repo_dict['updated_at'])
    print('Description:', repo_dict['description'])"""

    # 17.1.6
    """print("\nSelected information about each repository:")
    for repo_dict in repo_dicts:
        print('\nName:', repo_dict['name'])
        print('Owner:', repo_dict['owner']['login'])
        print('Stars:', repo_dict['stargazers_count'])
        print('Repository:', repo_dict['html_url'])
        print('Description:', repo_dict['description'])"""

if __name__ == '__main__':
    main()
