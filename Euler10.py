#  The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

#  Find the sum of all the primes below two million.

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

prime_sum = 2
for x in range(3,2*pow(10,6),2):
    if prime_q(x) == True:
        prime_sum = prime_sum + x

print(prime_sum)