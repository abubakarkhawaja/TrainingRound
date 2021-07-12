import unittest
from utilities import get_weather_info, get_weather_files

class TestUtilites(unittest.TestCase):

    def test_get_weather_info(self):
        filePath = '/Users/abubakarkhawaja/Documents/weatherfiles/Murree_weather_2004_Aug.txt'

        self.assertIsInstance(get_weather_info(filePath), dict)    
        
        self.assertRaises(FileNotFoundError,get_weather_info,'')

    def test_get_weather_files(self):
        directoryPath = '/Users/abubakarkhawaja/Documents/weatherfiles/'
        self.assertIsInstance(get_weather_files('2004/6', directoryPath), list)

        self.assertIsNone(get_weather_files('',''))
