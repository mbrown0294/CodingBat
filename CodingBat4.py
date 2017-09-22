def first_last6(nums):
  if (nums[0] == 6) | (nums[len(nums)-1] == 6):
    return True
  return False


def same_first_last(nums):
  if len(nums) < 1:
    return False;
  first = nums[0]
  last = nums[len(nums)-1]
  if first==last:
    return True
  return False


def make_pi():
  nums = [3,1,4]
  return nums


def common_end(a, b):
  firsta = a[0]
  firstb = b[0]
  lasta = a[len(a)-1]
  lastb = b[len(b)-1]
  if firsta == firstb:
    return True
  if lasta == lastb:
    return True
  return False