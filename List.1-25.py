# # 1. Merge two lists and remove duplicates.

# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# merge = list(set(list1 + list2))
# print( merge) # [1, 2, 3, 4, 5, 6, 7, 8]



# # 2. Find the second largest element in a list without using sort().

# numbers = [10, 20, 4, 45, 99]
# first_max = max(numbers)
# while first_max in numbers:
#     numbers.remove(first_max)
# second_max = max(numbers)
# print(second_max) # 45



# # 3. Find the longest increasing subsequence in a list.



# # 4. Rotate a list by k positions to the right.

# nums = [1, 2, 3, 4, 5, 6, 7]
# k = 3
# k = k % len(nums)  
# for i in range(k):
#     last = nums.pop()
#     nums.insert(0, last)
# print("Rotated list:", nums)




# # 5. Count the number of sublists inside a list of lists.

# main_list = [1, [2, 3], [4, 5, 6], 7, [8]]
# count = 0
# for item in main_list:
#     if type(item) == list:
#         count += 1
# print(count) # 3



# # 6. Find all pairs in a list whose sum equals a target value.

# nums = [1, 2, 3, 4, 5, 6, 7]
# target = 7
# pairs = []
# for i in range(len(nums)):
#     for j in range(i+1, len(nums)):
#         if nums[i] + nums[j] == target:
#             pairs.append((nums[i], nums[j]))
# print(pairs) # [(1, 6), (2, 5), (3, 4)]




# # 7. Find the longest consecutive sequence of numbers in a list.




# # 8. Separate even and odd numbers into two lists.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# even = []
# odd = []
# for num in nums:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("Even numbers:", even) # Even numbers: [2, 4, 6, 8]
# print("Odd numbers:", odd) # Odd numbers: [1, 3, 5, 7, 9]




# 9. Find the indices of all occurrences of a specific element.



# # 10. Replace negative numbers with 0 in a list.

# nums = [3, -1, 5, -7, 0, 9, -2]
# for i in range(len(nums)):
#     if nums[i] < 0:
#         nums[i] = 0
# print(nums) # [3, 0, 5, 0, 0, 9, 0] 




# # 11. Merge n sorted lists into a single sorted list.

# lists = [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
# merge = [num for sublist in lists for num in sublist]
# merge.sort() # If this line is not then [1, 4, 7, 2, 5, 8, 3, 6, 9]
# print(merge) # [1, 2, 3, 4, 5, 6, 7, 8, 9]





# # 12. Remove all elements appearing more than once.

# nums = [1, 2, 2, 3, 4, 4, 5]
# once = list(set(nums))
# print(once) # [1, 2, 3, 4, 5]



# # 13. Find the element that appears most frequently.

# nums = [1, 2, 2, 3, 4, 2, 5, 3, 3, 3] 
# more = max(nums, key=nums.count) 
# frequency = nums.count(more)
# print(f"{more}:{frequency}")




# # 14. Find the intersection of multiple lists.

# l1 = [1, 2, 3, 4]
# l2 = [2, 3, 5]
# l3 = [2, 3, 6]
# intersection = list(set(l1) & set(l2) & set(l3))
# print(intersection) # [2, 3]




# 15. Flatten a nested list of arbitrary depth.




# 16. Move all zeros in a list to the end without changing order. 




# 17. Count the number of prime numbers in a list.





# 18. Find the sublist with the maximum sum (Kadane’s algorithm).




# # 19. Split a list into chunks of size k.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# k = 3
# chunks = []
# for i in range(0, len(nums), k):
#     chunks.append(nums[i:i+k])
# print(chunks) # [[1, 2, 3], [4, 5, 6], [7, 8, 9]]




# 20. Find pairs with the minimum difference.



# 21. Check if a list can be made strictly increasing by removing one element.




# # 22. Group elements by remainder when divided by n.

# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# n = 3
# groups = {}
# for num in nums:
#     remainder = num % n
#     if remainder not in groups:
#         groups[remainder] = []
#     groups[remainder].append(num)
# print("Grouped by remainder:", groups)




# # 23. Find elements appearing in only one of the two lists.

# l1 = [1, 2, 3, 4]
# l2 = [3, 4, 5, 6]
# once = list(set(l1) ^ set(l2))
# print(once) # [1, 2, 5, 6]



# 24.Find the longest repeating element streak.





# # 25. Compute the running sum of a list.

# nums = [1, 2, 3, 4, 5]

# running_sum = []
# sum = 0
# for num in nums:
#     sum += num
#     running_sum.append(sum)
# print(running_sum) # [1, 3, 6, 10, 15] 



