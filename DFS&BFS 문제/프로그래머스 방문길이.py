dirs=	"LULLLLLLU"

Delta={"U":(0,1),"D":(0,-1),"R":(1,0),"L":(-1,0)}

def solution(dirs):
    visited=[]
    x,y=0,0
    for ord in dirs:
        dx,dy=Delta[ord]
        nx,ny=x+dx,y+dy
        if -5<=nx<=5 and -5<=ny<=5:
            visited.append((x,y,nx,ny))
            visited.append((nx,ny,x,y))
            x,y=nx,ny
    return len(set(visited))//2
print(solution(dirs))