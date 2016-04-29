def reverse(string): 
  if string != '':
    begin = 0 
    end = len(string) - 1 
    strlist = [i for i in string] 
    while(begin < end): 
        temp = strlist[begin] 
        strlist[begin] = strlist[end] 
        strlist[end] = temp 
        begin += 1 
        end -= 1 
        return ''.join(strlist)
  else:
    

    return None

print reverse('flash')
print reverse('anna')
print reverse('')