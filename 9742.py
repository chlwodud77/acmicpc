#9742.py - 순열

x = 0
# per_list = []
def permutation(s, result, goal, first):
  #print(s)
  global x
  if len(s) == 1:
    #print(s[0])
    result += s
    x += 1
    # print(result)
    # per_list.append(result)
    if x == goal:
      print(first+' = '+''.join(result))
      return True
    return 
  for a in s:
    #print(a)
    new_s = s.copy()
    new_s.remove(a)

    permutation(new_s, result+[a], goal, first)

while True:
  try:
    first = input()
    test = first.split()
    per = list(test[0])
    pos = int(test[1])

    permutation(per, [], pos, first)
    # print('x: ', x)
    if x < pos:
      print(first+' = '+'No permutation')
    x = 0
    # print(len(per_list))
    # if len(per_list) > pos:
    #   print(first+' = '+''.join(per_list[pos-1]))
    # else:
    

    # per_list = []

  except EOFError:
    break
