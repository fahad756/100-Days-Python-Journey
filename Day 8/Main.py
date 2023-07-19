# LIST

Randomv = [1,"Fahad",4,1,"4","Home",7]

# print(Randomv[1:-2])

print(Randomv[0:6:2])
#
# for random in Randomv:
#     print(random)

#List comprehension

lst  = [i for i in range(4)]
print(lst)

lst = [i+i for i in range(5)]
print(lst)


even = [i*i for i in range(6) if i%2==0]
print(even)

#List Manipulation
numbers = [4,6,3,1,5,2]
numbers.append(7)
print(numbers)
numbers.sort()
print(numbers)
print(numbers.index(1))

lists = numbers
lists[0] = 9

numbers.insert(1,55)
print(numbers)

fahad = [12,568,876]
numbers.extend(fahad)
print(numbers)
k = numbers + fahad
print(k)