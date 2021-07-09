from sourcecode.utilities import get_Weather_Info, getWeatherFiles, calendar


def task1 (path: str, date: str):
    """
    Summary:
        Visits all files and prints Highest Temperature, Lowest Temperature
        and Humidity based on comparising months of requested Year.

    Args:
        date (str): Date entered by user as command line argument
        path (str): Contains path to weather files directory
    """
    #Inititalization
    highest_temp = float('-inf')
    highest_temp_date = ""
    lowest_temp_date = ""
    lowest_temp = float('inf')
    humidity = float('-inf')
    humidity_date = ""

    # getting files name list
    weatherFiles = getWeatherFiles(date, path)     

    # traversing through all files of same year   
    for weatherfile in weatherFiles:
        # concating full path of a weatherfile
        fullPath = path+weatherfile
        weather_data = get_Weather_Info(fullPath)

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
                monthNumber = int(key.split('-')[1])
                month = calendar.month_name[monthNumber]
                day = key.split('-')[2]
                max_temp_date = month + " " + day
            
            temp = int (weather_data[key]['Min TemperatureC'])
            if temp < min_temp:
                min_temp = temp
                # saving date
                monthNumber = int(key.split('-')[1])
                month = calendar.month_name[monthNumber]
                day = key.split('-')[2]
                min_temp_date = month + " " + day
            
            humid = int(weather_data[key]['Max Humidity'])
            if humid > max_humid:
                max_humid = humid
                # saving date
                monthNumber = int(key.split('-')[1])
                month = calendar.month_name[monthNumber]
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
    print (f'Highest: {highest_temp}C on {highest_temp_date}')
    print(f'Lowest: {lowest_temp}C on {lowest_temp_date}')
    print(f'Humidity: {humidity}% on {humidity_date}')
