from csv import DictReader


class WeatherRecordsParser:
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
