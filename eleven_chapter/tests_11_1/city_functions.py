"""例题11.1-返回城市名和国家名的函数"""

def city_country(city_name, country_name):
    """返回城市名和国家名组成的字符串"""
    city_country_name = city_name.title() + ", " + country_name.title()
    return city_country_name
