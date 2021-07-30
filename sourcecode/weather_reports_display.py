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
        self.year_report = {}
        self.year_report['highest_temp'] = float('-inf')
        self.year_report['highest_temp_date'] = ""
        self.year_report['lowest_temp_date'] = ""
        self.year_report['lowest_temp'] = float('inf')
        self.year_report['humidity'] = float('-inf')
        self.year_report['humidity_date'] = ""

        self.month_report = {}
        self.month_report['avg_highest_temp'] = float('-inf')
        self.month_report['avg_lowest_temp'] = float('inf')
        self.month_report['avg_mean_humidity'] = float('-inf')

        weather_reader = WeatherRecordsReader(path)
        self.weathers_record = weather_reader.weathers_record

    def display_extreme_report_of_year(self, date: str) -> None:
        """
        Used for printing report
        
        @params        
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """
        record_calculator = WeatherRecordsCalculation()
        full_dates = tuple(key for key in self.weathers_record.keys() if date in key)
        
        if not full_dates:
            print(f'No such Records for {date}')
            return None
        for full_date in full_dates:
            self.year_report = record_calculator.calculate_year_record(self.weathers_record[full_date])
                
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
        if date not in self.weathers_record.keys():
            print('No Weather Date for these date.')
            return None

        record_calculator = WeatherRecordsCalculation()
        self.month_report = record_calculator.calculate_month_record(self.weathers_record[date])
    
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
        if date not in self.weathers_record.keys():
            print('No Weather Date for these date.')
            return None
            
        print(split_date(date))
        for weather_day_info in self.weathers_record[date]:
            if not weather_day_info['PKT']:
                continue
            weather_date = datetime.strptime(weather_day_info['PKT'], '%Y-%m-%d').day
            self.display_seperate_bar(weather_day_info, weather_date)

    def display_report_single_bar(self, date: str) -> None:
        """
        displays reports of each day in month
        
        @params
        :path str: Contains path to weather files directory.
        :date str: Date entered by user as command line argument.
        """    
        if date not in self.weathers_record.keys():
            print('No Weather Date for these date.')
            return None

        print(split_date(date))

        for weather_day_info in self.weathers_record[date]:
            if not weather_day_info['PKT']:
                continue
            weather_date = datetime.strptime(weather_day_info['PKT'], '%Y-%m-%d').day   
            high_temp = int(weather_day_info['Max TemperatureC'] or '0')
            high_bar = self.create_bar(high_temp)
            low_temp = int(weather_day_info['Min TemperatureC'] or '0')
            low_bar = self.create_bar(low_temp)
            self.display_combined_bar(weather_date, high_temp, high_bar, low_temp, low_bar)

    def display_combined_bar(self, weather_date: str, high_temp: int, high_bar: str, low_temp: int, low_bar: str) -> None:
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

    def display_seperate_bar(self, weather_day_info: dict, weather_date: str) -> None:
        """
        Show items for low temperature per day.

        @params
        :weather_day_info dict: Contains weather record of day.
        :weather_date str: Contains day of month.
        """
        low_temp = int(weather_day_info['Min TemperatureC'] or '0')
        low_bar = self.create_bar(low_temp)
        print(weather_date, f"{BLUE_COLOR}{low_bar}", f"{WHITE_COLOR}{low_temp}C")

        high_temp = int(weather_day_info['Max TemperatureC'] or '0')
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
        
def split_date(weather_date: str) -> list[str, str]:
    """
    Seperates day and month from date.

    @params
    :date str: Date of weather record.

    @return
    :list[str, str]: month and year of weather record.
    """
    date = datetime.strptime(weather_date, "%Y/%m")
    month = calendar.month_abbr[date.month]
    return [month, str(date.year)]
