import calendar

class ReportCalculator:
    def calculate_report_year(weather_data: dict) -> dict:
        """
        Calculates Highest Temperature, Lowest Temperature
        and Humidity.

        @params
        :weather_data dict: hold field names as key and their values.

        @return
        :dict: contains report data
        """
        report = {
            'highest_temp': float('-inf'),
            'highest_temp_date': "",
            'lowest_temp_date': "",
            'lowest_temp': float('inf'),
            'humidity': float('-inf'),
            'humidity_date': "",
        }
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
                temperature = int(weather_day_info['Min TemperatureC'])
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

        if report['highest_temp'] < max_temp:
            report['highest_temp'] = max_temp
            report['highest_temp_date'] =max_temp_date

        if report['lowest_temp'] > min_temp:
            report['lowest_temp'] = min_temp
            report['lowest_temp_date'] = min_temp_date
                
        if report['humidity'] < max_humid:
            report['humidity'] = max_humid
            report['humidity_date'] = max_humid_date
        return report

    def calculate_report_year_month(weather_data: dict) -> dict:
        """
        Calculates Highest Temperature, Lowest Temperature
        and Humidity.

        @params
        :weather_data dict: hold field names as key and their values.
        
        @return
        :dict: contains report data
        """
        report = {
            'avg_highest_temp': float('-inf'),
            'avg_lowest_temp': float('inf'),
            'avg_mean_humidity': float('-inf'),
        }
        total_max_temp = 0
        total_min_temp = 0
        total_mean_humidity = 0
            
        for weather_day_info in weather_data:
            if weather_day_info['Max TemperatureC'] != "":
                total_max_temp += int(weather_day_info['Max TemperatureC'])
                
            if weather_day_info['Min TemperatureC'] != "":            
                total_min_temp += int(weather_day_info['Min TemperatureC'])
                
            if weather_day_info['Mean Humidity'] != "":
                total_mean_humidity += int(weather_day_info['Mean Humidity'])
            
        length = len(weather_data)
        report['avg_highest_temp'] = total_max_temp // length
        report['avg_lowest_temp'] = total_min_temp // length
        report['avg_mean_humidity'] = total_mean_humidity // length

        return report