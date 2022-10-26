#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
import math

num = 600851475143
largest_factor = 1

def prime_q(x):
    poss_prime = False
    if x > 4:
        for y in range(2,x-1):
            result = x % y
            if result == 0:
                poss_prime = False
                break
            else:
                poss_prime = True
    if x > 1 and x < 4:
        poss_prime = True
    return poss_prime

x = 3
while x <= num:
    rem = num % x
    if rem == 0:
        num = num / x
        largest_factor = x
    x = x + 2

print(largest_factor)

# This whole thing took 30+ minutes to end, while doing other things I remembered the faster way I did when I solved this last time
#num = 600851475143
#max_fact = int(math.ceil((num/30))) #  Seeing as the last digit isn't divisble by 2, the cross-sum isn't divisible by 3 and the
#  last digit isn't divisible 5 or 0, meaning 'num' is NOT divisible by 2, 3 or 5, meaning we can divide by these factors to reduce the for-loop range

#for x in reversed(range(3,max_fact,2)):
#    rem = num % x
#    if rem == 0 and prime_q(x) == True:
#        print(x)
#        break