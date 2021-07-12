import sys

from sourcecode.weatherByYear.weatherman import weather_by_year
from sourcecode.weatherByYearMonth.weatherman import weather_by_year_month
from sourcecode.weatherByYearMonthBar.weatherman import weather_by_year_month_bar
from sourcecode.bonus.weatherman import weath_by_year_month_bar_bonus 

def main():
    """
    Uses options given by command line argument.
    And calls their respective function.
    """
    arguments = sys.argv
    pathToDirectory = arguments[1]

    if "-e" in arguments:
        print('\nTask 1:')
        weather_by_year(pathToDirectory, date=arguments[arguments.index('-e')+1])
        print('\n')
    if "-a" in arguments:
        print('\nTask 2:')
        weather_by_year_month(pathToDirectory, date=arguments[arguments.index('-a')+1])
        print('\n')
    if "-c" in arguments:
        print('\nTask 3:')
        weather_by_year_month_bar(pathToDirectory, date=arguments[arguments.index('-c')+1])
    if "-d" in arguments:
        print('\nTask 5:')
        weath_by_year_month_bar_bonus(pathToDirectory, date=arguments[arguments.index('-d')+1])

if __name__ == "__main__":
    main()
