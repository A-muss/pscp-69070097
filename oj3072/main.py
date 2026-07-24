"""A-E-I-O-U"""
def main():
    """main"""
    alpha = [str(x) for x in input().lower()]
    a = alpha.count('a')
    e = alpha.count('e')
    i = alpha.count('i')
    o = alpha.count('o')
    u = alpha.count('u')

    if a > 0:
        print(f"a : {a}")
    if e > 0:
        print(f"e : {e}")
    if i > 0:
        print(f"i : {i}")
    if o > 0:
        print(f"o : {o}")
    if u > 0:
        print(f"u : {u}")

main()
