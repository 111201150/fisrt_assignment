my_dict = {
    "name": "Jhon",
    "age": 25,
    "gender": "Male"
}

print(my_dict['age'])


#get method
print(my_dict.get('age'))
#keys
print(my_dict.items())
#Add operation
my_dict["new_key"]="new_value"
#update
my_dict["age"]= 48
#Extend
second_dictionary={
    "new_new_key":"new_new_value"
}
my_dict.update(second_dictionary)

#new_dictionary = my_dict + second_dictionary