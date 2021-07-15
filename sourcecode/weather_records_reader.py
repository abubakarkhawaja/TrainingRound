import calendar, csv

from sourcecode.weather_records_parser import WeatherRecordsParser


class WeatherRecordsReader:
    def get_weather_files(date: str, path: list) -> list[str]:
        """
        Gets date and directory path. 
        Base on these returns file names.

        @params:
        :date str: Date entered by user as command line argument
        :path list: Contains list of paths to weather files directory

        @return
        :list: list of full path to weather files
        """
        weather_files = []
        if '/' in date:
            month, year = split_date(date)
            weather_files = [file_path for file_path in path if year in file_path and month in file_path][0]        
        else:
            weather_files = [file_path for file_path in path if date in file_path]
        return weather_files

    def get_weather_info(path: str) -> list[dict]:
        """
        Gets directory path and read data within that file. 
        
        @params
        :path str: Contains path to weather file directory

        @return
        :dict: returns list of dictionaries with data on weather file.
        """
        weather_records = []
        if not path:
            raise FileNotFoundError('File not found')
        else:
            with open(path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                weather_records = WeatherRecordsParser.weather_records_parser(csv_reader)
                csv_file.flush()
        return weather_records

def split_date(date: str) -> list[str, str]:
    """
    Seperates day and month from date.

    @params
    :date str: Date of weather record.

    @return
    :list[str, str]: month and year of weather record.
    """
    month_number = int(date.split('/')[1])
    month = calendar.month_abbr[month_number]
    year = date.split('/')[0]

    return month, year
