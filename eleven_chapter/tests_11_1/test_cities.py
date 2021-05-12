"""例题11.1-测试代码"""
import unittest
from city_functions import city_country

class CityFunctionsTestCase(unittest.TestCase):
    """测试city_functions.py中的函数"""

    def test_city_country(self):
        """测试city_country函数"""
        city_country_name = city_country("santiago", "chile")
        self.assertEqual(city_country_name, "Santiago, Chile")

unittest.main()
