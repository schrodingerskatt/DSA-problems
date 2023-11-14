def increasing(n):
    if n == 0:
        return
    increasing(n-1)
    print(n)

increasing(10)