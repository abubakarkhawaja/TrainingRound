from pandas.io.parsers import read_csv
from sourcecode.utilities import get_weather_files, get_weather_info, calendar


def weather_by_year_month_bar(path: str, date: str) -> None:
    """
    Visits all files and prints High Temperatures, Low Temperatures 
    of all days of requested Year/Month with visual bar (red for high
    and blue for low temperature seperated by line).

    @params
    :date str: Date entered by user as command line argument
    :path str: Contains path to weather files directory
    """
    weatherfile = get_weather_files(date, path)
    if weatherfile == []:
        print('No such record founnd')
    else:
        fullPath = path + weatherfile[0]
        weather_data = get_weather_info(fullPath)

        monthNumber = int(date.split('/')[1])
        month = calendar.month_name[monthNumber]
        year = date.split('/')[0]
        
        print(month,year)
        
        for weatherDayInfo in weather_data:
            if weatherDayInfo['PKT'] != "":
                weatherDate = weatherDayInfo['PKT'].split('-')[2]
 
            if weatherDayInfo['Max TemperatureC'] != "":
                highTemp = int(weatherDayInfo['Max TemperatureC'])
                highBar = "".join(['+'] * highTemp)
                print(weatherDate, f"\033[1;31;40m{highBar}", f"\033[1;;40m{highTemp}C")

            if weatherDayInfo['Max TemperatureC'] != "":
                lowTemp = int(weatherDayInfo['Min TemperatureC'])
                lowBar = "".join(['+'] * lowTemp)
                
                print(weatherDate, f"\033[1;34;40m{lowBar}", f"\033[1;;40m{lowTemp}C")
