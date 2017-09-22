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


