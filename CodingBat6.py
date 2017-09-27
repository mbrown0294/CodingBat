def make_bricks(small, big, goal):
    rep = False
    if small >= goal:
        rep = True
    elif goal / 5 <= big:
        if (goal % 5 == 0):
            rep = True
        elif goal % 5 <= small:
            rep = True
    elif ((big * 5) + small) >= goal:
        rep = True
    return rep


def lone_sum(a, b, c):
  if a == b:
    if a == c:
      return 0
    else:
      return c
  elif a == c:
    return b
  elif b == c:
    return a
  else:
    return a + b + c


def lucky_sum(a, b, c):
  nums = [a,b,c]
  sum = 0
  for x in nums:
    if x == 13:
      return sum
    else:
      sum += x
  return sum


def no_teen_sum(a, b, c):
    numa = fix_teen(a)
    numb = fix_teen(b)
    numc = fix_teen(c)
    return numa + numb + numc


def fix_teen(n):
    if (n == 15) | (n == 16):
        return n
    elif (n >= 13) & (n <= 19):
        return 0
    else:
        return n


def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
def round10(num):
  if num < 5:
    return 0
  elif num < 10:
    return 10
  elif num % 10 < 5:
    return num - (num % 10)
  else:
    return num + (10 - (num % 10))
  return 0


