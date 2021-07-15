import unittest

from sourcecode.weather_records_reader import WeatherRecordsReader


class TestWeatherServices(unittest.TestCase):
    path = ['sourcecode/dummy_1998_Dec.txt']

    def test_get_weather_info(self):
        # full_path = self.path + 'dummy_1998_Dec.txt'
        for path in self.path:
            self.assertIsInstance(WeatherRecordsReader.get_weather_info(path), list)    

    def test_get_weather_files(self):
        self.assertIsInstance(WeatherRecordsReader.get_weather_files('1998/12', self.path), str)
        self.assertIsInstance(WeatherRecordsReader.get_weather_files('1998', self.path), list)
