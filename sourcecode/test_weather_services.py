import unittest

from sourcecode.filehandling import FileHandling


class TestWeatherServices(unittest.TestCase):
    path = 'sourcecode/'
    test_report = FileHandling()

    def test_get_weather_info(self):
        full_path = self.path + 'dummy_1998_Dec.txt'
        self.assertIsInstance(self.test_report.get_weather_info(full_path), list)    

    def test_get_weather_files(self):
        self.assertIsInstance(self.test_report.get_weather_files('1998/12', self.path), list)
