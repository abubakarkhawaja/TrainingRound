from sourcecode.weatherByYear.weatherman import WeatherManYear
from sourcecode.weatherByYearMonth.weatherman import WeatherManYearMonth
from sourcecode.weatherByYearMonthBar.weatherman import WeatherManBar
from sourcecode.bonus.weatherman import WeatherManBonus 

class Driver:

    def __init__(self, directory_path):
        """
        Constructor for Driver

        @params
        :directory_path str: Path to folder of weather files
        """
        self.directory_path = directory_path

    def getReport(self, option, date):
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
            obj.weather_by_year_month(self.directory_path, date)
        if option == 'c':
            obj = WeatherManBar()
            obj.weather_by_year_month_bar(self.directory_path, date)
        if option == 'd':
            obj = WeatherManBonus()
            obj.weather_by_year_month_bar_bonus(self.directory_path, date)
