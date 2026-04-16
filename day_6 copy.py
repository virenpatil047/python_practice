Reeborg's World : Maze Problem

def face_right():
    turn_left()
    turn_left()
    turn_left()

while not is_facing_north():
    turn_left()

while not wall_in_front():
    move()

while not at_goal():
    if right_is_clear():
        face_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
