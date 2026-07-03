"""student id"""
def main():
    """main"""
    num = input()
    x = 1
    is_three = False
    is_four = False

    for i in num:
        if x == 3 and i == "1":
            is_three = True
        if x == 4 and i == "6":
            is_four = True
        x += 1

    if is_four and is_three:
        print("yes")
    else:
        print("no")

main()
