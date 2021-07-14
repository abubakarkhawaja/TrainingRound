from sourcecode.filehandling import FileHandling
from sourcecode.report_generator import ReportGenerator


class WeatherManSingleBar():
    def daily_weather_by_single_bar(self, path: str, date: str) -> None:
        """
        Parses all files and generates report.

        @params
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory
        """
        weather_file = FileHandling.get_weather_files(date, path)
        if weather_file == []:
            print('No such record found')
        else:
            full_path = path + weather_file[0]
            weather_record = FileHandling.get_weather_info(full_path)
            
            ReportGenerator.generate_report_single_bar(date, weather_record)
