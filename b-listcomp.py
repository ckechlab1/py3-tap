n = [1,2,3,4,5]
squares = []

# for num in n:
#     squares.append(num**2)

# List comprehension
squares = [x**2 for x in n]

# Dictionary Comprehension
n_pow_2 = {f"{x}^2": x**2 for x in n}

print(n)
print(squares)
print(n_pow_2)