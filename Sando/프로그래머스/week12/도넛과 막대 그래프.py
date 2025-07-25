from collections import defaultdict, deque

def solution(edges) : 
    # 진입차수, 진출차수 개수 담는 dictionary
    indegree= defaultdict(int)
    outdegree = defaultdict(int) 
    
    nodes = set()
    
    for a,b in edges: 
        outdegree[a] += 1
        indegree[b] += 1
        nodes.add(a)
        nodes.add(b)
        
    # 생성점 찾기 : 진입 = 0 , 진출 >= 2
    start = -1
    for node in nodes:
        if indegree[node] == 0 and outdegree[node] >=2:
            start = node
            break
    
    # 그래프 재구성(생성점 기준)
    graph = defaultdict(list) # value를 list형태로 저장하겠다
    for a,b in edges : 
        if a == start:
            continue
        graph[a].append(b)
        
    visited = set()
    
    donut = 0 
    eight = 0
    stick = 0
    
    for a,b in edges:
        if a != start : 
            continue
        current = b
        path = set ()
        prev = current
        while True:
            if current in path:
                donut += 1
                break
            if current in visited :
                eight +=1
                break
            path.add(current)
            visited.add(current)
            
            if outdegree[current] == 0:
                stick += 1
                break
            if outdegree[current] >= 2 and current != start:
                eight +=1
                break
            
            # 다음 노드
            next = graph[current][0] if graph[current] else None
            if not next:
                stick += 1
                break
            prev = current
            current = next
            
    return [start, donut, stick, eight]
    
e = [[2, 3], [4, 3], [1, 1], [2, 1]]
print(solution(e))