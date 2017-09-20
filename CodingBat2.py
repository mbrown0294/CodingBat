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


def string_splosion(str):
  leng = len(str)
  if leng <= 0:
    return ""
  phrase = ""
  count = 1
  for x in xrange(leng):
    phrase += str[:count]
    count += 1
  return phrase


def last2(str):
  phr = str[-2:]
  count = 0
  for x in xrange(len(str) - 2):
    if str[x:x +2] == phr:
      count += 1
  return count