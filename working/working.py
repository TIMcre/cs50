import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    s.strip()
    if match := re.search(
        r"([1-9]|1[0-2])(:([0-5][0-9])|60)? (AM|PM) to ([1-9]|1[0-2])(:([0-5][0-9])|60)? (AM|PM)",
        s,
    ):
        times_old = [
            {
                "key": str(match.group(4)),
                "hour": int(match.group(1)),
                "minutes": str(match.group(3)) if match.group(3) else "00",
            },
            {
                "key": str(match.group(8)),
                "hour": int(match.group(5)),
                "minutes": str(match.group(7)) if match.group(7) else "00",
            },
        ]

        times = []

        for time in times_old:
            times.append(convertTime(time))

        return f'{times[0]["hour"]:02}:{times[0]["minutes"]} to {times[1]["hour"]:02}:{times[1]["minutes"]}'

    raise ValueError

def convertTime(time):
    if time["hour"] == 12:
        match time["key"]:
            case "AM":
                time["hour"] = 00
            case "PM":
                time["hour"] = 12

    elif time["key"] == "PM":
        time["hour"] += 12

    return time

if __name__ == "__main__":
    main()
