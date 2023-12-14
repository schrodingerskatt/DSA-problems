def count_sort(data):
    max_val = max(data)
    count_array = [0]*(max_val+1)

    for num in data:
        count_array[num]+=1
    
    for i in range(1,len(count_array)):
        count_array[i]+=count_array[i-1]
    
    sorted_data = [0]*len(data)
    for element in data:
        sorted_data[count_array[element]-1]=element
        count_array[element]-=1
    return sorted_data

data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
sorted_data = count_sort(data)

print(f"Sorted data: {sorted_data}")
        