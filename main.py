from os import path
import sys

from sourcecode.weatherByYear.weatherman import task1
from sourcecode.weatherByYearMonth.weatherman import task2
from sourcecode.weatherByYearMonthBar.weatherman import task3
from sourcecode.bonus.weatherman import task5 

# ex_path = "/Users/abubakarkhawaja/Documents/weatherfiles/"

def main():
    """
    Summary:
        Uses options given by command line argument.
        And calls their respective function.
    """
    arguments = sys.argv
    pathToDirectory = arguments[1]

    if "-e" in arguments:
        print('\nTask 1:')
        # arguments[arguments.index('-e')+1] is used to get the Date
        # which will be written after tag/option ('-e') 
        task1(pathToDirectory, arguments[arguments.index('-e')+1])
        print('\n')
    if "-a" in arguments:
        print('\nTask 2:')
        task2(pathToDirectory, arguments[arguments.index('-a')+1])
        print('\n')
    if "-c" in arguments:
        print('\nTask 3:')
        task3(pathToDirectory, arguments[arguments.index('-c')+1])
    if "-d" in arguments:
        print('\nTask 5:')
        task5(pathToDirectory, arguments[arguments.index('-d')+1])

if __name__ == "__main__":
    main()
