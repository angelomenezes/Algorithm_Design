if __name__ == '__main__':
    
    while True:

        n_of_nodes = int(input())

        if n_of_nodes == 0:
            break

        n_of_edges = int(input())

        graph = [[0 for _ in range(n_of_nodes)] for _ in range(n_of_nodes)]
        color = [-1] * n_of_nodes

        for _ in range(n_of_edges):
            a, b = map(int, input().split())
            graph[a][b] = 1
            graph[b][a] = 1
    
        node_list = [0]
        color[0] = 0
        flag = True

        while node_list:
            u = node_list.pop(0)
            for v in range(n_of_nodes):
                if graph[u][v]:  
                    if color[v] == -1:
                        color[v] = color[u] + 1
                        node_list.append(v)
                    elif color[u] == color[v]:
                        flag = False
                        break
        if flag:
            print("BICOLORABLE.")
        else:
            print('NOT BICOLORABLE.')

            