import os
import calendar
import pandas as pd


def get_Weather_Info(path: str) -> dict[str, dict]:
    """
    Summary:
        Used to read text file and cleans data. and generates dictionary.

    Args:
        path (str): [Contains file complete path]

    Returns:
        dict: [dictionary inside a dictionary]
    """

    try:
        df = pd.read_csv(path)
    except IOError:
        print("File not found")
    else:
        # cleaning
        df.columns = df.columns.str.strip()
        df = df.set_index('PKT')
        df.dropna(subset = ['Max TemperatureC', 'Mean TemperatureC', 'Min TemperatureC', 
                            'Max Humidity', 'Mean Humidity', 'Min Humidity'], 
                            how='any', inplace=True)

        # filling data in dictionary
        weather_data = {date : {column : df[column][date] for column in df.columns} for date in df.index.values}    
        return weather_data


def get_Weather_Files(date: str, path: str) -> list[str]:
    """
    Summary:
        Gets date and directory path. 
        Base on these returns file names.

    Args:
        date (str): Date entered by user as command line argument
        path (str): Contains path to weather files directory

    Returns:
        list: list of full path to weather files
    """

    try:
        directory = os.listdir(path)
    except IOError:
        print("File not found")
    else:
        if '/' in date:
            # It means year with month was given as command line argument
            monthNumber = int(date.split('/')[1])
            month = calendar.month_abbr[monthNumber]
            year = date.split('/')[0]
            weatherFiles = [dir for dir in directory if year in dir and month in dir]        
        else: 
            # It means only year was given as command line argument
            weatherFiles = [dir for dir in directory if date in dir]
        return weatherFiles


# def get_Weather_Info(path: str) -> dict[str, dict]:
    # weather_data = {}
    # column = []
    # with open(path, 'r') as file:
    #     flag = True
    #     for content in file.readlines():
    #         # condtion to read column names
    #         if flag:
    #             column = content.split(',')
    #             flag = False
    #         else:        
    #             # from 1 because dont want to read columns again s
    #             for i in range(1, len(content)):
    #                 # takinng values of first lines
    #                 column_data = content.split(',')
    #                 if column_data[1] == "":
    #                     continue
    #                 # using date as key for dictionary
    #                 weather_data[column_data[0]] = {}
    #                 for k in range(len(column)):
    #                     # saving values in their respective column according to date
    #                     key = column[k].strip()
    #                     weather_data[column_data[0]][key] = content.split(',')[k].strip()
    #     file.flush()
    # return weather_data
