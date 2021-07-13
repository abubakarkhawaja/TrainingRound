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
    weather_file = get_weather_files(date, path)
    if weather_file == []:
        print('No such record founnd')
    else:
        full_path = path + weather_file[0]
        weather_data = get_weather_info(full_path)

        month_number = int(date.split('/')[1])
        month = calendar.month_name[month_number]
        year = date.split('/')[0]
        
        print(month, year)
        
        for weather_day_info in weather_data:
            if weather_day_info['PKT'] != "":
                weather_date = weather_day_info['PKT'].split('-')[2]
 
            if weather_day_info['Max TemperatureC'] != "":
                high_temp = int(weather_day_info['Max TemperatureC'])
                high_bar = "".join(['+'] * high_temp)
                print(weather_date, f"\033[1;31;40m{high_bar}", f"\033[1;;40m{high_temp}C")

            if weather_day_info['Max TemperatureC'] != "":
                low_temp = int(weather_day_info['Min TemperatureC'])
                low_bar = "".join(['+'] * low_temp)
                print(weather_date, f"\033[1;34;40m{low_bar}", f"\033[1;;40m{low_temp}C")
