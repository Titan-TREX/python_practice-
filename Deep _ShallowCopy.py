import copy
#simple assignment (shallow copy)

number = [1,2,3,4,5,6,7,8,9,10]
add_number = number
add_number[0] = 100
print('number is ', number)
print('add_number is ', add_number)



#use copy module for SHALLOW COPY
number = [1,2,3,4,5,6,7,8,9,10]
add_number =copy.copy(number)
add_number[0] = 100
print('number is ', number)
print('add_number is ', add_number)

#using copy module for DEEP COPY
number = [1,2,3,4,5,6,[7,8,9,10]]
add_number =copy.deepcopy(number)
add_number[0]=100
print('number is ', number)
print('add_number is ', add_number)


class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("Ali", 25)
p2 = copy.deepcopy(p1)
p2.age = 18
print('p1 age is ', p1.age)
print('p2 age is ', p2.age)
    



# =




