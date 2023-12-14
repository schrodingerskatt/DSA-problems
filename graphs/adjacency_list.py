from collections import defaultdict

def display_adj_list(adj_list, v):
    for i in range(v):
        print(f"{i} ---> ", end="")
        for neighbor in adj_list[i]:
            print(f"{neighbor} ", end="")
        print()

def add_edge(adj_list, u, v):
    adj_list[u].append(v)
    adj_list[v].append(u)

def main():
    v = 6
    adj_list = defaultdict(list)
    add_edge(adj_list, 0, 4)
    add_edge(adj_list, 0, 3)
    add_edge(adj_list, 1, 2)
    add_edge(adj_list, 1, 4)
    add_edge(adj_list, 1, 5)
    add_edge(adj_list, 2, 3)
    add_edge(adj_list, 2, 5)
    add_edge(adj_list, 5, 3)
    add_edge(adj_list, 5, 4)

    display_adj_list(adj_list, v)

if __name__ == "__main__":
    main()
