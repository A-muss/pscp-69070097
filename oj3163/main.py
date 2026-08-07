"""sin kha song ork"""
def main():
    """main"""
    num = int(input())
    even = odd = sum_all = 0
    for _ in range(num):
        amount = int(input())
        sum_all += amount
        if not amount%2:
            even += 1
        else:
            odd += 1
    print(f"SUM {sum_all}")
    print(f"EVEN {even}")
    print(f"ODD {odd}")
main()
