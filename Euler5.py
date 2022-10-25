#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

#Not the smallest but A positive number which is evenly divisible by 1..20 is surely the product of 1..20,
#to set an upper bound to prevent endless calculation I calculate that number here
max = 1
for i in range(2,20):
    max = max * i

primes = [2,3,5,7,11,13,17,19] #List of the non-trivial primes in 1..20, using these to check first to reduce runtime
non_primes = [4,6,8,9,10,12,14,15,16,18,20] #List of the non-primes in 1..20, checking these to confirm
maybe_found = False #Used within for-loop to preserve potential number for checking against non_primes
found = False #Ends the loop once it's set to True after finding the first (i.e. the lowest)
i = 20
while i < max and found == False:
    i = i+20
    for x in primes:
        rem = i % x
        if rem == 0:
            maybe_found = True
        else:
            maybe_found = False
            break
    if maybe_found == True:
        for x in non_primes:
            rem = i % x
            if rem != 0:
                break
            if rem == 0 and x == 20:
                found = True

print(i)
