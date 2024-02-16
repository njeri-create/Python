my_set = {1,2,3,4,5}
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7,8,9,10])
print(my_set)
my_set2 = my_set.copy()
print(my_set2)
print(len(my_set))
my_set.discard(7)
print(my_set)
my_set.clear()
print(my_set)
del my_set
print(my_set2)
print(max(my_set2))
print(min(my_set2))
print(sum(my_set2))
print(sum(my_set2)/len(my_set2))

names = ['John', 'Smith', 'Mark', "James"]
if "James" in names:
    print("Student is present in the school system")
else:
    print("Student is not present in the school system")

parents = ['Moses', 'Eve', "Annah", "Brinnel" ]
one_value = "Annah"
if one_value in parents:
    output = one_value
    print(output)

numbers = [1,2,3,4,5]
if "7" in numbers:
    print("7 is present")
else:
    print("7 is not present")
