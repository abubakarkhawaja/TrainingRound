from sourcecode.filehandling import FileHandling
from sourcecode.report_generator import ReportGenerator
from sourcecode.weather_record_parser import WeatherRecordParser


class WeatherManYear(FileHandling):
    def __init__(self) -> None:
        self.report = {}

    def weather_by_year(self, path: str, date: str) -> None:
        """
        Parses all files and generates report.

        @params
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory
        """
        weather_files = FileHandling.get_weather_files(date, path)    
        
        if not weather_files:
            print('No Weather Date for these date.')
        else:
            record_parser = WeatherRecordParser()
            self.report = record_parser.parse_year_record(weather_files, path)
            
            ReportGenerator.generate_report_year(self.report)
