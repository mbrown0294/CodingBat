def make_bricks(small, big, goal):
    rep = False
    if small >= goal:
        rep = True
    elif goal / 5 <= big:
        if (goal % 5 == 0):
            rep = True
        elif goal % 5 <= small:
            rep = True
    elif ((big * 5) + small) >= goal:
        rep = True
    return rep


