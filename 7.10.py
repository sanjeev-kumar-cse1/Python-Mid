# s8 = {1, 2, 3, 4, 5, 6, 7}
# s8.discard(10) # 10 is not present, then .discard is not give any error
# print(s8) # {1, 2, 3, 4, 5, 6, 7}



# # Dictionary is a build in data type in py that allows you to store key value pair data
# # This is mutable/changeable
# d = {} # This is empty dictionary representation way
# d1 = dict() # Using constructors 


# d = {#key not change : value can change
#     'key1' : 'jaipur',
#     'key2' : 'jaipuri'
# }
# print(d['key2']) 




# details = {
#     "Name" : "Sanjeev",
#     "Branch" : " CSE",
#     "Loac" : " Jaipur",
#     "Mob.No." : 33220
# }
# s = details.keys() # Return all keys
# print(s)
# t = details.values() # Return all values
# print(t)

# # details.items() # All the value-key in pairs print, like tuple.
# print(details.items()) 




# Implementing the for loop into the dictionary
details = {
    "Name" : "Sanjeev",
    "Branch" : " CSE",
    "Loac" : " Jaipur",
    "Mob.No." : 33220
}
# for key in details.keys():
#     print(key) # only show 

# for value in details.values():
#     print(value) #only show

# for item in details.items():
#     print(item) # show in tuple-packing () formate or in pair or key value both print  

# for key, value in details.items(): 
#     print(f"{key}: {value}") # show in tuple-unpacking not () formate or in pair or key value both print




# # Frequency checking { 1:3, 2:2, 3:1, 4:1 , 5:1}
# li = [1,2,3,4,2,1,1,5]
# freq= {}
# for num in li:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)




# d = {
#     [1,2]:[1,2,3,4],
# }
# print(d) # Type error



# d = {
#     (1,2):[1,2,3,4]
# }
# print(d) # {(1, 2): [1, 2, 3, 4]}





# Creating the dictionary from two lists

# keys = [1,2,3,4,5]
# values = ["sanjeev", "location", "A20", "Regex", "Jaipur"]
# d = {}
# # for key,values in 
# s = zip(keys, values) # When two or more list write with all
# print(s) # <zip object at 0x00000191518AB9C0> This is address where store
# t = list(zip(keys, values))
# print(t) # [(1, 'sanjeev'), (2, 'location'), (3, 'A20'), (4, 'Regex'), (5, 'Jaipur')]



# other method 

# keys = [1,2,3,4,5]
# values = ["sanjeev", "location", "A20", "Regex", "Jaipur"]
# d = {}
# for key,value in list(zip(keys, values)): 
#     d[key] = value
# print(d) # {1: 'sanjeev', 2: 'location', 3: 'A20', 4: 'Regex', 5: 'Jaipur'}




# keys = [1,2,3,4,5]
# values = ["sanjeev", "location", "A20", "Regex", "Jaipur"]
# d = {}
# for key,value in list(zip(keys, values)): 
#     d[key] = value
# print(d) # {1: 'sanjeev', 2: 'location', 3: 'A20', 4: 'Regex', 5: 'Jaipur'}

# y = dict(zip(keys, values)) # {1: 'sanjeev', 2: 'location', 3: 'A20', 4: 'Regex', 5: 'Jaipur'}
# print(y)