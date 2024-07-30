my_dict = {
    "name": "Jhon",
    "age": 25,
    "gender": "Male"
}

print(my_dict['age'])
print(my_dict.get('age'))
print(my_dict.items())
my_dict["new_key"]="new_value"
my_dict["age"]= 48
second_dictionary={
    "new_new_key":"new_new_value"
}
my_dict.update(second_dictionary)

#new_dictionary = my_dict + second_dictionary