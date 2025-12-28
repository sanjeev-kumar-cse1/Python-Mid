# Function call itself called recursion 
# Basic case (To stop the function)


# # Five time Hello print
# count = 0
# def display():
#     global count
#     if count == 5:
#         return 
#     print("hello")
#     count += 1 
#     display()
# display()



# # Factorial finding 
# def fact(n):
#     if n == 0 or n == 1: #base case
#         return 1
#     return n * fact(n-1) # recursion call
# print(fact(5))




# # 1 - 10 number print 
# def print_numbers(n):
#     if n > 0:
#         print_numbers(n - 1)
#         print(n)

# print_numbers(10)




# # other-method 
# def display(n):
#     if n > 5:
#         return
#     print(n)
#     display(n+1)
# display(1) 



# # 1 - 10 number sum print 
# def sum_numbers(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum_numbers(n - 1)
# result = sum_numbers(10)
# print("Sum =", result)




# # count digit in numbers 321 = 3 digit
# count = 0 # We have this count variable 
# def count_digit(n):
#     global count # accessing global variable
#     if n == 0: # base case n==0 -> 0
#         return 0
#     count += 1 # when n!=0  then it increase the count value with one
#     count_digit(n//10) # recursion call
# count_digit(123)
# print(count)



# #User input other method
# count = 0 # We have this count variable 
# def count_digit(n):
#     global count # accessing global variable
#     if n == 0: # base case n==0 -> 0
#         return 0
#     count += 1 # when n!=0  then it increase the count value with one
#     count_digit(n//10) # recursion call
# n = int(input("ENter any number: "))
# count_digit(n)
# print(count)




# a = 0
# b = 1
# for i in range(10):
#     print(a)
#     a,b = a+b, a



# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(10):
#     print(fib(i))