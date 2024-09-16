str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
str_list2 = str_list.copy()
print(f"Original list of sting\n{str_list}\n")
for i in str_list:
    if i is None or i == "":
        str_list2.remove(i)
print(f"After removing empty strings\n{str_list2}")
