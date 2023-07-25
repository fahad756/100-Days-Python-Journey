# 100 Days of Coding - Day 13

## Sets in Python

Welcome to Day 13 of the 100 Days of Coding challenge! In this challenge, we will explore the concept of sets in Python.

### Sets Overview

Sets are a collection of unique elements, and they do not maintain any specific order. In Python, sets are defined using curly braces `{}` or the built-in `set()` function. Sets automatically remove duplicate elements, making them useful for handling unique data.

### Examples

1. Creating a Set with Duplicate Elements:
   - We demonstrate how to create a set with duplicate elements and observe that duplicates are automatically removed.
   - Output: `{1, 2, 3, 5, 6}`

2. Creating an Empty Set and Checking Its Type:
   - We create an empty set using the `set()` function and check its type.
   - Output: `<class 'set'>`

### Set Methods

1. Set Union (|) and Update:
   - We show how to perform a union operation between two sets using the `union()` method or the `|` operator.
   - We also demonstrate how to update a set with elements from another set using the `update()` method.
   - Output: `{1, 2, 5, 6, 8}`

2. Set Union with Duplicate Elements:
   - We perform the union operation on two sets, and duplicate elements are automatically removed.
   - Output: `{'Pakistan', 'India', 'USA', 'UAE', 'UK', 'GERMANY'}`

3. Set Intersection (&) and Difference (-):
   - We show how to find the intersection and difference between two sets using the `intersection()` and `difference()` methods.
   - Output: `{'Pakistan', 'USA'}` (Intersection), `{'India', 'UAE'}` (Difference)

4. Set Disjoint and Superset/Subset Check:
   - We demonstrate how to check if two sets are disjoint (have no common elements) using the `isdisjoint()` method.
   - We also check if one set is a superset or subset of another set using the `issuperset()` and `issubset()` methods.
   - Output: `False` (Disjoint), `True` (Superset), `True` (Subset)

5. Set add, remove, discard, and pop:
   - We show how to add, remove, and pop elements from a set using the `add()`, `remove()`, `discard()`, and `pop()` methods.
   - Note that `remove()` raises an error if the element is not present, while `discard()` does nothing if the element is not found.
   - Output: `{'India', 'Pakistan', 'NewAdded'}`, `{'Pakistan'}`, `'India'` (Removed by pop())

6. Clearing a Set using `clear()`:
   - We demonstrate how to clear a set and make it empty using the `clear()` method.
   - Output: `set()`

### Explanation

Sets provide an effective way to work with collections of unique elements. They are useful for tasks such as removing duplicates from lists or checking for common elements between multiple datasets. Additionally, sets support various set operations like union, intersection, and difference.

## Resources

To learn more about sets in Python and how to use them effectively, you can refer to the following resources:

- [Python Sets - w3schools](https://www.w3schools.com/python/python_sets.asp)
- [Python Set Documentation - Python.org](https://docs.python.org/3/tutorial/datastructures.html#sets)

Happy learning and coding on Day 13 of the challenge! Keep up the great work!
