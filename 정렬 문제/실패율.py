def solution(N, stages):
    answer = []
    stage_counts=[0]*(N+2)
    for stage in stages:
        stage_counts[stage]+=1
        
    fail_rates=[]
    for i in range(1,N+1):
        total=sum(stage_counts[i:])
        if total==0:
          fail_rates.append((0,0))
          continue
        fail_rates.append((stage_counts[i]/total,i))
    fail_rates.sort(key=lambda x:(-x[0],x[1]))
    
    result=[]
    for rate in fail_rates:
        result.append(rate[1])
    return result
  

print(solution(5,[1,1,1,1,1]))