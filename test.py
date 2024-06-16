import datetime


current_date = datetime.date.today()
current_date = datetime.datetime.fromtimestamp(1709640000) #DEV
weekday = current_date.strftime("%A")
formatted_date = current_date.strftime("%d %m %Y")
week_number = current_date.isocalendar()[1]

print("---INFO---")
print("Current Date:", formatted_date)
print("Weekday:", weekday)
print("ISO Week Number:", week_number)
print("----------")


def main():
    if week_number % 2 != 0 and weekday != "Thursday":
        return

    print("Let's go")
    next_saturday_date = find_next_saturday()
    print(f"JF Dienst {next_saturday_date.strftime('%d.%m.%Y')} 15:00 - 18:00 Uhr")


def find_next_saturday(today=datetime.date.today()):
    today = datetime.datetime.fromtimestamp(1709640000)  # DEV
    days_until_saturday = (5 - today.weekday() + 7) % 7
    next_saturday = today + datetime.timedelta(days=days_until_saturday)

    return next_saturday


if __name__ == "__main__":
    main()
