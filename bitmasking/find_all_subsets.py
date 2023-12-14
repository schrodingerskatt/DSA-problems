from itertools import combinations

def find_power_set(nums):
    bits = len(nums)
    pow_set_size = 2 ** bits

    nums.sort()
    ans = []
    subset_set = set()

    for counter in range(pow_set_size):
        subset = [nums[j] for j in range(bits) if (counter & (1 << j)) > 0]
        temp = ''.join(map(str, subset))

        if temp not in subset_set:
            ans.append(subset)
            subset_set.add(temp)

    return ans

# Driver code
if __name__ == "__main__":
    arr = [10, 12, 12]
    power_set = find_power_set(arr)

    for i in range(len(power_set)):
        for j in range(len(power_set[i])):
            print(power_set[i][j], end=" ")
        print()
   