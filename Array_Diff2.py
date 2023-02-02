# Returns set of input elements
def getInputArray(noOfElements):
    input_array = []

    for each in range(0, noOfElements):
        element = int(input())
        input_array.append(element)

    return set(input_array)

# get inputs
num_current = int(input("Enter number of elements in the 'current' array:"))
current = getInputArray(num_current)

num_target = int(input("Enter number of elements in the 'target' array:"))
target = getInputArray(num_target)

# Print
print(f"current:{current}")
print(f"target:{target}")


additions_set = target - current
deletions_set = current- target

additions = sorted(additions_set)
deletions = sorted(deletions_set)

print(f"additions:{additions}")
print(f"deletions:{deletions}")