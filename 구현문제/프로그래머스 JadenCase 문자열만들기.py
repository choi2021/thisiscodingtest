def Capitalize(s):
    s=s.lower()
    if s!=" ":
       s=s.capitalize()

    return s

def solution(s):
    arr=s.split(" ")
    arr=list(map(Capitalize,arr))
    return " ".join(arr)

s="3people  unFollowed me"
print(solution(s))