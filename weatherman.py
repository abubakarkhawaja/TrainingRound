from tasks.task3 import task3
from tasks.task2 import task2
from tasks.task1 import task1
from tasks.task5 import task5
#to take command line argument
import sys


def main():
    arguments = sys.argv

    if "-e" in arguments:
        print('Task 1:')
        task1('/Users/abubakarkhawaja/Documents/weatherfiles/',arguments[arguments.index('-e')+1])
        print('\n')
    if "-a" in arguments:
        print('Task 2:')
        task2('/Users/abubakarkhawaja/Documents/weatherfiles/',arguments[arguments.index('-a')+1])
        print('\n')
    if "-c" in arguments:
        print('Task 3:')
        task3('/Users/abubakarkhawaja/Documents/weatherfiles/',arguments[arguments.index('-c')+1])
    if "-d" in arguments:
        print('Task 5:')
        task5('/Users/abubakarkhawaja/Documents/weatherfiles/',arguments[arguments.index('-d')+1])

if __name__ == "__main__":
    main()