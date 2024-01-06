n = 5
parent = []

def initialize():
    global parent
    parent = [i for i in range(n)]

def find(x):
    if parent[x] == x:
        return x
    else:
        return find(parent[x])

def union(x, y):
    x_rep = find(x)
    y_rep = find(y)

    if x_rep == y_rep:
        return

    parent[y_rep] = x_rep

def main():
    
    initialize()
    union(0, 2)
    union(0, 4)
    print(find(4))
    print(find(3))

if __name__ == "__main__":
    main()
