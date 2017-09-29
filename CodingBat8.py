def count_evens(nums):
  count = 0
  for x in nums:
    if x % 2 == 0:
      count += 1
  return count


def big_diff(nums):
    large = nums[0]
    small = nums[0]
    for x in nums:
        if x > large:
            large = x
        if x < small:
            small = x
    return large - small


def centered_average(nums):
  new = list(nums)
  large = new[0]
  small = new[0]
  size = len(new) - 2
  for x in range(len(new)):
    if new[x] > large:
      large = new[x]
    if new[x] < small:
      small = new[x]
  new.remove(small)
  new.remove(large)
  sum = 0
  for x in new:
    sum += x
  return sum / size


def sum13(nums):
  sum = 0
  for x in range(len(nums)):
    if (nums[x] == 13) | ((nums[x-1] == 13) & (x != 0)):
      sum += 0
    else:
      sum += nums[x]
  return sum


