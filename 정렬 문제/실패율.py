
def solution(N, stages):
    result=[]
    length=len(stages)
    for i in range(1,N+1):
      count=stages.count(i)
      if length==0:
        fail=0
      else:
        fail=count/length
      result.append((fail,i))
      length-=count

    result.sort(key=lambda x:(-x[0],x[1]))
    return  [i[1] for i in result]

print(solution(4,[4,4,4,4,4]))