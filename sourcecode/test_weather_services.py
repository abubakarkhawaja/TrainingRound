import unittest

from sourcecode.weather_services import WeatherMan

class TestWeatherServices(unittest.TestCase):
    path = 'sourcecode/'
    obj = WeatherMan()

    def test_get_weather_info(self):
        full_path = self.path + 'dummy_1998_Dec.txt'
        self.assertIsInstance(self.obj.get_weather_info(full_path), list)    

    def test_get_weather_files(self):
        self.assertIsInstance(self.obj.get_weather_files('1998/12', self.path), list)
