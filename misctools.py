def checknum(msg, errmsg=None, division=False, divzeromsg=None, forceint=False, forcepos=False, negmsg=None):
    while True:
        num = input(msg)    # asks for a number with the provided message

        try:
            num = float(num)    # tries making it a float

            if num % 1 == 0 or forceint is True:
                num = int(num)  # makes it an int if that's what it's wanted to or should be

            if division is True:
                if num == 0:
                    if divzeromsg is not None:
                        print(divzeromsg)   # tells you you can't divide by zero if a message has been provided
                    continue

            if forcepos is True and num <= 0:
                if negmsg is not None:
                    print(negmsg)   # tells you the number can't be negative if a message has been provided
                continue

            break
        except ValueError:
            if errmsg is not None:
                print(errmsg)   # tells you your value is invalid if a message has been provided
            continue
    return num


def sign(date):
    print('\n Made by Leevi Aaltonen \n\n', date)


def clear():
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
