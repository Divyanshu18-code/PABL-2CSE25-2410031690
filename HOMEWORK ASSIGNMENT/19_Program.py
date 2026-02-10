#Given two arrays a[] and b[], your task is to determine whether b[] is a subset of a[].

def is_subset(a, b):
    set_a = set(a)

    for element in b:
        if element not in set_a:
            return False
    return True

print(is_subset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7]))  # output = True
print(is_subset([1, 2, 3, 4, 4, 5, 6], [1, 2, 4]))  # output = True
