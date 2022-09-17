# 내풀이: 
# 1.dist가 큰 순서대로 사용해
# 2.한명부터 dist에 사람들을 다써서 덮는데 길이가 안되면 다음 긴걸로
# 3. 거리 안에 있는 것 체크
# 어려워서 포기....
# from itertools import combinations
# n=int(input())
# weak=[1,5,6,10]
# dist=[1,2,3,4]

# def check_points(weak,start,end,dir):
#   points=[]
#   if dir=="R":
#     for i in range(start+1,end):
#       if i in weak:
#         points.append(i)
#   elif dir=="L":
#     for i in range(end+1,n):
#       if i in weak:
#         points.append(i)
#     for i in range(0,start):
#       if i in weak:
#         points.append(i)
#   return points
  

# def solution(n, weak, dist):
#   combis=list(combinations(weak,2))
#   for combi in combis:
#     start,end=combi
#     direction="R"
#     dist=abs(start-end)
#     if abs(start-end)>abs(n-abs(start-end)):
#       direction="L"
#       dist=abs(n-abs(start-end))
#     checked_points=check_points(weak,start,end,direction)
#     print(dist)
    

    
#책풀이
#1.원형은 길이를 2배로 늘려서 일자형태로 만든다


from itertools import permutations

def solution(n, weak, dist):
    length = len(weak)
    # 원형 맵 일직선 상에 구현하기 위해서 길이 2배로 늘리기
    for i in range(len(weak)):
        weak.append(weak[i] + n)
    # 최소 인원 계산할 최댓값 정의 for 그리디
    answer = len(dist) + 1
    # 2배 늘린 일직선 상 맵에서 시작점 하나씩 탐색(단, 원래 취약지점 길이까지만 탐색)
    for start in range(length):
        # 한 시작점에서 투입할 수 있는 친구 경우의 수 하나씩 탐색(순열)
        for friends in list(permutations(dist, len(dist))):
            # 최초의 친구 1명 투입!
            count = 1
            position = weak[start] + friends[count-1] # 투입한 친구가 처리할 수 있는 위치
            # 그 위치가 취약지점 중 어디까지 처리할 수 있는지 탐색
            for index in range(start, start+length):
                # 처리 가능 위치가 탐색하고 있는 위치보다 작을 때 -> 친구 하나 더 투입!
                if position < weak[index]:
                    count += 1
                    # 친구 다 썼는지 확인
                    if count > len(dist):
                        break
                    # 추가로 투입한 친구가 처리할 수 있는 위치로 업데이트
                    position = weak[index] + friends[count-1]
            # 다 탐색했을 때의 count(인원 수)를 최솟값으로 업데이트
            answer = min(answer, count)
    # 다 처리하기 전 친구를 다 썼으면 -1
    if count > len(dist):
        return -1
    return answer