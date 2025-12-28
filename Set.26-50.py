# # 26. Find elements appearing in exactly two out of three sets.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {4, 5, 6, 7}
# exactly_two = ((set1 & set2) | (set2 & set3) | (set1 & set3)) - (set1 & set2 & set3)
# print(exactly_two) # {3, 5, 6} Jo s1 me ho phir vo s2 me bhi aae , s2 me ho vo s3 me bhi aae



# # 27. Check if a set is a proper subset of another set.

# set1 = {1, 2, 3}
# set2 = {1, 2, 3, 4, 5}
# print(set1 < set2) # True




# # 28. Count unique elements across multiple sets.

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = {5, 6, 7}
# unique = set1 | set2 | set3
# count = len(unique)
# print(unique) # {1, 2, 3, 4, 5, 6, 7}
# print(count) # 7




# # 29.Find the first duplicate element using a set.

# nums = [1, 3, 4, 2, 5, 3, 2]
# seen = set()
# for num in nums:
#     if num in seen:
#         print(num) # 3
#         break
#     seen.add(num)


# 30.Find all common divisors of numbers in a set.



# 31. Identify elements that are powers of 2 in a set.




# # 32. Merge multiple sets and remove duplicates.

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# set3 = {5, 6, 7}
# merged = set1.union(set2, set3)
# print(merged) # {1, 2, 3, 4, 5, 6, 7}



# # 33. Find elements that appear in one set but not in the others.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {5, 6, 7, 8}
# sets = [set1, set2, set3]
# all_elements = set1 | set2 | set3
# common_elements = (set1 & set2) | (set2 & set3) | (set1 & set3)
# unique_elements = all_elements - common_elements
# print(unique_elements) # {8, 1, 2, 7}



# # 34.Check if two sets are permutations of each other.

# set1 = {1, 2, 3}
# set2 = {3, 1, 2}
# if set1 == set2: # output:- Both sets are permutations of each other
#     print("Both sets are permutations of each other")
# else:
#     print("They are not permutations")





# # 35. Find missing numbers from a consecutive range using a set.

# nums = {1, 2, 4, 6, 7}
# full_set = set(range(min(nums), max(nums) + 1))
# missing = full_set - nums
# print(missing) # {3,5}




# # 36. Count elements that are multiples of a given number.

# nums = [2, 3, 4, 6, 8, 9, 12]
# n = 3  
# count = 0
# for x in nums:
#     if x % n == 0:
#         count += 1
# print(count) # 4 but on other IDE there is 3





# 37. Create a set of all uppercase letters in a string.



# # 38. Find intersection of more than two sets efficiently.

# set1 = {1, 2, 3, 4, 5}
# set2 = {2, 3, 5, 7}
# set3 = {3, 5, 8, 9}
# common = set1.intersection(set2, set3)
# print(common) # {3,5}




# # 39. Find elements that are not in any of the other sets.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {5, 6, 7, 8}
# print(set1 ^ set2 ^ set3) # {1, 2, 7, 8}





# 40. Check if a set is equal to the union of its subsets.



# # 41. Count unique pairs across sets with sum equal to a target.

# set1 = {1, 2, 3, 4}
# set2 = {2, 3, 4, 5}
# target = 6
# pairs = set()
# for a in set1:
#     for b in set2:
#         if a + b == target:
#             pairs.add((a, b)) 
# print(pairs) # {(2, 4), (3, 3), (4, 2), (1, 5)}
# print(len(pairs)) # 4



# 42. Find symmetric difference across multiple sets.

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# set3 = {5, 6, 7, 8}
# print(set1 ^ set2 ^ set3) # {1, 2, 7, 8}



# # 43. Filter a set for elements divisible by 3 and 5.

# nums = {1, 3, 5, 6, 9, 10, 15, 30, 45, 50}
# filter = {x for x in nums if x % 3 == 0 and x % 5 == 0}
# print(filter) # {45, 30, 15}





# # 44. Remove elements from a set that exist in another list.

# nums_set = {1, 2, 3, 4, 5, 6}
# nums_list = [2, 4, 6, 8]
# result = nums_set - set(nums_list)
# print(result) # {1, 3, 5}




# 45. Compute the set of factors for each number in a set.


# 46. Identify prime numbers in a set.



# # 47. Group numbers by parity (even/odd) in sets.

# nums = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even = {x for x in nums if x % 2 == 0}
# odd = {x for x in nums if x % 2 != 0}
# print("Even numbers:", even) # Even numbers: {2, 4, 6, 8, 10}
# print("Odd numbers:", odd) # Odd numbers: {1, 3, 5, 7, 9}





# # 48. Find common elements without using intersection().

# set1 = {1, 2, 3, 4}
# set2 = {3, 4, 5, 6}
# common = {x for x in set1 if x in set2}
# print(common) # {3,4}



# 49. Find elements with maximum length in a set of strings.



# 50. Create a set of squares from 1 to n.






