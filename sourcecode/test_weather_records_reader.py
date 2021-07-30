import unittest

from .weather_records_reader import WeatherRecordsReader
from .weather_reports_display import fetch_weather_files

PATH = ['sourcecode/dummy_1998_Dec.txt']

class TestWeatherServices(unittest.TestCase):
    weather_reader = WeatherRecordsReader(PATH) 
    def test_weather_instance(self):
        self.assertIsInstance(self.weather_reader.weathers_record, dict)    
