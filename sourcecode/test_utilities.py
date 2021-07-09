import unittest
from utilities import get_Weather_Info, get_Weather_Files

class TestUtilites(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        """Will run at start of unittesting this class"""
        print('setUpClass')
    
    @classmethod
    def tearDownClass(cls) -> None:
        """Will run at end of unittesting this class"""
        print('tearDownClass')

    def setUp(self):
        """Will run before every testcase"""
        print('setUp')
        self.filePath = '/Users/abubakarkhawaja/Documents/weatherfiles/Murree_weather_2004_Aug.txt'
        self.directoryPath = '/Users/abubakarkhawaja/Documents/weatherfiles/'
        
    def tearDown(self):
        """Will run after every testcase"""
        print('tearDown\n')

    def test_get_Weather_Info(self):
        self.assertIsInstance(get_Weather_Info(self.filePath), dict)    

        self.assertIsNone(get_Weather_Info(''))
        print('test_get_Weather_Info')

    def test_get_Weather_Files(self):
        self.assertIsInstance(get_Weather_Files('2004/6', self.directoryPath), list)

        self.assertIsNone(get_Weather_Files('',''))
        print('test_get_Weather_Files')



"""
    with this no need to write command like >> python -m unittest [filename]
    use instead:
    python [filename] 
"""
if __name__ == "__main__":
    unittest.main()