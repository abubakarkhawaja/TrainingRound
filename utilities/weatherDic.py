
def getWeatherDic (PATH):
    weather_data = {}
    column = []

    with open(PATH) as file:

        flag = True
        for content in file.readlines():
            # condtion to read column names
            if flag:
                column = content.split(',')
                flag = False
            else:        
                # from 1 because dont want to read columns again s
                for i in range(1, len(content)):
                    # takinng values of first lines
                    column_data = content.split(',')
                    # using date as key for dictionary
                    weather_data[column_data[0]] = {}
            
                    for k in range(len(column)):
                        # saving values in their respective column according to date
                        key = column[k].strip()
                        weather_data[column_data[0]][key] = content.split(',')[k].strip()
    return weather_data