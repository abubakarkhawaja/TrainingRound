#to take command line argument
import sys

from sourcecode.weatherByYear.weatherman import task1
from sourcecode.weatherByYearMonth.weatherman import task2
from sourcecode.weatherByYearMonthBar.weatherman import task3
from sourcecode.bonus.weatherman import task5 

# ex_path = "/Users/abubakarkhawaja/Documents/weatherfiles/"

def main():
    arguments = sys.argv

    if "-e" in arguments:
        print('\nTask 1:')
        task1(arguments[1],arguments[arguments.index('-e')+1])
        print('\n')
    if "-a" in arguments:
        print('\nTask 2:')
        task2(arguments[1],arguments[arguments.index('-a')+1])
        print('\n')
    if "-c" in arguments:
        print('\nTask 3:')
        task3(arguments[1],arguments[arguments.index('-c')+1])
    if "-d" in arguments:
        print('\nTask 5:')
        task5(arguments[1],arguments[arguments.index('-d')+1])

if __name__ == "__main__":
    main()