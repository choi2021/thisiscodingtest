# 거리를 잴때 두개를 골라서
from itertools import permutations

n=12
weak=[1, 5, 6, 10]
dist=[1, 2, 3, 4]

def solution(n, weak, dist):
    length=len(weak)
    for i in range(length): #원형을 일자로
        weak.append(weak[i]+n)
    answer=len(dist)+1 #초기화
    for start in range(length): #탐색 시작할 시작점을 정해
        for friends in list(permutations(dist,len(dist))): #순서에 따라 값이 달라지니까 순열로 정해
            count=1 #1명으로 시작
            position=weak[start]+friends[count-1] #시작점~첫번째 친구가 탐지하는 위치
            for index in range(start,start+length): #시작점부터 취약점 체크
                if position<weak[index]:
                    count+=1
                    if count>len(dist): #이미 사람을 다썼으면 break
                        break
                    position=weak[index]+friends[count-1] # 사람을 추가해서 위치선정
            answer=min(answer,count)
    if answer>len(dist):
        return -1
    return answer