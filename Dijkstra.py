import sys

def dijkstra(file, start, target):
    """
    Parameters
    ----------
    file : str
        Name of the file containing the graph.
    start : str
        Starting destination (node).
    target : str
        Targer destination (node.

    Returns
    -------
    None.

    """
    
    graph = {}
    
    # Converting .dat data to a dictionary
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
    assign_inf = float('inf')
    
    # Assigns infinity to all but the starting node.
    for node in unseen_nodes:
        dist[node] = assign_inf
    dist[start] = 0
    
    # Finds node with the smallest distance
    while unseen_nodes:     
        min_dist_node = None
        for node in unseen_nodes:
            if (min_dist_node is None):
                min_dist_node = node
            elif dist[node] < dist[min_dist_node]:
                min_dist_node = node
        
        # Removes visited node from unseen node set
        neighbours = graph[min_dist_node].items()
        unseen_nodes.pop(min_dist_node)
        
        # Check neighbours of node 
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
            print('No path is possible.')
            break
    path.insert(0, start)
    
    
    if dist[target] != assign_inf:
        print("Path is " + str(path))
                
    return path

def main():
    try:
        file = str(sys.argv[1])
    except IndexError:
        print('Failed to provide a node file.')
    try:
        start = str(sys.argv[2])
    except IndexError:
        print('Failed to provide a starting node.')
    try:
        target = str(sys.argv[3])
    except IndexError:
        print('Failed to provide a target node.')
    dijkstra(file, start, target)
        
    
if __name__ == "__main__":
    main()