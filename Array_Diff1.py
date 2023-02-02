#without using sets
# Returns set of input elements
def get_input_array(no_of_elements):

    input_array = []

    for each in range(0, no_of_elements):
        element = int(input())
        input_array.append(element)

    return input_array


def get_array_diff(array1, array2):

    array_diff = []

    for i in array1:
        if i not in array2:
            array_diff.append(i)

    return array_diff


# get inputs
num_current = int(input("Enter number of elements in the 'current' array:"))

current = get_input_array(num_current)

num_target = int(input("Enter number of elements in the 'target' array:"))
target = get_input_array(num_target)


addition = get_array_diff(target, current)
deletion = get_array_diff(current, target)

print(f"deletion:{deletion}")
print(f"addition:{addition}")