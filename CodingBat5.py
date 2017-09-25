def cigar_party(cigars, is_weekend):
  rep = False
  if (cigars <= 60) & (cigars >= 40):
    rep = True
  if(is_weekend):
    if(cigars >= 40):
      rep = True
  return rep


def date_fashion(you, date):
  rep = 1
  if (you >= 8) | (date >= 8):
    rep = 2
  if(you <= 2) | (date <=2):
    rep = 0
  return rep


def squirrel_play(temp, is_summer):
  if(is_summer):
    if(temp <= 100) & (temp >= 60):
      return True
    return False
  if(temp >= 60) & (temp <= 90):
    return True
  return False


def caught_speeding(speed, is_birthday):
  if(is_birthday):
    if(speed <= 65):
      return 0
    elif(speed >= 86):
      return 2
    return 1
  if(speed <= 60):
    return 0
  elif(speed >= 81):
    return 2
  return 1


def sorta_sum(a, b):
  res = a + b
  if (res <= 19) & (res >= 10):
    res = 20
  return res


def alarm_clock(day, vacation):
    if (vacation):
        if ((day == 0) | (day == 6)):
            return "off"
        else:
            return "10:00"
    else:
        if ((day == 0) | (day == 6)):
            return "10:00"
        else:
            return "7:00"


def love6(a, b):
  add = a + b
  sub = abs(a - b)
  if((a==6) | (b==6) | (add==6) | (sub==6)):
    return True
  else:
    return False


def in1to10(n, outside_mode):
  if (outside_mode):
    if (n <= 1) | (n >= 10):
      return True
  else:
    if (n >= 1) & (n <= 10):
      return True
  return False


def near_ten(num):
  for x in xrange(3):
    if ((num + x) % 10) == 0:
      return True
    elif ((num - x) % 10) == 0:
      return True
  return False
