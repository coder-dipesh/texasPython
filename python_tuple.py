
def modify_tuple(tupl, elem):
  print(type(tupl))
  newData = list(tupl)
  newData.append(elem)
  tupl = tuple(newData)
  print(tupl)

modify_tuple((1,2,3), 4)