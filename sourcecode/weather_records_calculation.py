import calendar
from datetime import datetime

from .weather_records_reader import WeatherRecordsReader


class WeatherRecordsCalculation:
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

    def calculate_year_record(self, weather_month_record: list) -> dict:
        """
        Calculates Highest Temperature, Lowest Temperature
        and Humidity.

        @params
        :weather_records list: list of weather record of specific month.

        @return
        :dict: contains report data
        """
        for weather_day_record in weather_month_record:              
            self.compare_year_record(weather_day_record)
        return self.year_report
    
    def compare_year_record(self, weather_day_info: dict) -> None:
        """
        Assigns maximum humidity and its date in yearly report dictionary.

        @params
        :weather_day_info dict: Dictionary of Weather Record
        """
        temperature = int(weather_day_info['Max TemperatureC'] or '0')
        
        if temperature > self.year_report['highest_temp']:
            self.year_report['highest_temp'] = temperature
            self.save_date('highest_temp_date', weather_day_info['PKT'])

        temperature = int(weather_day_info['Min TemperatureC'] or '0')

        if temperature < self.year_report['lowest_temp']:
            self.year_report['lowest_temp'] = temperature            
            self.save_date('lowest_temp_date', weather_day_info['PKT'])

        humid = int(weather_day_info['Max Humidity'] or '0')
        
        if humid > self.year_report['humidity']:
            self.year_report['humidity'] = humid
            self.save_date('humidity_date', weather_day_info['PKT'])

    def calculate_month_record(self, weather_days_record: list) -> dict:
        """
        Calculates Highest Temperature, Lowest Temperature
        and Humidity.

        @params
        :weather_file str: hold file path.
        
        @return
        :dict: contains report data
        """
        total_max_temp = 0
        total_min_temp = 0
        total_mean_humidity = 0
        num_of_records = 0

        for weather_day_info in weather_days_record:
            total_max_temp += int(weather_day_info['Max TemperatureC'] or '0')
            total_min_temp += int(weather_day_info['Min TemperatureC'] or '0')                
            total_mean_humidity += int(weather_day_info['Mean Humidity'] or '0')
            num_of_records+=1

        self.calculate_average(total_max_temp, total_min_temp, total_mean_humidity, num_of_records)
        return self.month_report

    def calculate_average(self, total_max_temp: int, total_min_temp: int, total_mean_humidity: int, num_of_records: int) -> None:
        """
        Calculate average of maximum temperature, minimum temperature, and humidity.

        @params
        :total_max_temp int: Total of all maxmimum temperatures.
        :total_min_temp int: Total of all minimum temperatures.
        :total_mean_humidity int: Total of all mean humidities.
        :num_of_records int: total number of weather records.
        """
        self.month_report['avg_highest_temp'] = total_max_temp // num_of_records
        self.month_report['avg_lowest_temp'] = total_min_temp // num_of_records
        self.month_report['avg_mean_humidity'] = total_mean_humidity // num_of_records

    def save_date(self, key, weather_date: str) -> list[str, str]:
        """
        Seperates day and month from date.

        @params
        :key str: key of dictionary
        :weather_date str: Date of weather record.
        """
        date = datetime.strptime(weather_date, "%Y-%m-%d")
        month = calendar.month_name[date.month]
        self.year_report[key] = month + " " + str(date.day)
