import sys

items = {}

if not len(sys.argv) > 1:
    while True:
        try:
            item = input().upper()
            if item == "QUIT":
                break
            if item not in items:
                items[item] = 1
            else:
                items[item] += 1
        except EOFError:
            print()
            break
else:
    items = sys.argv[1:]


for key, value in sorted(items.items()):
    print(f"{value} {key}")
