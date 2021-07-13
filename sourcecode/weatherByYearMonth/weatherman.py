from sourcecode.weatherman import WeatherMan

class WeatherManYearMonth(WeatherMan):
    report = {
        'avg_highest_temp': float('-inf'),
        'avg_lowest_temp': float('inf'),
        'avg_mean_humidity': float('-inf'),
        }

    def weather_by_year_month(self, path: str, date: str) -> None:
        """
        Parses all files and generates report.
        
        @params
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory
        """
        weather_file = self.get_weather_files(date, path)
        if weather_file == []:
            print('No such record founnd')
        else:
            full_path = path + weather_file[0]
            weather_data = self.get_weather_info(full_path)
            self.calculate_report(weather_data)
            self.generate_report()

    def calculate_report(self, weather_data: dict) -> None:
        """
        Calculates Highest Temperature, Lowest Temperature
        and Humidity.

        @params
        :weather_data dict: hold field names as key and their values.
        """
        total_max_temp = 0
        total_min_temp = 0
        total_mean_humidity = 0
            
        for weather_day_info in weather_data:
            if weather_day_info['Max TemperatureC'] != "":
                total_max_temp += int(weather_day_info['Max TemperatureC'])
                
            if weather_day_info['Min TemperatureC'] != "":            
                total_min_temp += int (weather_day_info['Min TemperatureC'])
                
            if weather_day_info['Mean Humidity'] != "":
                total_mean_humidity += int(weather_day_info['Mean Humidity'])
            
        length = len(weather_data)
        self.report['avg_highest_temp'] = total_max_temp // length
        self.report['avg_lowest_temp'] = total_min_temp // length
        self.report['avg_mean_humidity'] = total_mean_humidity // length

    def generate_report(self) -> None:
        """Used for priniting report"""
        avg_highest_temp = self.report['avg_highest_temp']
        avg_lowest_temp = self.report['avg_lowest_temp']
        avg_mean_humidity = self.report['avg_mean_humidity']
        print (f'Highest Average: {avg_highest_temp}C')
        print(f'Lowest Average: {avg_lowest_temp}C')
        print(f'Average Mean Humidity: {avg_mean_humidity}%')
