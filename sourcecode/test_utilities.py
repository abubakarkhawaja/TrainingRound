import unittest
from utilities import get_weather_info, get_weather_files


class TestUtilites(unittest.TestCase):

    path = '/Users/abubakarkhawaja/Documents/weatherfiles/'

    def test_get_weather_info(self):
        file_path = self.path + 'Murree_weather_2004_Aug.txt'
        
        self.assertIsInstance(get_weather_info(file_path), list)    
        self.assertRaises(FileNotFoundError,get_weather_info,'')

    def test_get_weather_files(self):
        self.assertIsInstance(get_weather_files('2004/6', self.path), list)
        self.assertIsNone(get_weather_files('',''))
