import os, calendar, csv


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
            monthNumber = int(date.split('/')[1])
            month = calendar.month_abbr[monthNumber]
            year = date.split('/')[0]
            weatherFiles = [dir for dir in directory if year in dir and month in dir]        
        else: 
            weatherFiles = [dir for dir in directory if date in dir]
        return weatherFiles


def get_weather_info(path: str) -> dict[str, dict]:
    """
    Gets directory path and read data within that file. 
    
    @params
    :path str: Contains path to weather file directory

    @return
    :dict: returns dictionary with data on weather file.
    """
    weatherData = {}
    if not path:
        raise FileNotFoundError('File not found')
    else:
        with open(path, 'r') as csv_file:
            csvReader = csv.DictReader(csv_file)
            for row in csvReader:
                weatherData[row['PKT']] = {column.strip(): value for column, value in row.items()}
            csv_file.flush()
    return weatherData
