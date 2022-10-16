from heapq import heappush,heappop,heapify

def negative_num(num):
    return -num

def solution(operations):
    q=[]
    for operation in operations:
        a,b=operation.split(" ")
        if a=="I":
            heappush(q,int(b))
        else:
            if b=="-1" and len(q)!=0:
                heapify(q)
                heappop(q)

            elif b=="1" and len(q)!=0:
                max_q=list(map(negative_num,q))
                heapify(max_q)
                heappop(max_q)
                q=list(map(negative_num,max_q))
    if len(q)==0:
        return [0,0]
    else:
        min=q[0]
        max_q=list(map(negative_num,q))
        heapify(max_q)
        max=-max_q[0]
        print(min,max)
        return [max,min]



operations=["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
print(solution(operations))