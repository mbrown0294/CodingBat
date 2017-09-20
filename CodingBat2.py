def string_times(str, n):
  numb = n - 1
  if n == 0:
    return ""
  elif n < 2:
    return str
  else:
    return str + string_times(str, numb)


def front_times(str, n):
  leng = 3
  if len(str) < leng:
    leng = len(str)
  word = str[:leng]
  ans = ""
  for x in xrange(n):
    ans += word
  return ans


def string_bits(str):
  return str[::2]
