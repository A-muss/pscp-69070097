"""bill"""
def main():
    """main"""
    food_price = int(input())
    service_price = food_price * 0.1

    if service_price < 50:
        service_price = 50
    elif service_price > 1000:
        service_price = 1000

    vat = (food_price + service_price) * 0.07
    final_price = vat + service_price + food_price

    print(f"{final_price:.2f}")

main()
