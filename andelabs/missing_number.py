def find_missing (list1, list2):

  if len(list1) < 0 and len(list2) < 0:
    return 0

  elif len(list1) == len(list2):
    return 0

  else:
     l = set(list2) - set(list1)
     number = list(l)
     return number[0]
