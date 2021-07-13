from sourcecode.filehandling import FileHandling
from sourcecode.report_generator import ReportGenerator

class WeatherManBar(FileHandling):
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
            ReportGenerator.generate_report_bar(date, weather_data)
