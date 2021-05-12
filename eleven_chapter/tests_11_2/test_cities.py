"""例题11.2-测试代码"""
import unittest
from city_functions import city_country

class CityFunctionsTestCase(unittest.TestCase):
    """测试city_functions.py中的函数"""

    def test_city_country(self):
        """测试city_country函数只有城市名和国家名参数时的情况"""
        city_country_name = city_country("santiago", "chile")
        self.assertEqual(city_country_name, "Santiago, Chile")

    def test_city_country_population(self):
        """测试city_country函数有城市名、国家名和人口参数时的情况"""
        city_country_population = city_country("santiago", "chile", 5000000)
        self.assertEqual(city_country_population, "Santiago, Chile - population 5000000")

unittest.main()
