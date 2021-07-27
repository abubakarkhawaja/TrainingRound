import calendar

from sourcecode.weather_records_reader import WeatherRecordsReader


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

    def calculate_year_record(self, weather_files: list) -> dict:
        """
        Calculates Highest Temperature, Lowest Temperature
        and Humidity.

        @params
        :weather_files list: hold list of files path.

        @return
        :dict: contains report data
        """
        for weather_file in weather_files:
            weather_records = WeatherRecordsReader.weather_info(weather_file)

            for weather_day_info in weather_records:                
                self.max_temperature(weather_day_info)
                self.min_temperature(weather_day_info)
                self.max_humidity(weather_day_info)

        return self.year_report

    def calculate_month_record(self, weather_file: str) -> dict:
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

        weather_records = WeatherRecordsReader.weather_info(weather_file)    
        for weather_day_info in weather_records:
            if weather_day_info['Max TemperatureC'] != "":
                total_max_temp += int(weather_day_info['Max TemperatureC'])
                
            if weather_day_info['Min TemperatureC'] != "":            
                total_min_temp += int(weather_day_info['Min TemperatureC'])
                
            if weather_day_info['Mean Humidity'] != "":
                total_mean_humidity += int(weather_day_info['Mean Humidity'])
            
        length = len(weather_records)
        self.calculate_average(total_max_temp, total_min_temp, total_mean_humidity, length)

        return self.month_report

    def calculate_average(
            self, total_max_temp: int, total_min_temp: int, 
            total_mean_humidity: int, length: int
    ) -> None:
        """
        Calculate average of maximum temperature, minimum temperature, and humidity.

        @params
        :total_max_temp int: Total of all maxmimum temperatures.
        :total_min_temp int: Total of all minimum temperatures.
        :total_mean_humidity int: Total of all mean humidities.
        :length int: length of all weather records.
        """
        self.month_report['avg_highest_temp'] = total_max_temp // length
        self.month_report['avg_lowest_temp'] = total_min_temp // length
        self.month_report['avg_mean_humidity'] = total_mean_humidity // length

    def max_humidity(self, weather_day_info: dict) -> None:
        """
        Assigns maximum humidity and its date in yearly report dictionary.

        @params
        :weather_day_info dict: Dictionary of Weather Record
        """
        if weather_day_info['Max Humidity'] == "":
            return

        humid = int(weather_day_info['Max Humidity'])

        if humid > self.year_report['humidity']:
            self.year_report['humidity'] = humid

            weather_date = weather_day_info['PKT']
            month, day = self.date(weather_date)
            self.year_report['humidity_date'] = month + " " + day

    def min_temperature(self, weather_day_info: dict) -> None:
        """
        Assigns maximum humidity and its date in yearly report dictionary.

        @params
        :weather_day_info dict: Dictionary of Weather Record
        """
        if weather_day_info['Min TemperatureC'] == "":
            return 

        temperature = int(weather_day_info['Min TemperatureC'])

        if temperature < self.year_report['lowest_temp']:
            self.year_report['lowest_temp'] = temperature

            weather_date = weather_day_info['PKT']            
            month, day = self.date(weather_date)
            self.year_report['lowest_temp_date'] = month + " " + day

    def max_temperature(self, weather_day_info: dict) -> None:
        """
        Assigns maximum humidity and its date in yearly report dictionary.

        @params
        :weather_day_info dict: Dictionary of Weather Record
        """
        if weather_day_info['Max TemperatureC'] == "":
            return
            
        temperature = int(weather_day_info['Max TemperatureC'])

        if temperature > self.year_report['highest_temp']:
            self.year_report['highest_temp'] = temperature

            weather_date = weather_day_info['PKT']            
            month, day = self.date(weather_date)
            self.year_report['highest_temp_date'] = month + " " + day

    def date(self, weather_date: str) -> list[str, str]:
        """
        Seperates day and month from date.

        @params
        :weather_date str: Date of weather record.

        @return
        :list[str, str]: month and day of weather record.
        """
        month_number = int(weather_date.split('-')[1])
        month = calendar.month_name[month_number]
        day = weather_date.split('-')[2]
        return [month, day]
