from codeFiles.utilities import MONTHS,getWeatherDic, getWeatherFiles


def task5(path,date):
    # getting weatherfiles folder path
    # filtering only those with which are needed according to date
    weatherfile = getWeatherFiles(date, path)[0]        
    PATH = path+weatherfile
    weather_data = getWeatherDic(PATH)

    month = MONTHS[int(date.split('/')[1])]
    year = date.split('/')[0]
    
    print(month,year)
    
    for key in weather_data.keys():
        # getting high and low temperature
        highTemp = int(weather_data[key]['Max TemperatureC'])
        lowTemp = int(weather_data[key]['Min TemperatureC'])

        #creating bar
        highBar = "".join(['+']*highTemp)
        lowBar = "".join(['+']*lowTemp)

        # As weather data keys are acutal date '2011-09-03'. So, getting days from it.
        day = key.split('-')[2]

        """
            The ANSI escape code will set the text colour to bright green. The format is;
            \033[  Escape code, this is always the same
            1 = Style, 1 for normal.
            31 = Text colour, 31 for red, 34 for blue.
            40m = Background colour, 40 is for black.
        """
        print(day,f"\033[;34;40m{lowBar}\033[;31;40m{highBar}",f"\033[;;40m{lowTemp}C - \033[;;40m{highTemp}C")
    






