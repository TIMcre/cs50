filename = input("File name: ").lower().strip().split(".")
match filename[-1]:
    case "gif":
        print("image/gif")
    case "jpg":
        print("image/jpeg")
    case "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")

# doing it with a dictonary would have been nicer and more accsesebil but i only just thought of that.
