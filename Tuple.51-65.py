# 51. Find all unique elements in a tuple.




# # 52. Count elements that appear more than once in a tuple.

# t = (1, 2, 3, 2, 4, 1, 5, 6, 5)
# appear = set()
# dup = set()
# for i in t:
#     if i in appear:
#         dup.add(i)
#     else:
#         appear.add(i)
# print(len(dup)) # There are 3 elements appear in this tuple t




# 53. Find the second smallest element in a tuple.




# # 54. Convert a list of tuples into a dictionary.

# lst = [(1, 'A'), (2, 'B'), (3, 'C')]
# d = dict(lst)
# print(d) # {1: 'A', 2: 'B', 3: 'C'}




# # 55. Find tuples that contain a specific element.

# data = [(1, 2, 3), (4, 5, 6), (1, 7, 8), (9, 10, 1)]
# element = 1 # in tuple which have 1 then return tuple.
# result = [t for t in data if element in t]
# print(result) # [(1, 2, 3), (1, 7, 8), (9, 10, 1)]




# # 56. Merge multiple tuples into a sorted tuple.

# t1 = (5, 2, 9)
# t2 = (1, 7, 3)
# t3 = (8, 4, 6)
# merged = t1 + t2 + t3
# sorted_tuple = tuple(sorted(merged))
# print(sorted_tuple) # (1, 2, 3, 4, 5, 6, 7, 8, 9)


# # 57. Swap elements at two indices in a tuple (convert temporarily to list).

# t = (10, 20, 30, 40, 50)
# i, j = 1, 3 # index value which have to swap
# lst = list(t)
# lst[i], lst[j] = lst[j], lst[i]
# swapped = tuple(lst)
# print(swapped) # (10, 40, 30, 20, 50)



# # 58. Find tuples with maximum sum of elements.

# tuples = [(1, 2, 3), (4, 5), (1, 2, 3, 4), (6,)]
# max_tuple = max(tuples, key=sum)
# print(max_tuple) # (1, 2, 3, 4) is tuple ka sum max hoga




# 59. Count tuples based on length in a list of tuples.




# 60. Check if a tuple is strictly increasing.


# # 61. Find the first repeating element in a tuple.

# t = (3, 5, 1, 2, 5, 7, 3)
# appear = set()
# first_repeat = None
# for x in t:
#     if x in appear:
#         first_repeat = x
#         break
#     appear.add(x)
# print(first_repeat) # 5 is repeat first





# 62. Group tuple elements by their data type.




# # 63. Find tuples with elements satisfying a condition (e.g., even numbers only).

# tuples = [(2, 4, 6), (1, 2, 3), (8, 10), (3, 5), (12, 14, 16)]
# even_tuples = [t for t in tuples if all(x % 2 == 0 for x in t)]
# print(even_tuples) # [(2, 4, 6), (8, 10), (12, 14, 16)] 




# # 64. Slice multiple non-contiguous elements from a tuple.

# t = (10, 20, 30, 40, 50, 60, 70)
# indices = [1, 3, 5]
# result = tuple(t[i] for i in indices)
# print(result) # (20, 40, 60)




# # 65. Reverse a tuple without converting to list.

# t = (1, 2, 3, 4, 5)
# reversed = t[::-1]
# print(reversed) # (5, 4, 3, 2, 1)