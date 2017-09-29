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


