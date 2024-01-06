n = 5

def initialize():
    parent = [i for i in range(n)]
    ranks = [0] * n
    return parent, ranks

def find(x, parent):
    if parent[x] == x:
        return x
    else:
        return find(parent[x], parent)

def union(x, y, parent, ranks):
    x_rep = find(x, parent)
    y_rep = find(y, parent)

    if x_rep == y_rep:
        return

    if ranks[x_rep] < ranks[y_rep]:
        parent[x_rep] = y_rep
    elif ranks[y_rep] < ranks[x_rep]:
        parent[y_rep] = x_rep
    else:
        parent[y_rep] = x_rep
        ranks[x_rep] += 1

def main():
    parent, ranks = initialize()

    union(3, 4, parent, ranks)
    union(2, 3, parent, ranks)
    union(1, 2, parent, ranks)
    union(0, 1, parent, ranks)

    print(parent[3])
    print(ranks[3])

if __name__ == "__main__":
    main()
