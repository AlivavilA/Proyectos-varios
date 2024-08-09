question = input("What is the Answer to the great Question of Life, the universe and everything? ")

match question:
    case "42" | "Forty Two" | "forty-two":
        print("Yes")
    case _:
        print("No")