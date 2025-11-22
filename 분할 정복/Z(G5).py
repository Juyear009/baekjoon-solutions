def solution(n,x,y):
    global answer
    if n == 1:
        if x == c and y == r:
            print(answer)
        answer += 1
        return
    elif x <= c <= x+n-1 and y <= r <= y+n-1:
        a1 = solution(n//2,x,y)
        a2 = solution(n//2,x+n//2,y)
        a3 = solution(n//2,x,y+n//2)
        a4 = solution(n//2,x+n//2,y+n//2)
    else:
        answer += n**2
        return


N,r,c = map(int,input().split())

answer = 0
solution(2**N,0,0)