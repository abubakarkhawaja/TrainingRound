import os, calendar, csv

class WeatherMan:
    def get_weather_files(self, date: str, path: str) -> list[str]:
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
                weather_files = [dir 
                                for dir in directory 
                                if year in dir 
                                and month in dir]        
            else: 
                weather_files = [dir 
                                for dir in directory 
                                if date in dir]
            return weather_files


    def get_weather_info(self, path: str) -> list[dict]:
        """
        Gets directory path and read data within that file. 
        
        @params
        :path str: Contains path to weather file directory

        @return
        :dict: returns list of dictionaries with data on weather file.
        """
        weather_data = []
        if not path:
            raise FileNotFoundError('File not found')
        else:
            with open(path, 'r') as csv_file:
                csv_reader = csv.DictReader(csv_file)
                csv_reader.fieldnames = [str(field).strip()
                                        for field in csv_reader.fieldnames]
                weather_data = list(csv_reader)
                csv_file.flush()
        return weather_data

    def generateBar(self, size_of_bar: int) -> str:
        """
        Used to create bar of certain length made of '+' character

        @params
        :size_of_bar int: length of bar needed
        """
        return "".join(['+'] * size_of_bar)
    
    def printMonthYear(self, date: str) -> None:
        """
        Print Month and date

        @params
        :date str: Contains date 'Year/Month'
        """
        month_number = int(date.split('/')[1])
        month = calendar.month_name[month_number]
        year = date.split('/')[0]
        print(month, year)
