"""EuclideanDistance2D"""
import math
def main():
    """main"""
    q1 = float(input())
    q2 = float(input())
    p1 = float(input())
    p2 = float(input())

    dis = math.sqrt(((q1 - p1) ** 2) + ((q2 - p2) ** 2))

    print(dis)

main()
