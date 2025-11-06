class Solution:
    def processQueries(self, c: int, connections: List[List[int]], queries: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in connections:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: Find connected components
        visited = [False] * (c + 1)
        component = [0] * (c + 1)
        comp_id = 0
        
        for i in range(1, c + 1):
            if not visited[i]:
                comp_id += 1
                queue = deque([i])
                visited[i] = True
                while queue:
                    node = queue.popleft()
                    component[node] = comp_id
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            queue.append(nei)
        
        # Step 3: Maintain online stations for each component using SortedList
        online = defaultdict(SortedList)
        for i in range(1, c + 1):
            online[component[i]].add(i)
        
        # Step 4: Process queries
        res = []
        status = [True] * (c + 1)
        
        for q in queries:
            if q[0] == 1:
                x = q[1]
                if status[x]:
                    res.append(x)
                else:
                    comp = component[x]
                    if online[comp]:
                        res.append(online[comp][0])  # min element
                    else:
                        res.append(-1)
            else:  # q[0] == 2
                x = q[1]
                if status[x]:
                    status[x] = False
                    comp = component[x]
                    online[comp].remove(x)
        
        return res