def solution(n, cores):
    if n < len(cores):
        return cores[n-1]
    
    left = 0
    right = max(cores) * n
    while left <= right:
        mid = (left + right) // 2
        done = 0
        for c in cores:
            done += mid // c + 1
            
        if done >= n:
            right = mid - 1
        elif done < n:
            left = mid + 1
            
    t = left
    temp = 0
    for c in cores:
        temp += (t-1) // c + 1
    
    remain = n - temp
        
    for i,c in enumerate(cores):
        if t % c == 0:
            remain -= 1
        if remain == 0:
            return i + 1
            
    return answer