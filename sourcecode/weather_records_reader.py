import calendar
from csv import DictReader
from datetime import datetime


class WeatherRecordsReader:
    def __init__(self, paths) -> None:
        self.paths = paths
        self.weathers_record = {}
        self.read_weather_info()

    def read_weather_info(self):
        """Gets directory path and read data within that file."""
        if not self.paths:
            raise FileNotFoundError('File not found')
            
        for file_path in self.paths:
            splitted_path = file_path.split('.')[0].split('_')
            month, year = list(calendar.month_abbr).index(splitted_path[-1]), splitted_path[-2]
            key = f"{year}/{month}"
            
            self.weathers_record[key] = []
            with open(file_path, 'r') as csv_file:
                csv_reader = DictReader(csv_file)
                if not csv_reader:
                    print('Empty file')
                    continue
                
                csv_reader.fieldnames = [str(field).strip() for field in csv_reader.fieldnames]
                self.weathers_record[key] = list(csv_reader)
                csv_file.flush()
