# imported os to get list of file names in directory
import os
from codeFiles.utilities import MONTHS,getWeatherDic, getWeatherFiles

def task1 (path,date):
    highest_temp = float('-inf')
    highest_temp_date = ""
    lowest_temp_date = ""
    lowest_temp = float('inf')
    humidity = float('-inf')
    humidity_date = ""

    directory = os.listdir(path)
    weatherFiles = getWeatherFiles(date, directory)        
    for weatherfile in weatherFiles:
        PATH = path+weatherfile
        weather_data = getWeatherDic(PATH)

        max_temp =  float('-inf')
        max_temp_date = ""
        min_temp = float('inf')
        min_temp_date = ""
        max_humid =  float('-inf')
        max_humid_date = ""
        
        for key in weather_data.keys():
            temp = int(weather_data[key]['Max TemperatureC'])
            if temp > max_temp:
                max_temp = temp
                
                month = MONTHS[int(key.split('-')[1])]
                day = key.split('-')[2]
                max_temp_date = month + " " + day
            
            temp = int (weather_data[key]['Min TemperatureC'])
            if temp < min_temp:
                min_temp = temp
                month = MONTHS[int(key.split('-')[1])]
                day = key.split('-')[2]
                min_temp_date = month + " " + day
            
            humid = int(weather_data[key]['Max Humidity'])
            if humid > max_humid:
                max_humid = humid
                month = MONTHS[int(key.split('-')[1])]
                day = key.split('-')[2]
                max_humid_date = month + " " + day

        if highest_temp < max_temp:
            highest_temp = max_temp
            highest_temp_date =max_temp_date
        if lowest_temp > min_temp:
            lowest_temp = min_temp
            lowest_temp_date = min_temp_date
        if humidity < max_humid:
            humidity = max_humid
            humidity_date = max_humid_date
    
    print ('Highest:', f'{highest_temp}C on',highest_temp_date)
    print('Lowest:', f'{lowest_temp}C on',lowest_temp_date)
    print('Humidity:', f'{humidity}% on',humidity_date)






