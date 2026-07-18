"""castle"""
def main(): # didnt use ai btw
    """main"""
    position = int(input())
    last_level_num = 1 # the last room number on that floor
    level_room = 1 # uh, a number of room on that floor or somtin like that idk
    level = 1 # isnt ts obvious

    if position == 1:
        print(0)
    else:
        while position > last_level_num:
            level_room += 2
            last_level_num += level_room
            level += 1
        odd_even_checker = last_level_num - position
        if odd_even_checker % 2: #odd == up
            wall_break = ((level - 1) * 2) - 1
        else: #even == down
            wall_break = (level - 1) * 2

        print(wall_break)

        # print("ans", wall_break)
        # print("last room number", last_level_num)
        # print("level room", level_room)
        # print("level", level)

main()
