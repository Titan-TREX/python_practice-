import random
a = random.randint(1, 100)
print(a)


b = random.random()
print(b)

c= random.uniform(1.5, 5.5)
print(c)

my_list = [10, 20, 30, 40, 50]

d = random.choice(my_list)
print(d)

#shuffle list
e = random.shuffle(my_list)
print(my_list)




random.seed(10)
print(random.random())
print(random.randint(1, 100))

random.seed(10)
print(random.random())
print(random.randint(1, 100))

random.seed(1)
print(random.random())
print(random.randint(1, 100))
