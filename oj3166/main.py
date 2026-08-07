"""pass/fail average"""
def main():
    """main"""
    num = int(input())
    all_score = 0
    status = "FAIL"
    for _ in range(num):
        score = int(input())
        if score < 50:
            status = "FAIL"
        all_score += score
    if all_score / num > 60 and status != "FAIL":
        print("PASS")
    else:
        print('FAIL')
    print(f"{all_score / num:.1f}")
main()
