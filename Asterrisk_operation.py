result = 2**4
print('result is ', result)
result is  16



# print list in multiple time
My_list = [2] *4
print('My_list is ', My_list)

# we can do with tuple also or do with string also
My_list = (3,3,4,5,6,7,8,9,)*4
print('My_list is ', My_list)



# *args and *kwargs
# args use tuple and kwargs use dictionary

def fun(a,b, *args, **kwargs):
    print('a and b', a, b)

    for item in args:
        print('item in args ', item)
    for key in kwargs:
        print('key in kwargs ', key, kwargs[key])

fun(1,2,3,4,5, name = "Ali", age = 25)
  

# iss line ma * ka matlub hai ka jo ke work * ka baad aie ga wo keyword argument hogas
def fun(a,b,*,c):
    print('a, b and c', a, b, c)
fun(1,2,c=3)


# unpack the list or tuple
def fun(a,b,c):
    print(a,b,c)

my_list = (0,20,30)
fun(*my_list)


# if we use the star in variable then it will take the rest of the value in the list
number = [1,2,3,4,5,6,7,8,9,10]
*begner ,last = number
print('begner is ', begner)
print('last is ', last)

# we can combine the list,tuple and string or set by using *

my_list = [1,2,3,4,5,6,7,8,9,10]
my_tuple = (11,12,13,14,15)
my_string = "Hello"
combined = [*my_list, *my_tuple, *my_string]
print('combined is ', combined)