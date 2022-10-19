from collections import deque

def solution(n, words):
    q=deque()
    visited=[]
    last_word=""
    for i in range(len(words)):
        q.append((words[i],i))
    while q:
        word,ord,=q.popleft()
        if word in visited:
            return [ord % n + 1, ord // n + 1]
        if last_word!="":
            if last_word[-1]!=word[0]:
                return [ord%n+1, ord // n+1]
        visited.append(word)
        last_word=word
    return [0,0]


n=3
words=["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
print(solution(n,words))