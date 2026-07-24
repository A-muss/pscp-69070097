"""brick bridge"""
def main():
    """main"""
    a = int(input())
    b = int(input())
    goal = int(input())

    b_req = goal // 5
    b_check = b - b_req
    if b_check < 0:
        b_req = b
    dis_left = goal - (b_req * 5)

    if dis_left > a:
        print(-1)
    else:
        print(dis_left)

main()
