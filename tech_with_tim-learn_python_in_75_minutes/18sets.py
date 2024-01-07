# Sets are unordered collections of unique elements (all we care is if an element is in a set or not)
# Sets are mutable
# Sets are unordered
# Sets are unindexed
# Sets are iterable
# Sets are unhashable
# Sets are heterogeneous
# Sets are dynamic
# Sets are used to remove duplicates
# Sets are used to perform mathematical operations (union, intersection, difference, symmetric difference)
# Sets are used to check if an element is in a set

s = {
    4,
    2,
    55,
    31,
    2,
}  # non-empty set; WARNING: if we would have written s = {}, then we would have created an empty DICTIONARY and not an empty SET!
x = set()  # this is how we create an empty set
print(
    "Set s:", s
)  # {2, 4, 55, 31}; notice that the order of the elements is not the same as the order in which we added them; this is because sets are unordered
# also, the set is not sorted either

# Checking if an element is in a set is very fast; it is O(1), meaning - it is done in constant time, which is faster than lists and tuples
# this is because sets are implemented using hash tables
print("Is 55 in s?", 55 in s)  # True

# Union of sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}
# print("Union of s1 and s2:", s1 | s2)  # {1, 2, 3, 4, 5}
print("Union of s1 and s2:", s1.union(s2))  # {1, 2, 3, 4, 5}

# Difference of sets
# print("Difference of s1 and s2:", s1 - s2)  # {1, 2}
print("Difference of s1 and s2:", s1.difference(s2))  # {1, 2}

# Intersection of sets
# print("Intersection of s1 and s2:", s1 & s2)  # {3}
print("Intersection of s1 and s2:", s1.intersection(s2))  # {3}

# Symmetric difference of sets
# print("Symmetric difference of s1 and s2:", s1 ^ s2)  # {1, 2, 4, 5}
print("Symmetric difference of s1 and s2:", s1.symmetric_difference(s2))  # {1, 2, 4, 5}
