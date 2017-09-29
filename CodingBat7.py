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


