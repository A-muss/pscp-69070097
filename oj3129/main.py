"""coffee shop"""
def main():
    """main"""
    num = int(input())
    income_list = []
    for _ in range(num):
        income_list.append(int(input()))
    print(sum(income_list))
    print(max(income_list))
    print(min(income_list))
    print(f"{sum(income_list)/len(income_list):.1f}")
main()
