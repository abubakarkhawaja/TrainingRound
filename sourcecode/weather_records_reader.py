import calendar
from csv import DictReader
from datetime import datetime


class WeatherRecordsReader:
    def weather_files(date: str, path: list) -> list[str]:
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
            weather_files = [file_path for file_path in path if year in file_path and month in file_path]
            if not weather_files:
                return
            return weather_files[0]
        
        weather_files = [file_path for file_path in path if date in file_path]
        return weather_files

    def weather_info(path: str) -> list[dict]:
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
        
        with open(path, 'r') as csv_file:
            csv_reader = DictReader(csv_file)
            weather_records = WeatherRecordsReader.weather_records_parser(csv_reader)
            csv_file.flush()
        return weather_records
    
    def weather_records_parser(csv_reader: DictReader) -> dict:
        """
        Cleans and converts data to its appropriate datatype.

        @params
        :csv_reader DictReader: contains data gathered from weatherfile

        @return
        :dict: dictionary with column name as key and their values
        """
        weather_records = []
        if not csv_reader:
            print('Empty file')
            return
        
        csv_reader.fieldnames = [str(field).strip() for field in csv_reader.fieldnames]
        weather_records = list(csv_reader)
        return weather_records


def split_date(weather_date: str) -> list[str, str]:
    """
    Seperates day and month from date.

    @params
    :date str: Date of weather record.

    @return
    :list[str, str]: month and year of weather record.
    """
    date_format = "%Y/%m"
    date = datetime.strptime(weather_date, date_format)
    month = calendar.month_abbr[date.month]
    return [month, str(date.year)]
