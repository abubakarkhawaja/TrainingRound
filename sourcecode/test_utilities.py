import unittest
from utilities import get_Weather_Info, get_Weather_Files

class TestUtilites(unittest.TestCase):

    def test_get_Weather_Info(self):
        filePath = '/Users/abubakarkhawaja/Documents/weatherfiles/Murree_weather_2004_Aug.txt'
        self.assertIsInstance(get_Weather_Info(filePath), dict)    
        self.assertIsNone(get_Weather_Info(''))

    def test_get_Weather_Files(self):
        directoryPath = '/Users/abubakarkhawaja/Documents/weatherfiles/'
        self.assertIsInstance(get_Weather_Files('2004/6', directoryPath), list)
        self.assertIsNone(get_Weather_Files('',''))



"""
    with this no need to write command like >> python -m unittest [filename]
    use instead:
    python [filename] 
"""
if __name__ == "__main__":
    unittest.main()