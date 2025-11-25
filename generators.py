def mygenrators():
    yield 10
    yield 8
    yield 3
    yield 6
    yield 2

g = mygenrators()

# value = next(g)
# print(value)

# value = next(g)
# print(value)



print(sorted(g))


def countdown(n):
    print("Starting to count down")
    while n > 0:
        yield n
        n -= 1
cd = countdown(5)
value = next(cd)
print(value)
print(next(cd))


import sys 
def first(n):
    nums = []
    num = 0

    while num < n:
        nums.append(num)
        num += 1
    return nums

def second(n):
    num = 0
    while num < n:
        yield num
        num += 1

print(sys.getsizeof(first(1000000)))
print(sys.getsizeof(second(1000000)))





import sys

mygenrators = (i for i in range(1000000) if i % 2 ==0)
print(sys.getsizeof(mygenrators))

mylist = [i for i in range(1000000) if i % 2 ==0]
print(sys.getsizeof(mylist))