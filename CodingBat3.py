def hello_name(name):
  return "Hello " + name + "!"


def make_abba(a, b):
  return a + b + b + a


def make_tags(tag, word):
  return "<" + tag + ">" + word + "</" + tag + ">"


def make_out_word(out, word):
  one = out[:2]
  two = out[-2:]
  return one + word + two


def extra_end(str):
  end = str[-2:]
  return end + end + end


def first_two(str):
  return str[:2]


def first_half(str):
  leng = len(str) / 2
  return str[:leng]


def without_end(str):
  return str[1:-1]


def combo_string(a, b):
  sho = a
  lon = b
  if len(a) > len(b):
    lon = a
    sho = b
  return sho  + lon + sho


def non_start(a, b):
  return a[1:] + b[1:]


def left2(str):
  if len(str) == 2:
    return str
  return str[2:] + str[:2]
