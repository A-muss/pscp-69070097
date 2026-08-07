"""sum square"""
def main():
    """main"""
    num = int(input())
    ans = 0
    for i in range(1, num+1):
        ans += i ** 2
    print(ans)
main()
