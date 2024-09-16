# remove duplicate and convert into tuple form find min and max value

sample_list = [87, 52, 44, 53, 54, 87, 52, 53]
sample_tuple = tuple(sample_list)

print(sample_list)
print(sample_tuple)
print(min(sample_tuple))
print(max(sample_tuple))

# sample_tuple = ()
# for i in sample_list:
#     if i not in sample_tuple:
#         sample_tuple += (i,)
# print(sample_tuple)
# print(min(sample_tuple))
# print(max(sample_tuple))