from sourcecode.utilities import get_weather_files, get_weather_info, calendar


class WeatherManYear:
    report = {
        'highest_temp': float('-inf'),
        'highest_temp_date': "",
        'lowest_temp_date': "",
        'lowest_temp': float('inf'),
        'humidity': float('-inf'),
        'humidity_date': "",
        }

    def weather_by_year(self, path: str, date: str) -> None:
        """
        Parses all files and generates report.

        @params
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory
        """
        weather_files = get_weather_files(date, path)     
        if not weather_files:
            print('No Weather Date for these date.')
        else:
            for weather_file in weather_files:
                full_path = path + weather_file
                weather_data = get_weather_info(full_path)
                self.calculate_report(weather_data)
            self.generate_report()

    def calculate_report(self, weather_data: dict) -> None:
        """
        Calculates Highest Temperature, Lowest Temperature
        and Humidity.

        @params
        :weather_data dict: hold field names as key and their values.
        """
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

        if self.report['highest_temp'] < max_temp:
            self.report['highest_temp'] = max_temp
            self.report['highest_temp_date'] =max_temp_date

        if self.report['lowest_temp'] > min_temp:
            self.report['lowest_temp'] = min_temp
            self.report['lowest_temp_date'] = min_temp_date
                
        if self.report['humidity'] < max_humid:
            self.report['humidity'] = max_humid
            self.report['humidity_date'] = max_humid_date

    def generate_report(self) -> None:
        """Used for priniting report"""
        highest_temp = self.report['highest_temp']
        highest_temp_date = self.report['highest_temp_date']
        lowest_temp = self.report['lowest_temp']
        lowest_temp_date = self.report['lowest_temp_date']
        humidity = self.report['humidity']
        humidity_date = self.report['humidity_date']
        print (f'Highest: {highest_temp}C on {highest_temp_date}')
        print(f'Lowest: {lowest_temp}C on {lowest_temp_date}')
        print(f'Humidity: {humidity}% on {humidity_date}')
