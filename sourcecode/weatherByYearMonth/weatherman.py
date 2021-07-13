from sourcecode.utilities import get_weather_files, get_weather_info


def weather_by_year_month(path: str, date: str) -> None:
    """
    Visits all files and prints Average of High Temperatures, 
    Average of Low Temperatures ,and Average of Mean Humidity 
    based on requested Year/Month.

    @params
    :date str: Date entered by user as command line argument
    :path str: Contains path to weather files directory
    """
    avg_highest_temp = float('-inf')
    avg_lowest_temp = float('inf')
    avg_mean_humidity = float('-inf')

    weather_file = get_weather_files(date, path)
    if weather_file == []:
        print('No such record founnd')
    else:
        full_path = path + weather_file[0]
        weather_data = get_weather_info(full_path)

        total_max_temp = 0
        total_min_temp = 0
        total_mean_humidity = 0
        
        for weather_day_info in weather_data:
            if weather_day_info['Max TemperatureC'] != "":
                total_max_temp += int(weather_day_info['Max TemperatureC'])
            
            if weather_day_info['Min TemperatureC'] != "":            
                total_min_temp += int (weather_day_info['Min TemperatureC'])
            
            if weather_day_info['Mean Humidity'] != "":
                total_mean_humidity += int(weather_day_info['Mean Humidity'])
        
        length = len(weather_data)
        avg_highest_temp = total_max_temp / length
        avg_lowest_temp = total_min_temp / length
        avg_mean_humidity = total_mean_humidity / length

        print (f'Highest Average: {round(avg_highest_temp)}C')
        print(f'Lowest Average: {round(avg_lowest_temp)}C')
        print(f'Average Mean Humidity: {round(avg_mean_humidity)}%')
