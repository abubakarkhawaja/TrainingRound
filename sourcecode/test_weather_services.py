import unittest
from sourcecode.weather_services import WeatherMan

class TestWeatherServices(unittest.TestCase):

    path = '/Users/abubakarkhawaja/Documents/weatherfiles/'
    obj = WeatherMan()

    def test_get_weather_info(self):
        file_path = self.path + 'Murree_weather_2004_Aug.txt'
        
        self.assertIsInstance(self.obj.get_weather_info(file_path), list)    
        self.assertRaises(FileNotFoundError, self.get_weather_info, '')

    def test_get_weather_files(self):
        self.assertIsInstance(self.get_weather_files('2004/6', self.path), 
                            list)
        self.assertIsNone(self.get_weather_files('', ''))
