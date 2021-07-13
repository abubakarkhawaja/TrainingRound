import calendar

class WeatherMan:
    def generate_bar(size_of_bar: int) -> str:
        """
        Used to create bar of certain length made of '+' character

        @params
        :size_of_bar int: length of bar needed
        """
        return "".join(['+'] * size_of_bar)
    
    def print_month_year(date: str) -> None:
        """
        Print Month and date

        @params
        :date str: Contains date 'Year/Month'
        """
        month_number = int(date.split('/')[1])
        month = calendar.month_name[month_number]
        year = date.split('/')[0]
        print(month, year)
