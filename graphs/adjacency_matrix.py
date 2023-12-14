vertArr = [[0] * 20 for _ in range(20)] 

def display_matrix(v):
    for i in range(v):
        for j in range(v):
            print(vertArr[i][j], end=" ")
        print()

def add_edge(u, v):
    vertArr[u][v] = 1
    vertArr[v][u] = 1

def main():
    v = 6  # there are 6 vertices in the graph

    add_edge(0, 4)
    add_edge(0, 3)
    add_edge(1, 2)
    add_edge(1, 4)
    add_edge(1, 5)
    add_edge(2, 3)
    add_edge(2, 5)
    add_edge(5, 3)
    add_edge(5, 4)

    display_matrix(v)

if __name__ == "__main__":
    main()