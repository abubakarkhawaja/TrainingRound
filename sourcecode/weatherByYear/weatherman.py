from sourcecode.filehandling import FileHandling
from sourcecode.report_calculator import ReportCalculator
from sourcecode.report_generator import ReportGenerator

class WeatherManYear(FileHandling):
    report = {}

    def weather_by_year(self, path: str, date: str) -> None:
        """
        Parses all files and generates report.

        @params
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory
        """
        weather_files = self.get_weather_files(date, path)     
        if not weather_files:
            print('No Weather Date for these date.')
        else:
            for weather_file in weather_files:
                full_path = path + weather_file
                weather_data = self.get_weather_info(full_path)
                self.report = ReportCalculator.calculate_report_year(weather_data)
            ReportGenerator.generate_report_year(self.report)
