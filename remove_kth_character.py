def removekth(input_string, k):
    if k < 1 or k > len(input_string):
        raise ValueError("Invalid value of k")

    # Remove the kth character using string slicing
    result_string = input_string[:k - 1] + input_string[k:]

    return result_string

# Test the function
input_str = "Hello, World!"
kth_position = 5

try:
    modified_str = removekth(input_str, kth_position)
    print("Original String:", input_str)
    print("Modified String:", modified_str)
except ValueError as e:
    print("Error:", e)
