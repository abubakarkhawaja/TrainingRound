import unittest
from utilities import get_weather_info, get_weather_files

class TestUtilites(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Will run at start of unittesting this class"""
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Will run at end of unittesting this class"""
        print('\ntearDownClass')

    def setUp(self):
        """Will run before every testcase"""
        print('\nsetUp')
        self.filePath = '/Users/abubakarkhawaja/Documents/weatherfiles/Murree_weather_2004_Aug.txt'
        self.directoryPath = '/Users/abubakarkhawaja/Documents/weatherfiles/'
        
    def tearDown(self) -> None:
        """Will run after every testcase"""
        print('tearDown\n')

    def test_get_weather_info(self) -> None:
        self.assertIsInstance(get_weather_info(self.filePath), dict)    
        
        self.assertRaises(FileNotFoundError,get_weather_info,'')
        print('test_get_weather_info')

    def test_get_weather_files(self) -> None:
        self.assertIsInstance(get_weather_files('2004/6', self.directoryPath), list)

        self.assertIsNone(get_weather_files('',''))
        print('test_get_weather_files')
