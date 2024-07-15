# Input dictionary
dict_num = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# Printing the header
print("key  value")

# Iterating through the dictionary and printing key-value pairs
for key, value in dict_num.items():
    print(f"{key:<3}  {value:<4}")

"""
Output:
key  value
1    10  
2    20  
3    30  
4    40  
5    50  
6    60  
"""
