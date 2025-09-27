name = "harry"
# print(name.title()) #Converts the first character of each word to uppercase
# print(name.upper()) #Converts all characters to uppercase
# print(name.lower())  #Converts all characters to lowercase
# print(name.capitalize()) #Converts the first character to uppercase
# print(name.casefold()) #Converts string into lowercase and removes all case distinctions

# print(name.index("y")) #Returns the index of the first occurrence of the specified value
# print(name.count("r")) #Returns the number of occurrences of a substring in the given string

# name2 = "harsh"

# sum = name + " " + name2  #Concatenation
# print(sum)

#Lists -> Mutable (can be changed), heterogeneous (can contain different data types)
#can contain tuple lists, sets, dictionaries, floats, integers, strings etc.
List = [1, 2, 3, 4, 5, "harry", 45.6, (1, 2), {1, 2}, {"name": "harry"}]
# print(type(List))
# print(len(List))
# print(List[5])  #Indexing
# print(List[:5:-1])  #Slicing

#Operations on Lists
# List.append("new item")  #Adds an item to the end of the list
# List.insert(5, "inserted item")  #Inserts an item at the specified
# print(List)

# List.extend(["another item", 100, "Multiple items added"])  #Adds multiple items to the end of the list

# print(List)

# List.remove("harry")  #Removes the specified item
# print(List)

# List.pop()  #Removes the last item
# print(List)

# del List[0]  #Removes the item at the specified index
# print(List)

# #Memberships
# List2 = [1, 4, 3, 4, 0, 5.5, 8.7]
# print(max(List2))  #Returns the largest item
# print(min(List2))  #Returns the smallest item
# List2.sort()
# print(List2) #Sorts the list in ascending order (only if all items are of same data type)

#Tuples -> Immutable (cannot be changed), heterogeneous (can contain different data types)
# #can contain tuple lists, sets, dictionaries, floats, integers, strings etc.
# Tuple = (1, 2, 3, 4, 5, "harry", 45.6, (1, 2), {1, 2}, {"name": "harry"})
# # print(type(Tuple))
# # print(len(Tuple))
# # print(Tuple[5])  #Indexing
# # print(Tuple[:5:-1])  #Slicing

# Tuple2 = (1, 4, 3, 4, 0, 5.5, 8.7)
# print(Tuple + Tuple2)  #Concatenation
# print(4 in Tuple2)  #Membership

# #Tuple Unpacking
# a, b, c, d, e, f, g, h, i, j = Tuple
# print(f)

#Dictionaries -> Mutable (can be changed), heterogeneous (can contain different data types)
#can contain tuple lists, sets, dictionaries, floats, integers, strings etc.
# Dict = {
#     "name": "harry",
#     "age": 24,
#     "courses": ["CSE", "IT"],
#     "isMarried": False,
#     "address": {
#         "street": "xyz",
#         "city": "abc"
#     }
# }

# print(type(Dict))
# print(len(Dict))
# print(Dict["name"])  #Accessing value using key

# #updating dictionary
# Dict["age"] = 25
# Dict["phone"] = "1234567890" #Adding new key-value pair
# print(Dict)

# #copy dictionary
# Dict2 = Dict.copy()
# print(Dict2)

# #.update() method to update dictionary
# Dict2.update({"age": 21, "name": "harsh"})

# print(Dict.items())  #Returns a view object that displays a list of a dictionary's key-value tuple pairs
# print(Dict.keys())  #Returns a view object that displays a list of all the keys in the dictionary
# print(Dict.values())  #Returns a view object that displays a list of all the values in the dictionary

# Dict.pop("age")  #Removes the item with the specified key name
# print(Dict)

# print(Dict2.get("name"))  #Returns the value of the specified key

#sets -> Mutable (can be changed), heterogeneous (can contain different data types)
#can contain tuple lists, sets, dictionaries, floats, integers, strings etc.
# Set = {1, 2, 3, 4, 5, "harry", 45.6, (1, 2)}
# print(type(Set))
# print(len(Set))
# print(Set)  #Sets are unordered, so the items will appear in a random order
# print(3 in Set)  #Membership
# # print(Set[0])  #Sets do not support indexing
# # print(Set[:3])  #Sets do not support slicing

# Set.add("new item")  #Adds an item to the set
# print(Set)

# Set.update([6, 7, 8])  #Adds multiple items to the set
# print(Set)

# Set.remove(3)  #Removes the specified item
# print(Set)
# Set.discard(10)  #Removes the specified item, if item not found does not raise an error
# print(Set)

# Set.pop()  #Removes a random item
# print(Set)
# # Set.clear()  #Removes all items from the set
# # print(Set)

# # del Set  #Deletes the set
# # print(Set)  #Raises an error as the set is deleted
# Set2 = {4, 5, 6, 7, 8, 9}
# print(Set2)
# print(Set.intersection(Set2))  #Returns a set that contains the items that are present in both sets
# print(Set.union(Set2))  #Returns a set that contains all items from both sets,
# #duplicates are excluded
# print(Set.difference(Set2))  #Returns a set that contains the items that are only in the first set, and not in both sets

# #superset
# print(Set.issuperset(Set2))  #Returns True if the set contains all items of the specified set, otherwise False


# for i in List:
#     print(i)
#     if List.index(i) == 4:
#         break


# while i in range(0, 7):
#     print(i)
#     i += 1
#     if i == 5:
#         continue

# Dictionary = {
#     "name": "harry",
#     "age": 24,
#     "courses": ["CSE", "IT"],
# }

# for key, value in Dictionary.items():
#     print(f"The key is {key} and the value is {value}")

#functions
def greet(name):
    print("Hello " + name + ", Good Morning!")

greet("harsh")