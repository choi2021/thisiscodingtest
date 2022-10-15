from collections import deque
def solution(queue1, queue2):
    count=0
    q1,q2=deque(queue1),deque(queue2)
    sum1,sum2=sum(q1),sum(q2)
    if (sum1+sum2)%2!=0:
      return -1

    while len(q1)!=0 and len(q2)!=0:
        if count>=300000:
          break
        if sum1==sum2:
            return count
        elif sum1 >sum2:
            poped=q1.popleft()
            q2.append(poped)
            sum1-=poped
            sum2+=poped
        else:
            poped=q2.popleft()
            q1.append(poped)
            sum2-=poped
            sum1+=poped
        count+=1
    return -1


queue1= [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 10 ]
queue2=[ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ]

print(solution(queue1,queue2))