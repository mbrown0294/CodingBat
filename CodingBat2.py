def string_times(str, n):
  numb = n - 1
  if n == 0:
    return ""
  elif n < 2:
    return str
  else:
    return str + string_times(str, numb)


