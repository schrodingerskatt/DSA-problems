
# program to print all substrings of a string

def print_all_substrings(input_string):
    length = len(input_string)

    # Iterate through the string
    for i in range(length):
        for j in range(i + 1, length + 1):
            # Extract and print the substring
            substring = input_string[i:j]
            print(substring)

# Example usage:
input_string = "abc"
print("All substrings of", input_string, "are:")
print_all_substrings(input_string)

