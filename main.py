import argparse
from sourcecode.driver import Driver

def main(args):
    """
    Uses options given by command line argument.
    And calls their respective function.
    """
    directory_path = args.pathToDirectory
    driver = Driver(directory_path)

    if args.e:
        print('\nWeather Data by Year:')
        driver.getReport('e', args.e)
        print('\n')
    if args.a:
        print('\nWeather Data by Year & Month:')
        driver.getReport('a', args.a)
        print('\n')
    if args.c:
        print('\nWeather Data by Year & Month with Coloured Bars')
        driver.getReport('c', args.c)
    if args.d:
        print('\nWeather Data by Year & Month with Coloured Bars (Bonus)')
        driver.getReport('d', args.d)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pathToDirectory", help="Path to directory")
    parser.add_argument("-e", help="Weather Data by Year. i.e. -e 2011")
    parser.add_argument("-a", help="Weather Data by Month & Year. i.e. -a 2011/8")
    parser.add_argument("-c", help="Weather Data by Month & Year with Bar. i.e. -c 2004/8")
    parser.add_argument("-d", help="Weather Data by Month & Year with Bar Bonus. i.e. -d 2004/8")
    args = parser.parse_args()
    main(args)
