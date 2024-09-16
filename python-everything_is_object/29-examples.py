a = 5
print(id(a))  # Example output: 140332822268688
print(type(a))  # Output: <class 'int'>


a = [1, 2, 3]
b = a
a.append(4)
print(b)  # Output: [1, 2, 3, 4]


a = 10
b = a
a += 5
print(b)  # Output: 10
print(a)  # Output: 15


def modify_list(lst):
    lst.append(4)

def modify_number(num):
    num += 5

my_list = [1, 2, 3]
my_number = 10

modify_list(my_list)
modify_number(my_number)

print(my_list)  # Output: [1, 2, 3, 4]
print(my_number)  # Output: 10