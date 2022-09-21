# 내풀이: 너무 정렬만 생각해서 오히려 더 돌아갔어
# 1. stages를 정렬해야하나 생각했지만 그게 아니라 같은 stage에 있는 사람을 정리해줘야했어
# 2. stages의 순서대로 정리된 사람수를 계산해서 실패율을 계산해서 정리
# 3. 정리된 실패율을 실패율의 내림차순, stage는 오름차순으로 sort
# 4. 마지막으로 stage들만 호출해주기 

def solution(N, stages):
    stage_counts=[0]*(N+2)
    for stage in stages:
        stage_counts[stage]+=1
        
    fail_rates=[]
    for i in range(1,N+1):
        total=sum(stage_counts[i:])
        if total==0:
          fail_rates.append((0,i))
          continue
        fail_rates.append((stage_counts[i]/total,i))
    fail_rates.sort(key=lambda x:(-x[0],x[1]))
    
    result=[]
    for rate in fail_rates:
        result.append(rate[1])
    return result
  

print(solution(5,[1,1,1,1,1]))

#책풀이: 훨씬 간결해

def solution(N,stages):
  answer=[]
  length=len(stages)

  for i in range(1,N+1):
    count=stages.count(i) #일일히 세서 정리하는 로직을 쓰지 않고 세고 length에서 빼줘
    if length==0:
      fail=0
    else:
      fail=count/length
    
    answer.append((i,fail))
    length-=count
  
  answer=sorted(answer,key=lambda t:t[1],reverse=True)
  answer=[i[0] for i in answer] #배열에 정리할때 for loop을 이용하지 않고 값만 이용해서 넣어
  return answer