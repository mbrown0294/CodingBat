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


def array_count9(nums):
  count = 0
  for x in nums:
    if x == 9:
      count += 1
  return count


def array_front9(nums):
  leng = 4
  if len(nums) < leng:
    leng = len(nums)
  count = 0
  for x in xrange(leng):
    if nums[x] == 9:
      count += 1
  if count > 0:
    return True
  else:
    return False


def array123(nums):
  res = False
  count = 0
  ray = [1,2,3]
  for x in xrange(len(nums) - 2):
    if nums[x:x+3] == ray:
      res = True
  if count > 0:
    res = True
  return res


def string_match(a, b):
  count = 0
  leng = len(a)
  if len(b) < leng:
    leng = len(b)
  for x in xrange(leng - 1):
    if a[x:x+2] == b[x:x+2]:
      count += 1
  return count