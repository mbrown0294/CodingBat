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


