MONTHS = ['','January','February','March','April','May','June','July','August','September','October','November','December']
MON = ['','Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
def getWeatherDic (PATH):
    weather_data = {}
    column = []

    with open(PATH) as file:

        flag = True
        for content in file.readlines():
            # condtion to read column names
            if flag:
                column = content.split(',')
                flag = False
            else:        
                # from 1 because dont want to read columns again s
                for i in range(1, len(content)):
                    # takinng values of first lines
                    column_data = content.split(',')
                    if column_data[1] == "":
                        continue

                    # using date as key for dictionary
                    weather_data[column_data[0]] = {}
            
                    for k in range(len(column)):
                        # saving values in their respective column according to date
                        key = column[k].strip()
                        weather_data[column_data[0]][key] = content.split(',')[k].strip()
    return weather_data
    
    
# imported os to get list of file names in directory
import os

def getWeatherFiles(date, path):
    directory = os.listdir(path)
    if '/' in date:
        month = MON[int(date.split('/')[1])]
        year = date.split('/')[0]
        weatherFiles = [dir for dir in directory if year in dir and month in dir]        
    else: 
        weatherFiles = [dir for dir in directory if date in dir]
    return weatherFiles