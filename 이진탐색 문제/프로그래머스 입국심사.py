n=6
times=[7,10]




def solution(n, times):
  times.sort()
  start=0
  end=times[-1]*n
  result=end

  while start<=end:
    mid=(start+end)//2
    num=0
    for i in times:
      num+=mid//i
    if num>=n:
      result=mid
      end=mid-1
    else:
      start=mid+1
  return result