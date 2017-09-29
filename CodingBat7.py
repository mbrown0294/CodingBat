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


