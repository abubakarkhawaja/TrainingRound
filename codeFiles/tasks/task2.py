# imported os to get list of file names in directory
from codeFiles.utilities import getWeatherDic, getWeatherFiles
import os

def task2 (path,date):
    avg_highest_temp = float('-inf')
    avg_lowest_temp = float('inf')
    avg_mean_humidity = float('-inf')

    directory = os.listdir(path)
    weatherfile = getWeatherFiles(date, directory)[0]        
    PATH = path+weatherfile
    weather_data = getWeatherDic(PATH)

    total_max_temp = 0
    total_min_temp = 0
    total_mean_humidity = 0
    
    for key in weather_data.keys():
        total_max_temp += int(weather_data[key]['Max TemperatureC'])            
        total_min_temp += int (weather_data[key]['Min TemperatureC'])
        total_mean_humidity += int(weather_data[key]['Mean Humidity'])
    
    length = len(weather_data)
    avg_highest_temp = total_max_temp/length
    avg_lowest_temp = total_min_temp/length
    avg_mean_humidity = total_mean_humidity/length
    print (f'Highest Average: {round(avg_highest_temp)}C')
    print(f'Lowest Average:', f'{round(avg_lowest_temp)}C')
    print(f'Average Mean Humidity: {round(avg_mean_humidity)}%')






