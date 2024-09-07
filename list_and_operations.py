my_list = [1, 2, 3, 4, 5]

my_list.append(6)
print(my_list.append)

my_list.insert(2, 0)
print(my_list.insert)
my_list.remove(3)
print(my_list.remove)
list_length = len(my_list)

popped_element = my_list.pop(4)

my_list.clear()

print("Modified list:", my_list)
print("Length of the list:", list_length)
print("Popped element:", popped_element)
