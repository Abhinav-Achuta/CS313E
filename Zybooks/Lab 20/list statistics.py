# Step 0: Input values
nums = [int(n) for n in input().split()]

# Step 1: Find minimumimum and maximumimum values
# Type your code here.
min = nums[0]
max = nums[0]

for i in range(len(nums)):
    if nums[i] < min:
        min = nums[i]
    if nums[i] > max:
        max = nums[i]

print(f"Minimum: {min}")
print(f"Maximum: {max}")

# Step 2: Calculate mean
# Type your code here.
mean = sum(nums)/len(nums)
print(f"Mean: {mean:.1f}")

# Step 3: Check if palindrome
# Type your code here.

def is_palindrome(list):

    for i in range(len(list)//2):
        if list[i] != list[-i-1]:
            return False
    return True

print("Palindrome: " + str(is_palindrome(nums)))


# Sort list
nums.sort()

# Step 4: Find and output median
# Type your code here.
if len(nums)%2 == 0:
    length = len(nums)//2
    right_middle = nums[length]
    left_middle = nums[length-1]
    median = (right_middle+left_middle)/2
else:
    median = nums[len(nums)//2]

print(f"Median: {median:.1f}")

# Step 5: Find and output mode
# Type your code here.

def find_mode(list):
    counter = 0
    counter_max = 0
    current_mode = None

    for i in range(len(list)-1): #i-1 because do not need to check last number (if last number is alone it is not mode anyways)
        if list[i] == list[i+1]: #If next in list is the same number, adds to counter
            counter += 1
        if counter > counter_max: #If the counter of current number being counted, updates max counter and declares this the mode
            counter_max = counter
            current_mode = list[i]
        if list[i] != list[i+1]: #If next in list is a new number, resets the counter
            counter = 0
    
    return current_mode

mode = find_mode(nums)

print(f"Mode: {mode}")
