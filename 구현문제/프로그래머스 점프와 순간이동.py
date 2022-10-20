def solution(n):
	answer=0
	while n!=0:
		if n==1:
			answer+=1
			break
		if n%2==1:
			answer+=1
		n//=2
	return answer
n=6
print(solution(n))
