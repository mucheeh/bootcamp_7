def data_type(item):
  if type(item) == str:
    return(len(item))
  elif type(item) == bool:
    return item
  elif type(item)== int:
    if item < 100:
      return "less than 100"
    elif item > 100:
      return "more than 100"
    else:
      return "equal to 100"
  elif type(item) == list:
    if len(item) < 3:
      return None
    return item[2]
  elif item == None:
    return 'no value'