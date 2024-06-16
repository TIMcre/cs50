import re


def is_valid(date):
    if re.match("\d{1,2}\/\d{1,2}\/\d{4}", date):
        old_date = date.split("/")
        if int(old_date[0]) < 12 and int(old_date[1]) < 31:
            old_date[0], old_date[1] = old_date[0].zfill(2), old_date[1].zfill(2)
            old_date.insert(0, old_date.pop(2))
            return True, old_date

    elif re.match("[A-Z][a-z]{2,9} \d{1,2}, \d{4}$", date):
        old_date = date.replace(",", "").split(" ")
        if old_date[0] in months:
            old_date[0] = str(months.index(old_date[0]) + 1)
            if int(old_date[0]) < 12 and int(old_date[1]) < 31:
                old_date[0], old_date[1] = old_date[0].zfill(2), old_date[1].zfill(2)
                old_date.insert(0, old_date.pop(2))
                return True, old_date

    else:
        return False


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]


while True:
    user_input = input("Date: ").strip()

    date_return = is_valid(user_input)
    if date_return:
        break
print("-".join(date_return[1]))


# really nasty code but i just couldnt quite wrap my head a round a esier way so here we are
