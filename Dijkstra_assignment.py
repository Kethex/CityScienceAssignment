import sys

def dijkstra(file, start, target):
    
    graph = {}

    with open(file, "r") as f:
        lines = f.readlines()
        for line in lines:
            fields = line.split(' ')
            if fields[0] in graph:
                graph[fields[0]][fields[1]] = int(fields[2].replace('\n', ''))
            else:
                graph[fields[0]] = {}
                graph[fields[0]][fields[1]] = int(fields[2].replace('\n', ''))
            
    dist = {}
    prev = {}
    unseen_nodes = graph
    assign_inf = 1e10
    
    for node in unseen_nodes:
        dist[node] = assign_inf
    dist[start] = 0
    
    while unseen_nodes:     
        min_dist_node = None
        for node in unseen_nodes:
            if (min_dist_node is None):
                min_dist_node = node
            elif dist[node] < dist[min_dist_node]:
                min_dist_node = node
            
        neighbours = graph[min_dist_node].items()
        unseen_nodes.pop(min_dist_node)
        
        for neighbour, weight in neighbours:
            if min_dist_node == target:
                pass
            elif weight + dist[min_dist_node] < dist[neighbour]:
                dist[neighbour] = weight + dist[min_dist_node]
                prev[neighbour] = min_dist_node
                
                
        
    node = target
    path = []
    
    while node != start:
        try:
            path.insert(0, node)
            node = prev[node]
        except:
            print('Path is not reachable')
            break
    path.insert(0, start)
    
    
    if dist[target] != assign_inf:
        print("Path is " + str(path))
                

if __name__ == "__main__":
    file = str(sys.argv[1])
    start = str(sys.argv[2])
    target = str(sys.argv[3])
    dijkstra(file, start, target)