#Expression for expressions in list
my_list=[1,2,3,4,5,6,7]
update_list = [x**2 for x in my_list]
print(update_list)

#Expression for expressions in list if condition
my_list = [1,2,3,4,5,6,7]
update_list = [x**2 for x in my_list if x%2==0 or x>3 if x**2>25]
print(update_list)