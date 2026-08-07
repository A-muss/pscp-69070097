"""festival"""
def main():
    """main"""
    direction = input()
    x = y = 0
    for i in direction:
        match i:
            case 'N':
                y += 1
            case 'S':
                y -= 1
            case 'E':
                x += 1
            case 'W':
                x -= 1
    print(x, y, abs(x)+abs(y))
main()
