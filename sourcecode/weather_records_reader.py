from csv import DictReader


class WeatherRecordsReader:
    def read_weather_info(path: str) -> list[dict]:
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
            if not csv_reader:
                print('Empty file')
                return weather_records
            
            csv_reader.fieldnames = [str(field).strip() for field in csv_reader.fieldnames]
            weather_records = list(csv_reader)
            csv_file.flush()
        return weather_records
