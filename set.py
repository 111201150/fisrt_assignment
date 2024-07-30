set1={1,2,3,3,5,5,6,7}
set2={5,6,7}
print(set1)
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))
print(set2.issubset(set1))
print(set2.issuperset(set1))

#list to set conversion
list1=[1,2,3,4,4,4,5,7]
list1_temp=set(list1)
list1=list(list1_temp)
print(list1)