# Defining the function with "def" keyword
def add(a,b):
    return a+b
add(10,40) # 50 # calling the function with arguments



# # Parameter (paisa)
# def dost(paisa):
#     return "Ye le bhai tere lie coffee!"
# dost(300) # Ye le bhai tere lie coffee ,, here is argument 300



# # Check this is even or not

# def is_even(n):
#     if n % 2 == 0:
#         return True
#     return False
# is_Even = is_even(20)
# if is_Even:
#     print("Even") # Even 
# else:
#     print("Not even")



# Check prime or not

# def is_prime(n):
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True
# s = is_prime(7) 
# print(s) # false

# # Find prime between 2 and 100  
# def is_prime(n):
#     for i in range(2,100):
#         if is_prime(i):
#             print(i, end = "") # 2,3,5,7,11....97
# print(is_prime)




# # Fibbonacci number 

# a = 0
# b = 1
# for i in range(10):
#     print(a)
#     a,b = a+b, a




# # Using function

# def fibb(n):
#     a = 0
#     b = 1
#     li = []
#     for i in range(10):
#         li.append(a)
#         a,b = a+b, a
#     return li
# print(fibb(10)) # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]





# def fibb(n):
#     a = 0
#     b = 1
#     for i in range(10):
#         print(a)
#         a,b = a+b, a
# print(fibb(10)) # 0,1,1,2,3,....,34, none



# def fact(n):
#     prod = 1
#     for i in range(1,n+1):
#         prod *= i
#     return prod
# print(fact(5)) # 120


