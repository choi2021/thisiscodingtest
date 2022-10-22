# 시간초과
people=[10, 20, 30,40]
limit=50
#
# def solution(people, limit):
# 	people.sort()
# 	temp=[]
# 	count=0
# 	for i in range(len(people)):
# 		for j in range(len(people)-1,i,-1):
# 			if people[i]+people[j]<=limit:
# 				if i in temp or j in temp:
# 					continue
# 				count+=1
# 				temp.append(i)
# 				temp.append(j)
# 				break
# 	print(temp)
# 	return count+len(people)-len(temp)
#
#
#


from collections import deque

def solution(people,limit):
	answer=0
	deq=deque(sorted(people))
	while deq:
		if len(deq)==1:
			answer+=1
			break
		if deq[0]+deq[-1]<=limit:
			deq.pop()
			deq.popleft()
			answer+=1
		else:
			deq.pop()
			answer+=1
	return answer

print(solution(people,limit))