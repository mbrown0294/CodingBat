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


