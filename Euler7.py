# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

# We simply create a function to check if a number is prime
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

primes = 0 # Number of primes found so far
prime_num = 0  # Initialize the number we check each iteration, skipping 2 & 3
while primes < 10001:
    prime_num = prime_num + 1

    if prime_q(prime_num) == True:
        primes = primes + 1

print(prime_num)

