"""Elo"""
def main():
    """main"""
    RA = int(input())
    RB = int(input())
    winner = input()

    EA = 1 / (1+(10 ** ((RB - RA) / 400)))
    EB = 1 / (1+(10 ** ((RA - RB) / 400)))

    if winner == 'A':
        print(f"{EA:.2f}")
    else:
        print(f"{EB:.2f}")

main()
