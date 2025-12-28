# # Write a program to print numbers from 1 to 10 using a for loop.

# for i in range(1,11):
#     print(i)



# # Print all even numbers between 1 and 20.

# for i in range(2,21,2):
#     print(i)

# # or 

# for i in range(1, 21):
#     if i % 2 == 0:
#         print(i)



# # Given a list numbers = [10, 20, 30, 40, 50], print each element using a for-Loop 

# numbers = [10, 20, 30, 40, 50]
# for num in numbers:
#     print(num)



# # Create a list of 5 student names and print each name with the message "Welcome, [name]".

# students = ["Ravi", "Priya", "Aman", "Sneha", "Karan"]
# for name in students:
#     print("Welcome,", name)




# # Write a program to find the sum of all elements in a list.

# numbers = [10, 20, 30, 40, 50]
# total = 0
# for num in numbers:
#     total += num
# print("Sum of all elements:", total)



# # Print all elements of a list that are greater than 50.

# numbers = [10, 55, 32, 78, 49, 100, 67]
# for num in numbers:
#     if num > 50:
#         print(num)



# # Write a program to count how many numbers in a list are odd.

# numbers = [10, 15, 23, 8, 7, 42, 19, 28]
# count = 0
# for num in numbers:
#     if num % 2 != 0:   # Check if number is odd
#         count += 1
# print("Total odd numbers:", count)



# # Write a program that takes a list of numbers and prints "High" for numbers above 50, otherwise "Low".

# numbers = [10, 55, 32, 75, 49, 100, 25]
# for num in numbers:
#     if num > 50:
#         print(num, "High")
#     else:
#         print(num, "Low")




# # Print the squares of numbers from 1 to 10.

# for i in range(1, 11):
#     print(f"The square of {i} is {i*i}")



# # Write a program that takes a list marks = [45, 67, 32, 89, 90] and prints "Pass" for marks ≥ 40 and "Fail" otherwise.

# marks = [45, 67, 32, 89, 90]
# for mark in marks:
#     if mark >= 40:
#         print(f"{mark}: Pass")
#     else:
#         print(f"{mark}: Fail")





######### SECTION : B ###############




# # Given a list nums = [2, 5, 8, 11, 14, 17, 20], print only the numbers divisible by both 2 and 5.

# nums = [2, 5, 8, 11, 14, 17, 20]
# for num in nums:
#     if num % 2 == 0 and num % 5 == 0:
#         print(num) 



# # Create a list of fruits. Use a for loop to find whether "apple" exists in the list.

# fruits = ["banana", "orange", "mango", "apple", "grapes"]
# found = False
# for fruit in fruits:
#     if fruit == "apple":
#         found = True
#         break
# if found:
#     print("Apple exists in the list!")
# else:
#     print("Apple does not exist in the list.")



# # Given a list a = [1, 2, 3, 4, 5], create a new list with each element multiplied by 3.

# a = [1, 2, 3, 4, 5]
# new_list = []
# for num in a:
#     new_list.append(num * 3)
# print(new_list)



# # From the list numbers = [5, -3, 9, -8, 0, 2], print only the positive numbers.

# numbers = [5, -3, 9, -8, 0, 2]
# for num in numbers:
#     if num > 0:
#         print(num)



# # Write a program to reverse a list using a for loop (without using reverse() or slicing).

# numbers = [1, 2, 3, 4, 5]
# reversed_list = []
# for i in range(len(numbers) - 1, -1, -1):
#     reversed_list.append(numbers[i])
# print("Reversed list:", reversed_list)


# # Write a program that finds the maximum and minimum number in a list using a for loop.

# numbers = [5, 8, 2, 10, 3, 7]
# max_num = numbers[0]
# min_num = numbers[0]
# for num in numbers:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num
# print("Maximum number:", max_num)
# print("Minimum number:", min_num)


# # Given a list names = ["Ankit", "Neha", "Ravi", "Asha"], print only the names that start with "A".

# names = ["Ankit", "Neha", "Ravi", "Asha"]
# for name in names:
#     if name[0] == "A":
#         print(name)


# # Write a program to separate even and odd numbers from a list into two new lists.

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even = []
# odd = []
# for num in numbers:
#     if num % 2 == 0:
#         even.append(num)
#     else:
#         odd.append(num)
# print("Even numbers:", even)
# print("Odd numbers:", odd)


# # Given a list of integers, print "Fizz" if the number is divisible by 3, "Buzz" if divisible by 5, and "FizzBuzz" if divisible by both.

# numbers = [1, 3, 5, 10, 15, 18, 20, 30]
# for num in numbers:
#     if num % 3 == 0 and num % 5 == 0:
#         print("FizzBuzz")
#     elif num % 3 == 0:
#         print("Fizz")
#     elif num % 5 == 0:
#         print("Buzz")
#     else:
#         print(num)


# # Write a program to count vowels in a string using a for loop and if condition.

# text = input("Enter a string: ") 
# count = 0
# vowels = "aeiouAEIOU"
# for ch in text:
#     if ch in vowels:
#         count += 1  
# print("Number of vowels:", count) 




############### SECTION : C ###############


# # Write a program that prints all numbers from 1 to 100, but skips multiples of 7.

# for i in range(1, 101):
#     if i % 7 == 0:
#         continue
#     print(i) 


# # Create a list nums = [10, 20, 30, 40, 50, 60]. Print the index of each element along with its value.

# nums = [10, 20, 30, 40, 50, 60]
# for index in range(len(nums)):
#     print("Index:", index, "Value:", nums[index])


# # Given a list of temperatures, print "Cold" if below 20, "Warm" if between 20–30, and "Hot" if above 30.

# temperatures = [15, 22, 30, 35, 18, 27]
# for temp in temperatures:
#     if temp < 20:
#         print(temp, "Cold")
#     elif 20 <= temp <= 30:
#         print(temp, "Warm")
#     else:
#         print(temp, "Hot")


# # Write a program that removes all duplicate elements from a list without using set().

# numbers = [1, 2, 2, 3, 4, 4, 5, 1, 6]
# unique_numbers = []
# for num in numbers:
#     if num not in unique_numbers:
#         unique_numbers.append(num)
# print("Original list:", numbers)
# print("List without duplicates:", unique_numbers)


# # Write a program to find the second largest number in a list using a for loop and if conditions.

# numbers = [10, 35, 20, 50, 40, 50, 15]
# largest = second_largest = None
# for num in numbers:
#     if largest is None or num > largest:
#         second_largest = largest
#         largest = num
#     elif num != largest and (second_largest is None or num > second_largest):
#         second_largest = num
# print("List:", numbers)
# print("Second largest number:", second_largest)


# # From a list of words, print only those whose length is greater than 5.

# words = ["apple", "banana", "cherry", "kiwi", "strawberry", "grape"]
# print("Words with length greater than 5:")
# for word in words:
#     if len(word) > 5:
#         print(word)



# # Write a program to check whether a list is sorted or not.

# numbers = [1, 2, 3, 4, 5, 6]
# # numbers = [1, 2, 3, 8, 5, 6] # Not stored due to sequencing
# is_sorted = True  
# for i in range(len(numbers) - 1):
#     if numbers[i] > numbers[i + 1]:
#         is_sorted = False
#         break
# if is_sorted:
#     print("The list is sorted.")
# else:
#     print("The list is not sorted.")


# # Given a list of integers, print all pairs of elements whose sum is equal to 10.

# numbers = [1, 2, 3, 7, 5, 8, 6, 4, 0]
# for i in range(len(numbers)):
#     for j in range(i + 1, len(numbers)):
#         if numbers[i] + numbers[j] == 10:
#             print(f"({numbers[i]}, {numbers[j]})")



# # Write a program that prints the factorial of each number in a given list.

# numbers = [1, 3, 5, 7]
# for num in numbers:
#     fact = 1
#     for i in range(1, num + 1):
#         fact *= i
#     print(f"Factorial of {num} is {fact}")


# # Write a program to count how many elements in a list are both positive and even.

# numbers = [10, -4, 3, 8, -2, 12, 7]
# count = 0
# for num in numbers:
#     if num > 0 and num % 2 == 0:
#         count += 1
# print(f"Number of positive and even elements: {count}")
