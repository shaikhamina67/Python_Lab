# Sample dictionaries
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

# Creating a new dictionary by concatenating dic1, dic2, and dic3
result = {**dic1, **dic2, **dic3}

# Printing the result
print("Concatenated Dictionary:", result)


"""
Output:
Concatenated Dictionary: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}"""
