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


def monkey_trouble(a_smile, b_smile):
  if (a_smile and b_smile) or not (a_smile or b_smile):
    return True
  else:
    return False


def parrot_trouble(talking, hour):
  var = False
  if hour < 7 or hour > 20:
    var = True
  if var == True and talking == True:
    return True
  else:
    return False


def pos_neg(a, b, negative):
  if negative:
    if a < 0 and b < 0:
      return True
    else:
      return False
  else:
    if (a < 0 and b > 0) or (a > 0 and b < 0):
      return True
    else:
      return False


def sum_double(a, b):
  if a==b:
    return 4*a
  else:
    return a + b


def makes10(a, b):
  if a==10 or b==10 or (a+b==10):
    return True
  else:
    return False


def not_string(str):
  start = str[:3]
  if start == "not":
    return str
  return "not " + str


