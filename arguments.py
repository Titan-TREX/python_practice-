def fun():
    x = number
    number = 10

    print('number is ',x)

fun()
number = 5


def num():
   global number
   number = 20

number = 15
num()
print('number is ', number)

#add number n list
def list_fun(my_list):
    my_list.append(4)

number = [1, 2, 3]
list_fun(number)
print('list is ', number)



#add number in third index
def fun(list_fun):

    list_fun.append(4)
    list_fun[2]=100

number = [1, 2, 3]
fun(number)
print('list is ', number)

# output is 15
number = 10
number += 5
print('number is ', number, number)


#add list by using += operator
def fun(my_list):
    my_list += [100, 200, 300]

number = [1, 2, 3]
fun(number)
print('list is ', number)