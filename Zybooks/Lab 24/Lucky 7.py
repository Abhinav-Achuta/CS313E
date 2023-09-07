import random
import gv_die

# Create two GVDie objects
die1 = gv_die.GVDie()
die2 = gv_die.GVDie()

# Read random seed to support testing (do not alter) and starting credits
seed = int(input())
# Set the seed for random
random.seed(int(seed))

# Initial credits
credits = int(input())

# Type your code here.


print(f"Dice total: {die1.roll(seed) + die2.roll(seed)}")
print(f"Credits: {die1.getvalue() + die2.getvalue()}")
