#17478.py - 재귀함수가 뭔가요?

msg = ['어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.',
'"재귀함수가 뭔가요?"',
'"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.',
'마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.',
'그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."',
'"재귀함수는 자기 자신을 호출하는 함수라네"',
'라고 답변하였지.']

dash_print = '____'

rago = '라고 답변하였지.'
question = '"재귀함수가 뭔가요?"'
answer = '"재귀함수는 자기 자신을 호출하는 함수라네"'

def reg(N, ndash):
  if N == 1:
    print(dash_print * ndash+question)
    print(dash_print * ndash+answer)
    print(dash_print * ndash+rago)
    return
  else:
    for i in range(1,5):
      print(dash_print * ndash+msg[i])
    reg(N-1, ndash+1)
    print(dash_print * ndash+rago)


N = int(input())

#초입
for i in range(5):
  print(msg[i])


#재귀함수
reg(N, 1)

#끝
print(msg[-1])