def sleep_in(weekday, vacation):
    return (not weekday) or vacation


def diff21(n):
    diff = n - 21
    if diff > 0:
        return (diff) * 2
    else:
        return diff * -1