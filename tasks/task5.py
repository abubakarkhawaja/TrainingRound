# imported os to get list of file names in directory
import os
from tasks.utilities import MONTHS, getWeatherDic, getWeatherFiles


def task5(path,date):
    directory = os.listdir(path)
    weatherfile = getWeatherFiles(date, directory)[0]        
    PATH = path+weatherfile
    weather_data = getWeatherDic(PATH)

    month = MONTHS[int(date.split('/')[1])]
    year = date.split('/')[0]
    
    print(month,year)
    
    for key in weather_data.keys():
        highTemp = int(weather_data[key]['Max TemperatureC'])
        lowTemp = int(weather_data[key]['Min TemperatureC'])

        #creating bar
        highBar = "".join(['+']*highTemp)
        lowBar = "".join(['+']*lowTemp)

        """
        The ANSI escape code will set the text colour to bright green. The format is;
        \033[  Escape code, this is always the same
        1 = Style, 1 for normal.
        31 = Text colour, 31 for red, 34 for blue.
        40m = Background colour, 40 is for black.
        """
        day = key.split('-')[2]
        print(day,f"\033[;34;40m{lowBar} \033[;31;40m{highBar}",f"\033[;;40m{lowTemp}C - \033[;;40m{highTemp}C")
    






