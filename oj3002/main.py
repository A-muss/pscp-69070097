"""password"""
def main():
    """main"""
    name = input()
    sur_name = input()
    age = input()

    if len(name) >= 5 and len(sur_name) >= 5:
        password = name[:2] + sur_name[:-2:-1] + age[:-2:-1]
    else:
        password = name[:1] + age + sur_name[:-2:-1]

    print(password)

main()
