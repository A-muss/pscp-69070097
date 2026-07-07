"""colors"""
def main():
    """main"""
    color1 = input()
    color2 = input()
    primary_colors = ["Red", "Yellow", "Blue"]
    color_list = [color1, color2]

    if color1 not in primary_colors or color2 not in primary_colors:
        print("Error")
        return

    if color1 == color2:
        print(color1)
        return

    if "Red" in color_list and "Yellow" in color_list:
        print("Orange")
    elif "Red" in color_list and "Blue" in color_list:
        print("Violet")
    elif "Yellow" in color_list and "Blue" in color_list:
        print("Green")

main()
