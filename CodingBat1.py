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


def missing_char(str, n):
  words = str[:n] + str[(n+1):]
  return words


def front_back(str):
  first = str[:1]
  last = str[-1:]
  middle = str[1:-1]
  if len(str) < 2:
    return first
  return last + middle + first


def front3(str):
    if len(str) < 3:
        return str + str + str
    chunk = str[:3]
    return chunk + chunk + chunk
