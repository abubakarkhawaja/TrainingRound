from sourcecode.utilities import get_weather_files, get_weather_info, calendar


def weather_by_year(path: str, date: str) -> None:
    """
    Visits all files and prints Highest Temperature, Lowest Temperature
    and Humidity based on comparising months of requested Year.

    @params
    :date str: Date entered by user as command line argument
    :path str: Contains path to weather files directory
    """
    highest_temp = float('-inf')
    highest_temp_date = ""
    lowest_temp_date = ""
    lowest_temp = float('inf')
    humidity = float('-inf')
    humidity_date = ""

    weatherFiles = get_weather_files(date, path)     
    if not weatherFiles:
        print('No Weather Date for these date.')
    else:
        for weatherfile in weatherFiles:
            fullPath = path + weatherfile
            weather_data = get_weather_info(fullPath)

            max_temp =  float('-inf')
            max_temp_date = ""
            min_temp = float('inf')
            min_temp_date = ""
            max_humid =  float('-inf')
            max_humid_date = ""
            
            for weatherDayInfo in weather_data:
                if weatherDayInfo['PKT'] != "":
                    weatherDate = weatherDayInfo['PKT']

                if weatherDayInfo['Max TemperatureC'] != "":
                    temperature = int(weatherDayInfo['Max TemperatureC'])
                    if temperature > max_temp:
                        max_temp = temperature
                        monthNumber = int(weatherDate.split('-')[1])
                        month = calendar.month_name[monthNumber]
                        day = weatherDate.split('-')[2]
                        max_temp_date = month + " " + day
                
                if weatherDayInfo['Min TemperatureC'] != "":            
                    temperature = int (weatherDayInfo['Min TemperatureC'])
                    if temperature < min_temp:
                        min_temp = temperature
                        monthNumber = int(weatherDate.split('-')[1])
                        month = calendar.month_name[monthNumber]
                        day = weatherDate.split('-')[2]
                        min_temp_date = month + " " + day
                
                if weatherDayInfo['Max Humidity'] != "":
                    humid = int(weatherDayInfo['Max Humidity'])
                    if humid > max_humid:
                        max_humid = humid
                        monthNumber = int(weatherDate.split('-')[1])
                        month = calendar.month_name[monthNumber]
                        day = weatherDate.split('-')[2]
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
        
        print (f'Highest: {highest_temp}C on {highest_temp_date}')
        print(f'Lowest: {lowest_temp}C on {lowest_temp_date}')
        print(f'Humidity: {humidity}% on {humidity_date}')
