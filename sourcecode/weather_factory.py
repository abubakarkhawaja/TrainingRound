from sourcecode.weatherByYear.weatherman import WeatherManYear
from sourcecode.weatherByYearMonth.weatherman import WeatherManYearMonth
from sourcecode.weatherByYearMonthBar.weatherman import WeatherManBar
from sourcecode.weatherByYearMonthSingleBar.weatherman import WeatherManSingleBar


class WeatherFactory:
    def __init__(self, directory_path: str) -> None:
        """
        Constructor for Driver

        @params
        :directory_path str: Path to folder of weather files
        """
        self.directory_path = directory_path

    def get_report(self, option: str, date: str) -> None:
        """
        Calls respective class according to option.
        
        @params
        :option str: used to identify which report to get
        :date str: date in form Year/Month 
        """
        if option == 'e':
            obj = WeatherManYear()
            obj.weather_by_year(self.directory_path, date)

        if option == 'a':
            obj = WeatherManYearMonth()
            obj.average_weather_of_month(self.directory_path, date)
        
        if option == 'c':
            obj = WeatherManBar()
            obj.daily_weather_by_seperate_bar(self.directory_path, date)
        
        if option == 'd':
            obj = WeatherManSingleBar()
            obj.daily_weather_by_single_bar(self.directory_path, date)
