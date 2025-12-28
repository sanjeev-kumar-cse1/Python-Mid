#Set does not allow duplicate element into it.(Contain unique elements)
# Mutable
# Indexing formula not working in the set
# Set is represented by " {} "



# s = {1,2,3,4}
# print(type(s)) # <class 'set'>



# s2 = set()
# print(type(s2)) # <class 'set'>



# # Creating set using list
# s3 = set([1,2,3,4,4])
# print(s3) #{1, 2, 3, 4} , here repeated elements are  not show in final set


# # Since indexing is not possible into the set , so we are accessing the element using the iteration
# s5 = {1,2,3,4}
# for num in s5:
#     print(num) # 1 2 3 4 



# # Set modifications
# # Add element 
# s6 = {4,5,6,7}
# s6.add(8) # Which element wants to add.
# s6.add(7) # This is already present so it is only single time only appear.
# print(s6) # {4, 5, 6, 7, 8}



# # Update a set with the union of itself and others
# s6 = {4,5,6,7}
# s6.update([1,2,3,4,5])
# print(s6) # {1, 2, 3, 4, 5, 6, 7}



# # Remove element
# s8 = {1, 2, 3, 4, 5, 6, 7}
# s8.remove(1)
# print(s8) # {2, 3, 4, 5, 6, 7}



# s8 = {1, 2, 3, 4, 5, 6, 7}
# s8.remove(10) # 10 is not present in s8
# print(s8) # Error



# s8 = {1, 2, 3, 4, 5, 6, 7}
# s8.discard(10) # 10 is not present, then ".discard" is not give any error
# print(s8) # {1, 2, 3, 4, 5, 6, 7}



# s8 = {1, 2, 3, 4, 5, 6, 7}
# s8.discard(5) # This is delete element which are in set, if element not found which have to delete then no give any error
# print(s8) # {1, 2, 3, 4, 6, 7}



# # POP element
# s8 = {1, 2, 3, 4, 5, 6, 7}
# s8.pop() # This is removed element randomly
# print(s8)



# my_set = { 'apple', 'this', 'go', 'down'}
# my_set.pop() # Delete random element 
# print(my_set)



# # Clearing all element from the set
# my_set = { 'apple', 'this', 'go', 'down'}
# my_set.clear() # clear all element from set
# print(my_set) # set()



# # List Comprehension 
# li = []
# for i in range(10):
#     li.append(i)
# print(li) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# # List comprehension in Python provides a concise and efficient way to create new lists based on existing iterables (like lists, tuples, or strings). It offers a more compact and often more readable alternative to traditional for loops with append operations.
# l1 = [x for x in range(10)]
# print(l1)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9] 