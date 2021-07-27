import unittest

from sourcecode.weather_records_reader import WeatherRecordsReader

PATH = ['sourcecode/dummy_1998_Dec.txt']

class TestWeatherServices(unittest.TestCase):

    def test_weather_instance(self):
        for path in self.path:
            self.assertIsInstance(WeatherRecordsReader.get_weather_info(path), list)    

    def test_weather_files(self):
        self.assertIsInstance(WeatherRecordsReader.get_weather_files('1998/12', self.path), str)
        self.assertIsInstance(WeatherRecordsReader.get_weather_files('1998', self.path), list)
