"""例题17.3测试代码"""
import unittest
from python_repos import get_status_code

class PythonReposTestCase(unittest.TestCase):
    """测试python_repos.py中的函数"""

    def test_get_status_code(self):
        """测试get_status_code函数"""
        url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        status_code = get_status_code(url)
        self.assertEqual(status_code, 200)

unittest.main()