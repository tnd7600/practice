sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}
keys = ["name", "salary"]

for i in keys:
    if i in sample_dict:
        sample_dict.pop(i)

print(sample_dict)