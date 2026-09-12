n = (1, 2, 3, 4, 5, 6)
even_nums = tuple(x for x in n if x % 2 == 0)
# odd_nums = tuple(int(x) for y in n if x % 2 != 0)  #smallest error can lead to system failure in huge programs
odd_nums = tuple(x for x in n if x % 2 != 0)
print(f"even numbers tuple : {even_nums}")
print(f"odd numbers tuple : {odd_nums}")