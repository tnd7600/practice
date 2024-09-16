set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}
if set1.isdisjoint(set2):
    print("Two sets don't have items in common")
else:
    print(f"Two sets have items in common\n{set1.intersection(set2)}")
    

