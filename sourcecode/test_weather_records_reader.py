import unittest

from .weather_records_reader import WeatherRecordsReader
from .weather_reports_display import fetch_weather_files

PATH = ['sourcecode/dummy_1998_Dec.txt']

class TestWeatherServices(unittest.TestCase):

    def test_weather_instance(self):
        for path in self.path:
            self.assertIsInstance(WeatherRecordsReader.read_weather_info(path), list)    

    def test_weather_files(self):
        self.assertIsInstance(fetch_weather_files('1998/12', self.path), str)
        self.assertIsInstance(fetch_weather_files('1998', self.path), list)
