from pandas.io.parsers import read_csv
from sourcecode.utilities import get_Weather_Info, getWeatherFiles, calendar


def task3 (path,date):
    # acquiring file name of required weather file of specific month
    weatherfile = getWeatherFiles(date, path)
    if weatherfile == []:
        print('No such record founnd')
    else:
        fullPath = path+weatherfile[0]        # [0] because only 1 file exist of specific month in whole year
        weather_data = get_Weather_Info(fullPath)

        # converting numerical month to alphabetical month with help of MONTHS list
        monthNumber = int(date.split('/')[1])
        month = calendar.month_name[monthNumber]
        year = date.split('/')[0]
        
        print(month,year)
        
        for key in weather_data.keys():
            highTemp = int(weather_data[key]['Max TemperatureC'])
            lowTemp = int(weather_data[key]['Min TemperatureC'])

            # creating bar by mulitplying elements of list with total temperature value and then joining as string 
            # => giving total signs required with no spaces
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
            print(day,f"\033[;31;40m{highBar}",f"\033[;;40m{highTemp}C")
            print(day,f"\033[;34;40m{lowBar}",f"\033[;;40m{lowTemp}C")
