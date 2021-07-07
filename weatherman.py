
#to take command line argument
from codeFiles.tasks.task1 import task1
from codeFiles.tasks.task2 import task2
from codeFiles.tasks.task3 import task3
from codeFiles.tasks.task5 import task5

import sys

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