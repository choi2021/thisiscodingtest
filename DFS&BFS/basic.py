# Stack은 LIFO (Last-In-First-Out) 구조를 가져 마지막으로 들어온 게 먼저 나가는 구조를 가지고 있다

# stack=[]

# stack.append(5)
# stack.append(2)
# stack.append(3)
# stack.append(7)
# stack.pop()
# stack.append(1)
# stack.append(4)
# stack.pop()

# print(stack[::-1])

#queue는 FIFO(First-In-First-Out) 구조를 가져 처음 들어온 게 먼저 나가는 구조를 가지고 있다

# from collections import deque # deque를 사용하면 O(1)으로 popleft가능

# queue=deque()

# queue.append(5)
# queue.append(2)
# queue.append(3)
# queue.append(7)
# queue.popleft()
# queue.append(1)
# queue.popleft()
# queue.append(1)
# queue.append(4)
# queue.popleft()


# print(queue)
# queue.reverse()
# print(queue)

# 재귀 함수는 자기 자신을 다시 호출하는 함수로 멈추기 위한 조건이 필요하다.
# 재귀함수는 스택 자료구조를 이용해 가장 마지막 호출한 함수가 먼저 수행하고 앞의 함수가 종료 된다 (브라우저의 call stack과 같이)

# 예시 1번 100번까지 호출하기
def recursive_function(i):
  if i==100:
    return
  print(i, "번째 재귀 함수에서", i+1,"번째 재귀 함수를 호출합니다.")
  recursive_function(i+1)

recursive_function(1)

#예시 2번 factorial
def factorial_iterative(n):
  result=1
  for i in range(1,n+1):
    result*=i
  return result

def factorial_recursive(n):
  if n<=1:
    return 1
  return factorial_iterative(n-1)*n

print(factorial_iterative(5))
print(factorial_recursive(5))