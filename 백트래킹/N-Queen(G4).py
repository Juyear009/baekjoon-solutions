## pypy3로 해결 가능
# def solution(S,N):
#     global result
#     if S == N:
#       result += 1  
#       return
#     for i in range(N):
#         check = False
#         for x,y in queens:
#             if y == i or abs(x-S) == abs(y-i):
#                 check = True
#                 break
#         if not check:
#             queens.append((S,i))
#             solution(S+1,N)
#             queens.pop()
#     return result


# N = int(input())
# queens = []
# result = 0
# print(solution(0,N))


## 시간 복잡도 단축 버전 - GPT
def solution(row, N):
    global result
    if row == N:
        result += 1
        return
    
    for col in range(N):
        if not used_col[col] and not used_diag1[row - col + N - 1] and not used_diag2[row + col]:
            used_col[col] = used_diag1[row - col + N - 1] = used_diag2[row + col] = True
            
            solution(row + 1, N)
            
            used_col[col] = used_diag1[row - col + N - 1] = used_diag2[row + col] = False


N = int(input())
result = 0

used_col = [False] * N
used_diag1 = [False] * (2 * N - 1) 
used_diag2 = [False] * (2 * N - 1)

solution(0, N)
print(result)
