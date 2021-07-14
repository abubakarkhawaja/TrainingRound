import calendar, csv, os

from sourcecode.data_parser import DataParser


class FileHandling:
    def get_weather_files(date: str, path: str) -> list[str]:
        """
        Gets date and directory path. 
        Base on these returns file names.

        @params:
        :date str: Date entered by user as command line argument
        :path str: Contains path to weather files directory

        @return
        :list: list of full path to weather files
        
        @raise
        :IOError: File not found    
        """
        try:
            directory = os.listdir(path)
        except IOError:
            print("File not found")
        else:
            if '/' in date:
                month_number = int(date.split('/')[1])
                month = calendar.month_abbr[month_number]
                year = date.split('/')[0]
                
                weather_files = [filename for filename in directory if year in filename and month in filename]        
            else: 
                weather_files = [filename for filename in directory if date in filename]
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
                weather_records = DataParser.data_parser(csv_reader)
                csv_file.flush()
        return weather_records
