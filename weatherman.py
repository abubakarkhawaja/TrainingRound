import argparse

from sourcecode.weather_report_controller import WeatherReportController


class Driver:
    def main(args: argparse.Namespace) -> None:
        """        
        Uses options given by command line argument.
        And calls their respective function.
        
        @params
        :args argparse.Namespace: contains sequence of arguments with values.
        """
        directory_path = args.pathToDirectory
        weather_factory = WeatherReportController(directory_path)
        
        if args.e:
            print('\nWeather Data by Year:')
            weather_factory.report('e', args.e)
            print('\n')

        if args.a:
            print('\nAverage Weather Data of Month:')
            weather_factory.report('a', args.a)
            print('\n')
        
        if args.c:
            print('\nDaily Weather Data with Seperate Bar')
            weather_factory.report('c', args.c)
        
        if args.d:
            print('\nDaily Weather Data with Single Bar')
            weather_factory.report('d', args.d)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pathToDirectory", help="Path to directory")
    parser.add_argument("-e", help="Weather Data by Year. i.e. -e 2011")
    parser.add_argument("-a", help="Weather Data by Month & Year. i.e. -a 2011/8")
    parser.add_argument("-c", help="Weather Data by Month & Year with Bar. i.e. -c 2004/8")
    parser.add_argument("-d", help="Weather Data by Month & Year with Bar Bonus. i.e. -d 2004/8")
    args = parser.parse_args()

    Driver.main(args)
