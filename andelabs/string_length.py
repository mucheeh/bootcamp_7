def string_length(something):
  if type(something) == str:
    return [len(something)]
  else:
    lengths = []
    for i in something:
      lengths.append(len(i))
    return lengths

print string_length("hellen")