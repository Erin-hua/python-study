"""例题11.2-返回城市名、国家名和人口数的函数"""

def city_country(city_name, country_name, population=""):
    """返回城市名、国家名和人口数组成的字符串"""
    if population:
        city_country_name = city_name.title() + ", " + country_name.title() + " - " + "population " + str(population)
    else:
        city_country_name = city_name.title() + ", " + country_name.title()
    return city_country_name
