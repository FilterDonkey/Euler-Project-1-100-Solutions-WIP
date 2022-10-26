#A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
#a2 + b2 = c2

#For example, 32 + 42 = 9 + 16 = 25 = 52.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

import math

product, sum = 1, 1
abc = [0,0,0]

for a in range(1,999):
    for b in range(1,999):
        c2 = pow(a,2) + pow(b,2)
        c = math.sqrt(c2)
        if c % 1 ==0:
            sum = a + b + c
            if sum == 1000:
                product = int(a * b * c)
                abc[0] = a
                abc[1] = b
                abc[2] = int(c)

print("a: " + str(abc[0]))
print("b: " + str(abc[1]))
print("c: " + str(abc[2]))
print("abc: " + str(product))
