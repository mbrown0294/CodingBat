def sleep_in(weekday, vacation):
    return (not weekday) or vacation


def diff21(n):
    diff = n - 21
    if diff > 0:
        return (diff) * 2
    else:
        return diff * -1


def near_hundred(n):
    diff1 = n - 100
    diff2 = n - 200
    if (abs(diff1) <= 10) | (abs(diff2) <= 10):
        return True
    else:
        return False