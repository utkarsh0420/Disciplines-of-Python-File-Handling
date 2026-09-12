nums = [5, 10, 15, 20, 25]

# new_list = [val if val > 15 else None for val in nums]
new_list = [val for val in nums if val>15]  
print(new_list)
