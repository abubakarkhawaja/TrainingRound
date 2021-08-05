import argparse, os

from sourcecode.weather_reports_display import WeatherReportsDisplay


def main(args: argparse.Namespace) -> None:
    """        
    Uses options given by command line argument.
    And calls their respective function.
    
    @params
    :args argparse.Namespace: contains sequence of arguments with values.
    """
    files_path = complete_paths(args.pathToDirectory)
    
    weather_report = WeatherReportsDisplay(files_path)

    if args.e:
        print('\nWeather Data by Year:')
        weather_report.display_extreme_report_of_year(args.e)            
        print('\n')

    if args.a:
        print('\nAverage Weather Data of Month:')
        weather_report.display_average_report_of_month(args.a)
        print('\n')
    
    if args.c:
        print('\nDaily Weather Data with Seperate Bar')
        weather_report.display_report_bar(args.c)
    
    if args.d:
        print('\nDaily Weather Data with Single Bar')
        weather_report.display_report_single_bar(args.d)

def complete_paths(directory_path):
    try:
        files_names = os.listdir(directory_path)
    except IOError:
        print('Directory Not Found!')
    else:
        complete_files_paths = [directory_path + file_name for file_name in files_names]
        
        return complete_files_paths

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("pathToDirectory", help="Path to directory")
    parser.add_argument("-e", help="Weather Data by Year. i.e. -e 2011")
    parser.add_argument("-a", help="Weather Data by Month & Year. i.e. -a 2011/8")
    parser.add_argument("-c", help="Weather Data by Month & Year with Bar. i.e. -c 2004/8")
    parser.add_argument("-d", help="Weather Data by Month & Year with Bar Bonus. i.e. -d 2004/8")
    args = parser.parse_args()

    main(args)
