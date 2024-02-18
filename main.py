"""
CMPS 2200  Assignment 1.
See assignment-01.pdf for details.
"""
# no imports needed.


def foo(x):
  if x <= 1:
    return x
  else:
    return foo(x - 1) + foo(x - 2)


def longest_run(mylist, key):
  max_seq = 0
  current = 0
  for i in mylist:
    if i == key:
      current += 1
      if current > max_seq:
        max_seq = current
    else:
      current = 0
  return max_seq


class Result:
  """ done """

  def __init__(self, left_size, right_size, longest_size, is_entire_range):
    self.left_size = left_size  # run on left side of input
    self.right_size = right_size  # run on right side of input
    self.longest_size = longest_size  # longest run in input
    self.is_entire_range = is_entire_range  # True if the entire input matches the key

  def __repr__(self):
    return ('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
            (self.longest_size, self.left_size, self.right_size,
             self.is_entire_range))


def to_value(v):
  """
    if it is a Result object, return longest_size.
    else return v
    """
  if type(v) == Result:
    return v.longest_size
  else:
    return int(v)


def longest_run_recursive(mylist, key):
  # Base Case when mylist = 1
  if len(mylist) == 1:
    if mylist[0] == key:
      return Result(1, 1, 1, True)
    else:
      return Result(0, 0, 0, False)  # there are no runs of key in mylist
  else:
    # THIS IS THE RECURSIVE STEP

    mid = len(mylist) // 2
    l = longest_run_recursive(mylist[:mid], key)
    r = longest_run_recursive(mylist[mid:], key)

    # The left side is all the key (not the right side)
    if l.is_entire_range and r.is_entire_range == False:
      return Result(l.longest_size + r.left_size, r.right_size,
                    max(l.longest_size + r.left_size, r.longest_size), False)

    # The right side is all the key (not the left side)
    elif r.is_entire_range and l.is_entire_range == False:
      return Result(l.left_size, l.right_size + r.longest_size,
                    max(l.right_size + r.longest_size, l.longest_size), False)

    # left AND right side are all the key
    elif (l.is_entire_range and r.is_entire_range) == True:
      return Result(l.longest_size + r.longest_size,
                    l.longest_size + r.longest_size,
                    l.longest_size + r.longest_size, True)
    # neither left or right side are all the key
    else:
      return Result(
          l.left_size, r.right_size,
          max(l.longest_size, r.longest_size, l.right_size + r.left_size),
          False)
