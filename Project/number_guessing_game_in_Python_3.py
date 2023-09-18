import random
import math

# Taking Inputs
lower = int(input("Enter Lower Bound:- "))

# Taking Inputs
upper = int(input("Enter Upper Bound:- "))

# generating random number between
# the lower and upper
x = random.randint(lower, upper)
print("\n\tYou'have only", round(math.log(upper-lower + 1, 2)),
      " chances to guess the integar!\n")

# Initializing the number of guesses
count = 0

# for calculation of minimum number of
# gueses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
