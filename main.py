import argparse

from sourcecode.weatherByYear.weatherman import weather_by_year
from sourcecode.weatherByYearMonth.weatherman import weather_by_year_month
from sourcecode.weatherByYearMonthBar.weatherman import weather_by_year_month_bar
from sourcecode.bonus.weatherman import weather_by_year_month_bar_bonus 

def main(args):
    """
    Uses options given by command line argument.
    And calls their respective function.
    """
    pathToDirectory = args.pathToDirectory
    if args.e:
        print('\nWeather Data by Year:')
        weather_by_year(pathToDirectory, date=args.e)
        print('\n')
    if args.a:
        print('\nWeather Data by Year & Month:')
        weather_by_year_month(pathToDirectory, date=args.a)
        print('\n')
    if args.c:
        print('\nWeather Data by Year & Month with Coloured Bars')
        weather_by_year_month_bar(pathToDirectory, date=args.c)
    if args.d:
        print('\nWeather Data by Year & Month with Coloured Bars (Bonus)')
        weather_by_year_month_bar_bonus(pathToDirectory, date=args.d)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pathToDirectory", help="Path to directory")
    parser.add_argument("-e", help="Weather Data by Year. i.e. -e 2011")
    parser.add_argument("-a", help="Weather Data by Month & Year. i.e. -a 2011/8")
    parser.add_argument("-c", help="Weather Data by Month & Year with Bar. i.e. -c 2004/8")
    parser.add_argument("-d", help="Weather Data by Month & Year with Bar Bonus. i.e. -d 2004/8")
    args = parser.parse_args()
    main(args)
