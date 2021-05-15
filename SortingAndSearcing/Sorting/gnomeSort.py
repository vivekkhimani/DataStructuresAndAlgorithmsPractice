from common.helpers import default_compare

def sort(array, compare=default_compare):
  pos = 1
  while pos < len(array):
    if compare(array[pos], array[pos - 1]) >= 0:
      pos += 1
    else:
      array[pos], array[pos - 1] = array[pos - 1], array[pos]
      if pos > 1:
        pos -= 1
