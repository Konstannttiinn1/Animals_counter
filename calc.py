cash = int(input())

def count(cash):
    if cash >= 6796:
        print(int(cash / 6796), "sheep")
    elif cash >= 3848:
        if int(cash / 3848) > 1:
            print(int(cash / 3848), "cows")
        else:
            print("1", "cow")
    elif cash >= 1296:
        if int(cash / 1296) > 1:
            print(int(cash / 1296), "pigs")
        else:
            print("1", "pig")
    elif cash >= 678:
        if int(cash / 678) > 1:
            print(int(cash / 678), "goats")
        else:
            print("1", "goat")
    elif cash >= 23:
        if int(cash / 23) == 1:
            print("1", "chicken")
        else:
            print(int(cash / 23), "chickens")
    else:
        print("None")

count(cash)
