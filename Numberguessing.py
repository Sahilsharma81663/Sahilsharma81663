import random
import math

# taking input
lower = int(input("Enter lower bound:-"))
# taking inputs
upper = int(input("Enter upper bound:-"))

# generating the random between upper and lower

x = random.randint(lower, upper)
print("\n\tYou've only", round(math.log(upper - lower + 1, 2)), "chances to guess the integer!\n")
# initializing the number of guesses

count = 0

# for calculation of minimum number of guesses depends upon range
while count < math.log(upper - lower + 1, 2):
    count += 1
    # taking guessing number as input
    guess = int(input("Guess a number:-"))
    # condition testing

    if x == guess:
        print("Congratulations you did it in ", count, "try")

        # once guessed loop will break
        break
    elif x > guess:
        print("You guess too small!")
    elif x < guess:
        print("Your guess is too high!")

        # if guessing is more than required guess

        if count >= math.log(upper - lower + 1, 2):
            print("\nThe number is %d" % x)
            print("\tBetter luck next time!")
