"""temperature"""
def main():
    """main"""
    temp = float(input())
    type1 = input().upper()
    type2 = input().upper()
    temp_c = 0

    match type1:
        case "C":
            temp_c = temp
        case "F":
            temp_c = ((temp - 32) * 5) / 9
        case "K":
            temp_c = temp - 273.15
        case "R":
            temp_c = ((temp * 5) / 9) - 273.15

    match type2:
        case "C":
            temp_final = temp_c
        case "F":
            temp_final = ((temp_c * 9) / 5) +32
        case "K":
            temp_final = temp_c + 273.15
        case "R":
            temp_final = ((temp_c + 273.15) * 9) / 5

    print(f"{temp_final:.2f}")

main()
