#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

sum_sq = 0
sq_sum = 0

for x in range(1,101): #I do NOT understand why 101 please help
    sum_sq = sum_sq + pow(x,2)
    sq_sum = sq_sum + x

sq_sum = pow(sq_sum,2)

diff = abs(sum_sq - sq_sum)
print(diff)



