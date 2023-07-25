# SETS

# Sets are a collection of unique elements and do not maintain any specific order.
# In this code, we will explore various set operations and methods.

# Example 1: Creating a set with duplicate elements
set_val = {1, 2, 3, 5, 3, 6}
print(set_val)  # Output: {1, 2, 3, 5, 6} (Note that duplicate elements are removed)

# Example 2: Creating an empty set and checking its type
val = set()
print(type(val))  # Output: <class 'set'>

# SETS METHODS

# Example 3: Set Union (|) and Update
set1 = {1, 2, 5, 6}
set2 = {2, 5, 8}
print(set1.union(set2))  # Output: {1, 2, 5, 6, 8}
set1.update(set2)  # Updates set1 with elements from set2
print(set1)  # Output: {1, 2, 5, 6, 8} (Note that set1 is updated)

# Example 4: Set Union with duplicate elements
countries1 = {"Pakistan", "India", "UAE", "USA"}
countries2 = {"UK", "GERMANY", "Pakistan", "USA"}
final = countries1.union(countries2)
print(final)  # Output: {'Pakistan', 'India', 'USA', 'UAE', 'UK', 'GERMANY'} (Note that duplicate elements are removed)

# Example 5: Set Intersection (&) and Difference (-)
countries1 = {"Pakistan", "India", "UAE", "USA"}
countries2 = {"UK", "GERMANY", "Pakistan", "USA"}
final = countries1.intersection(countries2)
print(final)  # Output: {'Pakistan', 'USA'} (Elements present in both sets)

diff = countries1.difference(countries2)
print(diff)  # Output: {'India', 'UAE'} (Elements present in countries1 but not in countries2)

# Example 6: Set Disjoint and Superset/Subset Check
countries1 = {"Pakistan", "India", "UAE", "USA"}
countries2 = {"UK", "GERMANY", "Pakistan", "USA"}
countries3 = {"India", "Pakistan"}

disjoint = countries1.isdisjoint(countries2)
print(disjoint)  # Output: False (Sets have at least one common element)

superst = countries1.issuperset(countries3)
print(superst)  # Output: True (countries1 contains all elements of countries3)

subset = countries3.issubset(countries1)
print(subset)  # Output: True (countries3 is a subset of countries1)

# Example 7: Set add, remove, discard, and pop
countries3.add("NewAdded")
print(countries3)  # Output: {'India', 'Pakistan', 'NewAdded'}

# The remove() method raises an error if the element is not present in the set.
countries3.remove("NewAdded")
print(countries3)  # Output: {'India', 'Pakistan'}

# The discard() method removes the element if it exists, but does nothing if the element is not present.
countries3.discard("sss")
print(countries3)  # Output: {'India', 'Pakistan'}

# The pop() method removes and returns an arbitrary element from the set.
popval = countries3.pop()
print(countries3)  # Output: {'Pakistan'}
print(popval)  # Output: 'India' (Note that 'India' is removed and returned by pop())

# Example 8: Clearing a set using clear()
clr = countries3.clear()
print(countries3)  # Output: set()
print(clr)  # Output: None (Note that clear() does not return anything)
