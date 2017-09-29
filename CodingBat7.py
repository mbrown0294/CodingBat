def double_char(str):
  phrase = ""
  for x in range(len(str)):
    phrase += str[x] + str[x]
  return phrase


def count_hi(str):
  count = 0
  for x in range(len(str)-1):
    if str[x:x+2] == "hi":
      count += 1
  return count


def cat_dog(str):
    countC = 0
    countD = 0
    for x in range(len(str) - 2):
        if str[x:x + 3] == "cat":
            countC += 1
        if str[x:x + 3] == "dog":
            countD += 1
    return countC == countD


def count_code(str):
  count = 0
  for x in range(len(str) - 3):
    if (str[x:x+2] == "co") & (str[x+3] == "e"):
      count += 1
  return count


def end_other(a, b):
  newA = a.lower()
  newB = b.lower()
  big = newA
  small = newB
  if(len(b) > len(a)):
    big = newB
    small = newA
  boo = False
  start = len(big) - len(small)
  end = len(big)
  if big[start:] == small:
    boo = True
  return boo


