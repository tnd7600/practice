sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}

# method 1
sample_dict['emp3']['salary'] = 8500
print(sample_dict)

# method 2
for i in sample_dict.values():
    if i['name']=='Brad':
        i['salary'] = 8500

print(sample_dict)        
