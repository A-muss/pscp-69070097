"""bigger pair"""
def main():
    """main"""
    num = int(input())
    text = []
    if num == 1:
        pair1 = int(input())
        pair2 = int(input())
        if pair1 > pair2:
            print(pair1)
        else:
            print(pair2)

    else:
        for _ in range(num):
            pair1 = int(input())
            pair2 = int(input())
            if pair1 > pair2:
                text.append(pair1)
            else:
                text.append(pair2)
        print(" + ".join((map(str, text))), "=", sum(text))
main()
