def solution(brown, yellow):
    total=brown+yellow
    targets=[]
    for i in range(total-1,2,-1):
      if total%i==0:
        a,b=i,total//i
        if a>=b and not (a,b) in targets:
          targets.append((a,b))
    answer=[]
    for target in targets:
      row,col=target
      if row*2+col*2-4==brown:
        answer=[row,col]
        break    
    return answer

brown=10
yellow=2

solution(brown,yellow)