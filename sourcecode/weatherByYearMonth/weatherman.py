from sourcecode.filehandling import FileHandling
from sourcecode.report_generator import ReportGenerator
from sourcecode.weather_record_parser import WeatherRecordParser


class WeatherManYearMonth():
    def __init__(self) -> None:
        self.report = {}

    def average_weather_of_month(self, path: str, date: str) -> None:
        """
        Parses all files and generates report.
        
        @params
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory
        """
        weather_file = FileHandling.get_weather_files(date, path)

        if weather_file == []:
            print('No such record founnd')
        else:
            full_path = path + weather_file[0]
            weather_records = FileHandling.get_weather_info(full_path)
            
            record_parser = WeatherRecordParser()
            self.report = record_parser.parse_month_record(weather_records)
            
            ReportGenerator.generate_average_report_of_month(self.report)
