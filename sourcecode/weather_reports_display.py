import calendar

from sourcecode.weather_records_calculation import WeatherRecordsCalculation
from sourcecode.weather_records_reader import WeatherRecordsReader


class WeatherReportsDisplay():
    def __init__(self) -> None:
        """Constructor for initializing reports"""
        self.year_report = {
            'highest_temp': float('-inf'),
            'highest_temp_date': "",
            'lowest_temp_date': "",
            'lowest_temp': float('inf'),
            'humidity': float('-inf'),
            'humidity_date': "",
        }

        self.month_report = {
            'avg_highest_temp': float('-inf'),
            'avg_lowest_temp': float('inf'),
            'avg_mean_humidity': float('-inf'),
        }

    def display_extreme_report_of_year(self, path: str, date: str) -> None:
        """
        Used for printing report
        
        @params        
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_files = WeatherRecordsReader.get_weather_files(date, path)    
        
        if not weather_files:
            print('No Weather Date for these date.')
        else:
            record_calculator = WeatherRecordsCalculation()
            self.year_report = record_calculator.calculate_year_record(weather_files)

        print (f'Highest: {self.year_report["highest_temp"]}C on {self.year_report["highest_temp_date"]}')
        print(f'Lowest: {self.year_report["lowest_temp"]}C on {self.year_report["lowest_temp_date"]}')
        print(f'Humidity: {self.year_report["humidity"]}% on {self.year_report["humidity_date"]}')
    
    def display_average_report_of_month(self, path: str, date: str) -> None:
        """
        Used for priniting report
        
        @params
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_file = WeatherRecordsReader.get_weather_files(date, path)    
        
        if not weather_file:
            print('No such record founnd')
        else:
            record_calculator = WeatherRecordsCalculation()
            self.month_report = record_calculator.calculate_month_record(weather_file)
        
            print (f'Highest Average: {self.month_report["avg_highest_temp"]}C')
            print(f'Lowest Average: {self.month_report["avg_lowest_temp"]}C')
            print(f'Average Mean Humidity: {self.month_report["avg_mean_humidity"]}%')

    def display_report_bar(self, path: str, date: str) -> None:
        """ 
        Prints bar for high and low temperature of each dates.

        @params
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_file = WeatherRecordsReader.get_weather_files(date, path)    
        
        if not weather_file:
            print('No such record founnd')
        else:
            weather_records = WeatherRecordsReader.get_weather_info(weather_file)

            self.print_month_year(date)
                
            for weather_day_info in weather_records:
                if weather_day_info['PKT'] != "":
                    weather_date = weather_day_info['PKT'].split('-')[2]

                self.show_high_temperature(weather_day_info, weather_date)
                self.show_low_temperature(weather_day_info, weather_date)

    def display_report_single_bar(self, path: str, date: str) -> None:
        """
        displays reports of each day in month
        
        @params
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_file = WeatherRecordsReader.get_weather_files(date, path)    
        
        if not weather_file:
            print('No such record founnd')
        else:
            weather_records = WeatherRecordsReader.get_weather_info(weather_file)

            self.print_month_year(date)
                
            for weather_day_info in weather_records:
                if weather_day_info['PKT'] != "":
                    weather_date = weather_day_info['PKT'].split('-')[2]
                    
                if (weather_day_info['Max TemperatureC'] == "" or 
                weather_day_info['Min TemperatureC'] == ""):
                    continue

                high_temp = int(weather_day_info['Max TemperatureC'])
                high_bar = self.create_bar(high_temp)
                low_temp = int(weather_day_info['Min TemperatureC'])
                low_bar = self.create_bar(low_temp)
                    
                self.display(weather_date, high_temp, high_bar, low_temp, low_bar)

    def display(
            self, weather_date: str, 
            high_temp: int, high_bar: str, 
            low_temp: int, low_bar: str
    ) -> None:
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

    def show_low_temperature(self, weather_day_info: dict, weather_date: str) -> None:
        """
        Show items for low temperature per day.

        @params
        :weather_day_info dict: Contains weather record of day.
        :weather_date str: Contains day of month.
        """
        if weather_day_info['Min TemperatureC'] != "":
            low_temp = int(weather_day_info['Min TemperatureC'])
            low_bar = self.create_bar(low_temp)
            
            print(weather_date, f"\033[1;34;40m{low_bar}", f"\033[1;;40m{low_temp}C")

    def show_high_temperature(self, weather_day_info: dict, weather_date: str) -> None:
        """
        Show items for high temperature per day.

        @params
        :weather_day_info dict: Contains weather record of day.
        :weather_date str: Contains day of month.
        """
        if weather_day_info['Max TemperatureC'] != "":
            high_temp = int(weather_day_info['Max TemperatureC'])
            high_bar = self.create_bar(high_temp)

            print(weather_date, f"\033[1;31;40m{high_bar}", f"\033[1;;40m{high_temp}C")

    def create_bar(self, size_of_bar: int) -> str:
        """
        Used to create bar of certain length made of '+' character

        @params
        :size_of_bar int: length of bar needed
        @return
        :str: sequence of '+' signs 
        """
        return "".join(['+'] * size_of_bar)
    
    def print_month_year(self, date: str) -> None:
        """
        Print Month and Year

        @params
        :date str: Contains date 'Year/Month'
        """
        month_number = int(date.split('/')[1])
        month = calendar.month_name[month_number]
        year = date.split('/')[0]
        print(month, year)
