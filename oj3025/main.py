"""season"""
def main():
    """main"""
    month = int(input())
    date = int(input())
    season_list = ["winter", "spring", "summer", "fall", "winter"]
    current_season = 0

    if 1 <= month <= 3:
        current_season = 0
    elif 4 <= month <= 6:
        current_season = 1
    elif 7 <= month <= 9:
        current_season = 2
    elif 10 <= month <= 12:
        current_season = 3

    if date >= 21 and (not month % 3):
        current_season += 1

    print(season_list[current_season])

main()
