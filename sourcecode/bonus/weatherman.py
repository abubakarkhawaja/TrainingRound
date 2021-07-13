from sourcecode.weather_services import WeatherMan


class WeatherManBonus(WeatherMan):
    
    def weather_by_year_month_bar_bonus(self, path: str, date: str) -> None:
        """
        Parses all files and generates report.

        @params
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory
        """
        weather_file = self.get_weather_files(date, path)
        if weather_file == []:
            print('No such record found')
        else:
            full_path = path + weather_file[0]
            weather_data = self.get_weather_info(full_path)
            self.generate_report(date, weather_data)

    def generate_report(self, date: str, weather_data: dict) -> None:
        """
        Generates reports of each day in month
        
        @params
        :date str: date in form of Year/Month
        :weather_data dict: hold field names as key and their values.
        """
        self.print_month_year(date)
            
        for weather_day_info in weather_data:
            if weather_day_info['PKT'] != "":
                weather_date = weather_day_info['PKT'].split('-')[2]
                
            if weather_day_info['Max TemperatureC'] == "" \
                    or weather_day_info['Min TemperatureC'] == "":
                continue

            high_temp = int(weather_day_info['Max TemperatureC'])
            high_bar = self.generate_bar(high_temp)
            low_temp = int(weather_day_info['Min TemperatureC'])
            low_bar = self.generate_bar(low_temp)
                
            self.show_temperature_bar(
                    weather_date, high_temp, high_bar, low_temp, low_bar)

    def show_temperature_bar(
                self, weather_date: str, 
                high_temp: int, high_bar: str, 
                low_temp: int, low_bar: str) -> None:
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
        print(weather_date
                , f"\033[;34;40m{low_bar}\033[;31;40m{high_bar}"
                , f"\033[;;40m{low_temp}C - \033[;;40m{high_temp}C")
