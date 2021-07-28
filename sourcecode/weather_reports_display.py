import calendar
from datetime import datetime

from .weather_records_calculation import WeatherRecordsCalculation
from .weather_records_reader import WeatherRecordsReader

BLUE_COLOR = "\033[;34;40m"
RED_COLOR = "\033[;31;40m"
WHITE_COLOR = "\033[;;40m"

class WeatherReportsDisplay():
    def __init__(self, path: str) -> None:
        """
        Constructor for initializing reports
        
        @params
        :path str: Complete path of weatherfiles 
        """
        self.path = path
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

    def display_extreme_report_of_year(self, date: str) -> None:
        """
        Used for printing report
        
        @params        
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_files = WeatherRecordsReader.weather_files(date, self.path)    
        
        if not weather_files:
            print('No Weather Date for these date.')
            return

        record_calculator = WeatherRecordsCalculation()
        self.year_report = record_calculator.calculate_year_record(weather_files)

        print (f'Highest: {self.year_report["highest_temp"]}C on {self.year_report["highest_temp_date"]}')
        print(f'Lowest: {self.year_report["lowest_temp"]}C on {self.year_report["lowest_temp_date"]}')
        print(f'Humidity: {self.year_report["humidity"]}% on {self.year_report["humidity_date"]}')
    
    def display_average_report_of_month(self, date: str) -> None:
        """
        Used for priniting report
        
        @params
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_file = WeatherRecordsReader.weather_files(date, self.path)    
        
        if not weather_file:
            print('No such record found!')
            return

        record_calculator = WeatherRecordsCalculation()
        self.month_report = record_calculator.calculate_month_record(weather_file)
    
        print (f'Highest Average: {self.month_report["avg_highest_temp"]}C')
        print(f'Lowest Average: {self.month_report["avg_lowest_temp"]}C')
        print(f'Average Mean Humidity: {self.month_report["avg_mean_humidity"]}%')

    def display_report_bar(self, date: str) -> None:
        """ 
        Prints bar for high and low temperature of each dates.

        @params
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_file = WeatherRecordsReader.weather_files(date, self.path)    
        if not weather_file:
            print('No such record found')
            return 

        weather_records = WeatherRecordsReader.weather_info(weather_file)

        self.print_month_year(date)
            
        for weather_day_info in weather_records:
            if weather_day_info['PKT'] != "":
                weather_date = weather_day_info['PKT'].split('-')[2]

            self.show_high_temperature(weather_day_info, weather_date)
            self.show_low_temperature(weather_day_info, weather_date)

    def display_report_single_bar(self, date: str) -> None:
        """
        displays reports of each day in month
        
        @params
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        weather_file = WeatherRecordsReader.weather_files(date, self.path)    
        
        if not weather_file:
            print('No such record founnd')
            return

        weather_records = WeatherRecordsReader.weather_info(weather_file)

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

    def display(self, weather_date: str, high_temp: int, high_bar: str, low_temp: int, low_bar: str) -> None:
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
            , f"{BLUE_COLOR}{low_bar}{RED_COLOR}{high_bar}"
            , f"{WHITE_COLOR}{low_temp}C - {WHITE_COLOR}{high_temp}C"
        )

    def show_low_temperature(self, weather_day_info: dict, weather_date: str) -> None:
        """
        Show items for low temperature per day.

        @params
        :weather_day_info dict: Contains weather record of day.
        :weather_date str: Contains day of month.
        """
        if weather_day_info['Min TemperatureC'] == "":
            return

        low_temp = int(weather_day_info['Min TemperatureC'])
        low_bar = self.create_bar(low_temp)
        
        print(weather_date, f"{BLUE_COLOR}{low_bar}", f"{WHITE_COLOR}{low_temp}C")

    def show_high_temperature(self, weather_day_info: dict, weather_date: str) -> None:
        """
        Show items for high temperature per day.

        @params
        :weather_day_info dict: Contains weather record of day.
        :weather_date str: Contains day of month.
        """
        if weather_day_info['Max TemperatureC'] == "":
            return

        high_temp = int(weather_day_info['Max TemperatureC'])
        high_bar = self.create_bar(high_temp)

        print(weather_date, f"{RED_COLOR}{high_bar}", f"{WHITE_COLOR}{high_temp}C")

    def create_bar(self, size_of_bar: int) -> str:
        """
        Used to create bar of certain length made of '+' character

        @params
        :size_of_bar int: length of bar needed
        @return
        :str: sequence of '+' signs 
        """
        return "".join(['+'] * size_of_bar)
    
    def print_month_year(self, weather_date: str) -> None:
        """
        Print Month and Year

        @params
        :date str: Contains date 'Year/Month'
        """
        date_format = "%Y/%m"
        date = datetime.strptime(weather_date, date_format)
        month = calendar.month_name[date.month]
        print(month, str(date.year))
