list1 = [1,2,3,4,5,6]
list2 = ["hello", "World",]
list3 = [1,2,3, "Helloo"]

#Length of list
print(len(list1))

#Append
list1.append(8)
print(list1)

#Concatnation of list
result_list = list2+list3
print(result_list)

#Extend of list
list2.extend(list3)
print(result_list)
print(list2)

#Join operation
list2 = ["hello", "World"]
resulted = "#".join(list2)
print(resulted)

#Split operation
list2 = ["hello", "World"]
splited_result = resulted.split("#")
print(splited_result)

list1[:]
list1[:5]
list1[5:]
list1[-2]

#practice problem (add and print the value of list [2]& list[-2])
print(list1)
var1 = list1[2]
var2 = list1[-2]
result = var1+var2
print(result)
