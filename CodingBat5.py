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


