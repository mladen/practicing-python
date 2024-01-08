# Dictionaries are unordered mappings for storing objects.
# Previously we saw how lists store objects in an ordered sequence, dictionaries use a key-value pairing instead.
# This key-value pair allows users to quickly grab objects without needing to know an index location.
# Dictionaries use curly braces and colons to signify the keys and their associated values.
# {"key1":"value1","key2":"value2"}
# So when to choose a list and when to choose a dictionary?
# Dictionaries: Objects retrieved by key name. Unordered and can not be sorted.
# Lists: Objects retrieved by location. Ordered Sequence can be indexed or sliced.

x = {"key": 4}
print("x['key'] =", x["key"])  # 4

# Dictionaries can hold lists and other dictionaries as well:
y = {"k1": [1, 2, 3]}
print("y['k1'][1] =", y["k1"][1])  # 2

# Can also call methods on that value:
z = {"k1": ["a", "b", "c"]}
print("z['k1'][1].upper() =", z["k1"][1].upper())  # B

print("========================================")

# We can also affect the values of a key as well. For instance:
a = {"k1": 100, "k2": 200}
print("a =", a)  # {'k1': 100, 'k2': 200}
print("a['k3'] = 300")
a["k3"] = 300
print(a)  # {'k1': 100, 'k2': 200, 'k3': 300}

# We can check if some key is in a dictionary:
print("k1" in a)  # True

# We can also check if some value is in a dictionary:
print("100 in a.values() =", 100 in a.values())  # True"

print("========================================")

# We can also get all the keys in a dictionary:
print("a.keys() =", a.keys())  # dict_keys(['k1', 'k2', 'k3'])

# We can also get all the values in a dictionary:
print("a.values() =", a.values())  # dict_values([100, 200, 300])
# Convert to list:
print("list(a.values()) =", list(a.values()))  # [100, 200, 300]

print("========================================")

# Delete a key-value pair:
del a["k1"]
print("del a['k1']")
print(a)  # {'k2': 200, 'k3': 300}

print("========================================")
print("a =", a, "\n")  # {'k2': 200, 'k3': 300}

# Iterate over keys:
print("Iterate over keys:")
for key in a.keys():
    print(key)

# Iterate over values:
print("Iterate over values:")
for value in a.values():
    print(value)

# Iterate over key-value pairs:
print("Iterate over key-value pairs:")
for item in a.items():
    print(item)

# Alternatively:
print("Alternatively:")
for key in a:
    print(key, a[key])
