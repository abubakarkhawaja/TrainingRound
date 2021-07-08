from sourcecode.utilities import MONTHS,getWeatherDic, getWeatherFiles


def task1 (path,date):

    #Inititalization
    highest_temp = float('-inf')
    highest_temp_date = ""
    lowest_temp_date = ""
    lowest_temp = float('inf')
    humidity = float('-inf')
    humidity_date = ""

    # getting weatherfiles folder path
    # filtering only those with which are needed according to date
    weatherFiles = getWeatherFiles(date, path)     

    # traversing through all files of same year   
    for weatherfile in weatherFiles:
        # concating full path of a weatherfile
        PATH = path+weatherfile
        weather_data = getWeatherDic(PATH)

        # Inititalization
        max_temp =  float('-inf')
        max_temp_date = ""
        min_temp = float('inf')
        min_temp_date = ""
        max_humid =  float('-inf')
        max_humid_date = ""
        
        # vising all days in month inside weather file and finding min/max values
        for key in weather_data.keys():
            temp = int(weather_data[key]['Max TemperatureC'])
            if temp > max_temp:
                max_temp = temp
                # saving date
                month = MONTHS[int(key.split('-')[1])]
                day = key.split('-')[2]
                max_temp_date = month + " " + day
            
            temp = int (weather_data[key]['Min TemperatureC'])
            if temp < min_temp:
                min_temp = temp
                # saving date
                month = MONTHS[int(key.split('-')[1])]
                day = key.split('-')[2]
                min_temp_date = month + " " + day
            
            humid = int(weather_data[key]['Max Humidity'])
            if humid > max_humid:
                max_humid = humid
                # saving date
                month = MONTHS[int(key.split('-')[1])]
                day = key.split('-')[2]
                max_humid_date = month + " " + day

        # comparing base max/min values against max/min value of a month-year
        if highest_temp < max_temp:
            highest_temp = max_temp
            highest_temp_date =max_temp_date
        if lowest_temp > min_temp:
            lowest_temp = min_temp
            lowest_temp_date = min_temp_date
        if humidity < max_humid:
            humidity = max_humid
            humidity_date = max_humid_date
    
    # printing max/min value
    print ('Highest:', f'{highest_temp}C on',highest_temp_date)
    print('Lowest:', f'{lowest_temp}C on',lowest_temp_date)
    print('Humidity:', f'{humidity}% on',humidity_date)






