def cigar_party(cigars, is_weekend):
  rep = False
  if (cigars <= 60) & (cigars >= 40):
    rep = True
  if(is_weekend):
    if(cigars >= 40):
      rep = True
  return rep


