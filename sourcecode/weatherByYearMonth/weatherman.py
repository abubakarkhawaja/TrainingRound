from sourcecode.utilities import get_Weather_Info, getWeatherFiles


def task2 (path,date):
    avg_highest_temp = float('-inf')
    avg_lowest_temp = float('inf')
    avg_mean_humidity = float('-inf')

    # acquiring file name of required weather file of specific month
    weatherfile = getWeatherFiles(date, path)        # [0] because only 1 file exist of specific month in whole year
    if weatherfile == []:
        print('No such record founnd')
    else:
        PATH = path+weatherfile[0]
        weather_data = get_Weather_Info(PATH)

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
