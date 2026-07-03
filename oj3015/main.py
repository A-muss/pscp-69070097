"""Pro"""
def main():
    """main"""
    x = int(input())
    y = int(input())
    a = int(input())
    z = int(input())
    time = z // x
    price = z * a

    dis = x - y
    if time > 0:
        price -= time * (dis * a)

    print(price)

main()
