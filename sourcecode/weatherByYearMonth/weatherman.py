from sourcecode.utilities import get_weather_files, get_weather_info


def weather_by_year_month(path: str, date: str) -> None:
    """
    Visits all files and prints Average of High Temperatures, 
    Average of Low Temperatures ,and Average of Mean Humidity 
    based on requested Year/Month.

    Parameters:
        date (str): Date entered by user as command line argument
        path (str): Contains path to weather files directory
    """
    avg_highest_temp = float('-inf')
    avg_lowest_temp = float('inf')
    avg_mean_humidity = float('-inf')

    weatherfile = get_weather_files(date, path)
    if weatherfile == []:
        print('No such record founnd')
    else:
        fullPath = path + weatherfile[0]
        weather_data = get_weather_info(fullPath)

        total_max_temp = 0
        total_min_temp = 0
        total_mean_humidity = 0
        
        for key in weather_data.keys():
            if weather_data[key]['Max TemperatureC'] != "":
                total_max_temp += int(weather_data[key]['Max TemperatureC'])
            if weather_data[key]['Min TemperatureC'] != "":            
                total_min_temp += int (weather_data[key]['Min TemperatureC'])
            if weather_data[key]['Mean Humidity'] != "":
                total_mean_humidity += int(weather_data[key]['Mean Humidity'])
        
        length = len(weather_data)
        avg_highest_temp = total_max_temp / length
        avg_lowest_temp = total_min_temp / length
        avg_mean_humidity = total_mean_humidity / length

        print (f'Highest Average: {round(avg_highest_temp)}C')
        print(f'Lowest Average:', f'{round(avg_lowest_temp)}C')
        print(f'Average Mean Humidity: {round(avg_mean_humidity)}%')
