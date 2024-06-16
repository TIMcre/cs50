import sys
from datetime import date
import inflect as inflectimport

inflect = inflectimport.engine()


def main():
    pastDate = getDate()
    curDate = date.today()
    minutes = getDateDifMinutes(pastDate, curDate)
    print(inflect.number_to_words(minutes, andword="").capitalize() + " minutes")


def getDate():
    while True:
        try:
            year, month, day = str(input("Date: ")).rstrip().split("-")
            return date(int(year), int(month), int(day))
        except:
            sys.exit("not a Valid Date")


def getDateDifMinutes(past, cur):
    difDate = cur - past
    return round(difDate.total_seconds() / 60)


if __name__ == "__main__":
    main()
