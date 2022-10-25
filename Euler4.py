#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

def reverse(x): #Snippet stolen from Google to reverse a string
  return x[::-1]

#I just multiplied all the numbers 100-999, storing the reverse of the product in a string comparing it against the product,
#if they are equal and that product is larger than any previously found palindromical products then we store it as the new
#highest, once we've brute-checked we print the result
highest = 0
for i in range(100,999):
    for j in range(100,999):
        prod = i * j
        rev = reverse(str(prod))
        if str(prod) == rev and prod > highest:
            highest = prod

print(highest)
