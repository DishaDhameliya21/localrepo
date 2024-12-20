# Lambda function with a default argument
multiply = lambda x, y=2: x * y

print(multiply(4))  # Output: 8 (4 * 2)
print(multiply(4, 3))  # Output: 12 (4 * 3)


# Sorting a list of tuples by the second element
pairs = [(1, 2), (3, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])

print(sorted_pairs)  # Output: [(5, 0), (3, 1), (1, 2)]
