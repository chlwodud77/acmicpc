#10829.py - 이진수 변환

def con_dec2bin(N, result):
  if N == 1:
#         print(1)
    result.append(1)
    return result
  else:
    # print(N%2)
    result.append(N%2)
#         print(result)
    con_dec2bin(int(N/2), result)

def main(N):
  result = []
  final = ''
  con_dec2bin(N, result)
  for i in range(len(result)):
    # print(result[len(result) - i - 1])
    final += str(result[len(result) - i - 1])

  print(final)


N = int(input())
main(N)