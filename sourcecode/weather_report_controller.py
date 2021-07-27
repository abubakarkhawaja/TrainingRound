import os

from sourcecode.weather_reports_display import WeatherReportsDisplay


class WeatherReportController:
    def __init__(self, directory_path: str) -> None:
        """
        Constructor for Driver

        @params
        :directory_path str: Path to folder of weather files
        """
        self.files_paths = self.complete_paths(directory_path)

    def report(self, option: str, date: str) -> None:
        """
        Calls respective class according to option.
        
        @params
        :option str: used to identify which report to get
        :date str: date in form Year/Month 
        """
        weather_report = WeatherReportsDisplay()
        if option == 'e':
            weather_report.display_extreme_report_of_year(self.files_paths, date)

        if option == 'a':
            weather_report.display_average_report_of_month(self.files_paths, date)
        
        if option == 'c':
            weather_report.display_report_bar(self.files_paths, date)
        
        if option == 'd':
            weather_report.display_report_single_bar(self.files_paths, date)
    
    def complete_paths(self, directory_path):
        try:
            files_names = os.listdir(directory_path)
        except IOError:
            print('Directory Not Found!')
        else:
            complete_files_paths = [directory_path + file_name for file_name in files_names]
            
            return complete_files_paths
