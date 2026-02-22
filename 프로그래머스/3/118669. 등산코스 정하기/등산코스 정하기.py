import heapq

def solution(n, paths, gates, summits):
    def dijkstra():
        answer = [float('inf'),float('inf')]
        while queue:
            intensity,node = heapq.heappop(queue)
            if intensityList[node] < intensity:
                continue
            for newNode,newIntensity in graph[node]:
                if newNode in gatesSet:
                    continue
                maxIntensity = max(intensity,newIntensity)
                if intensityList[newNode] > maxIntensity:
                    intensityList[newNode] = maxIntensity
                    if newNode in summitsSet:
                        if answer[1] > maxIntensity or (answer[1] == maxIntensity and answer[0] > newNode):
                            answer = [newNode,maxIntensity]
                        continue
                    heapq.heappush(queue,[maxIntensity,newNode])
        return answer
    
    graph = [[] for _ in range(n+1)]
    for a,b,c in paths:
        graph[a].append((b,c))
        graph[b].append((a,c))
    
    summitsSet = set(summits)
    gatesSet = set(gates)
    queue = []
    intensityList = [float('inf')] * (n+1) # 이게 intensity 기준
    for gate in gates:
        heapq.heappush(queue,[0,gate])
        intensityList[gate] = 0
    
    answer = dijkstra()
        
    return answer