sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}
keys = ["name", "salary"]
new_dict = {i : sample_dict[i] for i in keys }
print(new_dict)