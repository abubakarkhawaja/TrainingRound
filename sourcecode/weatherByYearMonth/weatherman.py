from sourcecode.utilities import get_Weather_Files, get_Weather_Info


def task2 (path: str, date: str):
    """
    Summary:
        Visits all files and prints Average of High Temperatures, 
        Average of Low Temperatures ,and Average of Mean Humidity 
        based on requested Year/Month.

    Args:
        date (str): Date entered by user as command line argument
        path (str): Contains path to weather files directory
    """
    avg_highest_temp = float('-inf')
    avg_lowest_temp = float('inf')
    avg_mean_humidity = float('-inf')

    # acquiring file name of required weather file of specific month
    weatherfile = get_Weather_Files(date, path)        # [0] because only 1 file exist of specific month in whole year
    if weatherfile == []:
        print('No such record founnd')
    else:
        fullPath = path+weatherfile[0]
        weather_data = get_Weather_Info(fullPath)

        # inititalization
        total_max_temp = 0
        total_min_temp = 0
        total_mean_humidity = 0
        
        # calculating total max/min in month
        for key in weather_data.keys():
            total_max_temp += int(weather_data[key]['Max TemperatureC'])            
            total_min_temp += int (weather_data[key]['Min TemperatureC'])
            total_mean_humidity += int(weather_data[key]['Mean Humidity'])
        
        # calculating average
        length = len(weather_data)
        avg_highest_temp = total_max_temp/length
        avg_lowest_temp = total_min_temp/length
        avg_mean_humidity = total_mean_humidity/length

        # priniting values
        print (f'Highest Average: {round(avg_highest_temp)}C')
        print(f'Lowest Average:', f'{round(avg_lowest_temp)}C')
        print(f'Average Mean Humidity: {round(avg_mean_humidity)}%')
