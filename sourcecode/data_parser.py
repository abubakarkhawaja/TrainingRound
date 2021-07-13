from csv import DictReader

class DataParser:
    def data_parser(csv_reader: DictReader) -> dict:
        """
        Cleans and converts data to its appropriate datatype.

        @params
        :csv_reader DictReader: contains data gathered from weatherfile

        @return
        :dict: dictionary with column name as key and their values
        """
        if not csv_reader:
            print('Empty file')
        else:
            csv_reader.fieldnames = [str(field).strip() for field in csv_reader.fieldnames]
            weather_data = list(csv_reader)
        return weather_data