# Check if the first and last number of a list is the same

def true_false(a,b,list):
    if a == b:
        print(f"Given list:{list}\nResult Is True")
    else: 
        print(f"Given list:{list}\nResult Is False")
   

list_1 = [10, 20, 30, 40, 10]
list_2 = [75, 65, 35, 75, 30]
true_false(list_1[0],list_1[-1],list_1)
true_false(list_2[0],list_2[-1],list_2)

        


# if list_1[0] ==list_1[-1]:
#     print(f"Given list:{list_1}\nResult Is True")
# else:
    # print(f"Given list:{list_1}\nResult Is False")


# if list_2[0] ==list_2[-1]:
#     print(f"Given list:{list_2}\nResult Is True")
# else:
    # print(f"Given list:{list_2}\nResult Is False")_2