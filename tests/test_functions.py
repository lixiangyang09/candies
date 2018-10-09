import unittest
from candies.functions import *


class TestFunction(unittest.TestCase):
    def test_dict_to_xml(self):
        data = {'a': 12, 'bb': 32}
        res = dict_to_xml(data)
        print(res)
