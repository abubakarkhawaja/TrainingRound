from sourcecode.weather_services import WeatherMan

class ReportGenerator():
    def generate_report_year(report: dict) -> None:
        """
        Used for priniting report
        
        @params
        :report dict: contains values to be printed
        """
        highest_temp = report['highest_temp']
        highest_temp_date = report['highest_temp_date']
        lowest_temp = report['lowest_temp']
        lowest_temp_date = report['lowest_temp_date']
        humidity = report['humidity']
        humidity_date = report['humidity_date']
        print (f'Highest: {highest_temp}C on {highest_temp_date}')
        print(f'Lowest: {lowest_temp}C on {lowest_temp_date}')
        print(f'Humidity: {humidity}% on {humidity_date}')
    
    def generate_report_year_month(report: dict) -> None:
        """
        Used for priniting report
        
        @params
        :report dict: contains values to be printed
        """
        avg_highest_temp = report['avg_highest_temp']
        avg_lowest_temp = report['avg_lowest_temp']
        avg_mean_humidity = report['avg_mean_humidity']
        print (f'Highest Average: {avg_highest_temp}C')
        print(f'Lowest Average: {avg_lowest_temp}C')
        print(f'Average Mean Humidity: {avg_mean_humidity}%')

    def generate_report_bar(date: str, weather_data: dict) -> None:
        """ 
        Prints bar for high and low temperature of each dates.

        @params
        :date str: contains month and year 
        :weather_data dict: hold field names as key and their values.
        """
        WeatherMan.print_month_year(date)
            
        for weather_day_info in weather_data:
            if weather_day_info['PKT'] != "":
                weather_date = weather_day_info['PKT'].split('-')[2]
    
            if weather_day_info['Max TemperatureC'] != "":
                high_temp = int(weather_day_info['Max TemperatureC'])
                high_bar = WeatherMan.generate_bar(high_temp)
                ReportGenerator.show_high_temperature_bar(weather_date, high_temp, high_bar)

            if weather_day_info['Max TemperatureC'] != "":
                low_temp = int(weather_day_info['Min TemperatureC'])
                low_bar = WeatherMan.generate_bar(low_temp)
                ReportGenerator.show_low_temperature_bar(weather_date, low_temp, low_bar)

    def show_low_temperature_bar(weather_date: str, low_temp: int, low_bar: int) -> None:
        """
        Shows low temperature bar of blue color (34)
        
        @params
        :weather_date str: Day of month
        :low_temp int: Low temperature of date
        :low_bar str: '+'Bar to be visual
        """
        print(weather_date, f"\033[1;34;40m{low_bar}", f"\033[1;;40m{low_temp}C")

    def show_high_temperature_bar(weather_date: str, high_temp: int, high_bar: int) -> None:
        """
        Shows low temperature bar of red color (31)
        
        @params
        :weather_date str: Day of month
        :high_temp int: Low temperature of date
        :high_bar str: '+'Bar to be visual
        """
        print(weather_date, f"\033[1;31;40m{high_bar}", f"\033[1;;40m{high_temp}C")

    def generate_report_single_bar(date: str, weather_data: dict) -> None:
        """
        Generates reports of each day in month
        
        @params
        :date str: date in form of Year/Month
        :weather_data dict: hold field names as key and their values.
        """
        WeatherMan.print_month_year(date)
            
        for weather_day_info in weather_data:
            if weather_day_info['PKT'] != "":
                weather_date = weather_day_info['PKT'].split('-')[2]
                
            if weather_day_info['Max TemperatureC'] == "" \
                    or weather_day_info['Min TemperatureC'] == "":
                continue

            high_temp = int(weather_day_info['Max TemperatureC'])
            high_bar = WeatherMan.generate_bar(high_temp)
            low_temp = int(weather_day_info['Min TemperatureC'])
            low_bar = WeatherMan.generate_bar(low_temp)
                
            ReportGenerator.show_temperature_bar_single(weather_date, high_temp, high_bar, low_temp, low_bar)

    def show_temperature_bar_single(weather_date: str, high_temp: int, high_bar: str, low_temp: int, low_bar: str) -> None:
        """
        Show two different types of bars on same line of different
        colors.
        
        @params
        :weather_date str: Date
        :high_temp int: High temperature of day
        :high_bar str: Bar to be visualize for high temperature
        :low_temp int: Low temperature of day
        :low_bar str: Bar to be visualize for low temperature
        """
        print(
            weather_date
            , f"\033[;34;40m{low_bar}\033[;31;40m{high_bar}"
            , f"\033[;;40m{low_temp}C - \033[;;40m{high_temp}C"
        )
