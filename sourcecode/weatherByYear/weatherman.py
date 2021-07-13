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

    weather_files = get_weather_files(date, path)     
    if not weather_files:
        print('No Weather Date for these date.')
    else:
        for weather_file in weather_files:
            full_path = path + weather_file
            weather_data = get_weather_info(full_path)

            max_temp =  float('-inf')
            max_temp_date = ""
            min_temp = float('inf')
            min_temp_date = ""
            max_humid =  float('-inf')
            max_humid_date = ""
            
            for weather_day_info in weather_data:
                if weather_day_info['PKT'] != "":
                    weather_date = weather_day_info['PKT']

                if weather_day_info['Max TemperatureC'] != "":
                    temperature = int(weather_day_info['Max TemperatureC'])
                    if temperature > max_temp:
                        max_temp = temperature
                        month_number = int(weather_date.split('-')[1])
                        month = calendar.month_name[month_number]
                        day = weather_date.split('-')[2]
                        max_temp_date = month + " " + day
                
                if weather_day_info['Min TemperatureC'] != "":            
                    temperature = int (weather_day_info['Min TemperatureC'])
                    if temperature < min_temp:
                        min_temp = temperature
                        month_number = int(weather_date.split('-')[1])
                        month = calendar.month_name[month_number]
                        day = weather_date.split('-')[2]
                        min_temp_date = month + " " + day
                
                if weather_day_info['Max Humidity'] != "":
                    humid = int(weather_day_info['Max Humidity'])
                    if humid > max_humid:
                        max_humid = humid
                        month_number = int(weather_date.split('-')[1])
                        month = calendar.month_name[month_number]
                        day = weather_date.split('-')[2]
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
