list_1 = [int(x) for x in input("Enter numbers in list1:").split()]
list_2 = [int(y) for y in input("Enter numbers in list2:").split()]
merge_list = list(set(list_1 + list_2))
merge_list.sort()
print(merge_list)

