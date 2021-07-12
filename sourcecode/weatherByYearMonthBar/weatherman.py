from pandas.io.parsers import read_csv
from sourcecode.utilities import get_weather_files, get_weather_info, calendar


def weather_by_year_month_bar(path: str, date: str) -> None:
    """
    Visits all files and prints High Temperatures, Low Temperatures 
    of all days of requested Year/Month with visual bar (red for high
    and blue for low temperature seperated by line).

    Parameters:
        date (str): Date entered by user as command line argument
        path (str): Contains path to weather files directory
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
        
        for key in weather_data.keys():
            day = key.split('-')[2]
            if weather_data[key]['Max TemperatureC'] != "":
                highTemp = int(weather_data[key]['Max TemperatureC'])
                highBar = "".join(['+'] * highTemp)
                print(day, f"\033[1;31;40m{highBar}", f"\033[1;;40m{highTemp}C")

            if weather_data[key]['Max TemperatureC'] != "":
                lowTemp = int(weather_data[key]['Min TemperatureC'])
                lowBar = "".join(['+'] * lowTemp)
                
                print(day, f"\033[1;34;40m{lowBar}", f"\033[1;;40m{lowTemp}C")
