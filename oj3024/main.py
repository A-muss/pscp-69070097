"""surprisingVote"""
def main():
    """main"""
    all_point = float(input())
    hightest_point = float(input())
    point_left = all_point - hightest_point

    lowest_possible_point = point_left - hightest_point

    if lowest_possible_point < 0:
        lowest_possible_point = 0

    if hightest_point - lowest_possible_point > 2:
        print("Surprising")
    else:
        print("Not surprising")

main()
