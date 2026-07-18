"""ink"""
import math
def main():
    """main"""
    speed_sq, amount = map(int, input().split())
    for _ in range(amount):
        x, y = map(int, input().split())
        dis = math.sqrt((x ** 2) +(y ** 2))
        time = (3.1416 * (dis ** 2)) / speed_sq
        print(math.ceil(time))

main()
