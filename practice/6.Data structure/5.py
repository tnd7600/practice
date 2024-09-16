# combine two lists elements and convert into a set in tuple form

first_list = [2, 3, 4, 5, 6, 7, 8]
second_list = [4, 9, 16, 25, 36, 49, 64]

combine_set = zip(first_list, second_list)
combine_set = set(combine_set)
print(f"Result is {combine_set}")
