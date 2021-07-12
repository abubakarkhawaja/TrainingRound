import os
import calendar
import csv


def get_weather_files(date: str, path: str) -> list[str]:
    """
    Gets date and directory path. 
    Base on these returns file names.

    Parameters:
        date (str): Date entered by user as command line argument
        path (str): Contains path to weather files directory

    Returns:
        list: list of full path to weather files
    Raises:
        IOError: File not found    
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
    
    Parameters:
        path (str): Contains path to weather file directory

    Returns:
        dict: returns dictionary with data on weather file.
    """
    weatherData = {}
    columns = []
    with open(path, 'r') as csv_file:
        csvReader = csv.reader(csv_file, delimiter=',')
        lineCount = 0
        for line in csvReader:
            if lineCount == 0:
                columns = list(map(str.strip, line))
                lineCount+=1
            else:        
                for i in range(1, len(line)):
                    row = line
                    date = row[0]
                    weatherData[date] = {}
                    for j in range(1, len(columns)):
                        columnName = columns[j]
                        weatherData[date][columnName] = line[j]
        csv_file.flush()
    return weatherData
