from sourcecode.weather_services import WeatherMan


class WeatherManBar(WeatherMan):

    def weather_by_year_month_bar(self, path: str, date: str) -> None:
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
            self.generate_report(date, weather_data)

    def generate_report(self, date: str, weather_data: dict) -> None:
        """ 
        Prints bar for high and low temperature of each dates.

        @params
        :date str: contains month and year 
        :weather_data dict: hold field names as key and their values.
        """
        self.printMonthYear(date)
            
        for weather_day_info in weather_data:
            if weather_day_info['PKT'] != "":
                weather_date = weather_day_info['PKT'].split('-')[2]
    
            if weather_day_info['Max TemperatureC'] != "":
                high_temp = int(weather_day_info['Max TemperatureC'])
                high_bar = self.generateBar(high_temp)
                self.showHighTemperatureBar(weather_date, high_temp, high_bar)

            if weather_day_info['Max TemperatureC'] != "":
                low_temp = int(weather_day_info['Min TemperatureC'])
                low_bar = self.generateBar(low_temp)
                self.showLowTemperatureBar(weather_date, low_temp, low_bar)

    def showLowTemperatureBar(
                self, weather_date: str, 
                low_temp: int, low_bar: int) -> None:
        """
        Shows low temperature bar of blue color (34)
        
        @params
        :weather_date str: Day of month
        :low_temp int: Low temperature of date
        :low_bar str: '+'Bar to be visual
        """
        print(weather_date
                    , f"\033[1;34;40m{low_bar}"
                    , f"\033[1;;40m{low_temp}C")

    def showHighTemperatureBar(
                self, weather_date: str, 
                high_temp: int, high_bar: int) -> None:
        """
        Shows low temperature bar of red color (31)
        
        @params
        :weather_date str: Day of month
        :high_temp int: Low temperature of date
        :high_bar str: '+'Bar to be visual
        """
        print(weather_date
                    , f"\033[1;31;40m{high_bar}"
                    , f"\033[1;;40m{high_temp}C")
