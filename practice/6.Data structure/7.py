# find whether a given set is subset or superset of another set
# if yes then clear both sets

set1 = {27, 43, 34}
set2 = {34, 93, 22, 27, 43, 53, 48}

print(f"First set is subset of second set : {set1.issubset(set2)}")
print(f"second set is subset of first set : {set2.issubset(set1)}\n")

print(f"First set is subset of second set : {set1.issuperset(set2)}")
print(f"second set is subset of first set : {set2.issuperset(set1)}\n")

if set1.issuperset(set2):
    set2.clear()
if set2.issuperset(set1):
    set1.clear()

print(f"First Set : {set1}")
print(f"Second Set : {set2}")