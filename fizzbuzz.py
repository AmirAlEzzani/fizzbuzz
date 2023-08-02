#fizzbuzz: from range 1-100 print fizz if divisible by 3, buzz if divisible by 5, and fizzbuzz if divisible by both

i=1
for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + ' fizzbuzz')
    elif i % 3 == 0:
        print(str(i) +  ' fizz')
    elif i % 5 == 0:
        print(str(i) + ' buzz')
    