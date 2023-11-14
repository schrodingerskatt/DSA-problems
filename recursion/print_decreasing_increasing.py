# print decreasing, increasing sequence
'''
5
4
3
2
1
1
2
3
4
5
'''
def increase_decrease(n):
    if n == 0:
        return 
    print(n)
    increase_decrease(n-1)
    print(n)

increase_decrease(5)