# li = [1,2,3,4,]
# d = dict.fromkeys(li, 0) # This is used to set the value into all keys ..of the given list
# print(d) # {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}



# details = {
#     "Name" : "Sanjeev",
#     "Branch" : "CSE",
#     "College" : 123
# }
# # details['name'] # Error dega kyoki name =Name hai.
# details['Name'] # Jaisa key likha hua hai vaise hi find kre , agr capital letter me hai to capital use kre nhi to aap agr small likh rhe ho to error dega.
# print(details)



# details = {
#     "Name" : "Sanjeev",
#     "Branch" : "CSE",
#     "College" : 123
# }
# details['Name'] = 'Rahlll' # Sanjeev = Rahlll
# print(details)



# d= {}
# d ['name'] = 'asd'
# d['age'] = 20
# print(d)



# # (1:1, 2:4, 3:9, 4:16) square of numbers
# d= {}
# for i in range(1, 5):
#     d[i]= i** 2
# print(d)


# # Other method for square or cube.
# # d = {itertor : execution for iterator in range(r) condition }
# d = {i: i**3 for i in range(1,5)}
# print(d)


# # POP 
# d= {
#     'Name' : 'Sanjeev',
#     'Branch' : 'CSE',
#     'Roll' : 12,
# }
# d.pop('Name') # This pair is deleted from d = {}
# print(d)



# # POP ->  
d = {
    'Name' : 'Sanjeev',
    'Branch' : 'CSE',
    'Roll' : 12,
}
# print(d.pop('Name')) # value of name "Sanjeev" out of this d = {} and also print
# print(d) # {'Branch': 'CSE', 'Roll': 12}

# del d['Branch'] # Del is used to remove the key-value pairs from the dictionary and it doesn't return anything

# # PopItem() -> Tuples (key,value)
# # Pop item method removes a key-value pair from a dictionary. This method return key value into the form tuple
print(d.popitem()) # ('Roll', 12), due to this "del d["Branch"]" is deleted in pair

# print(d.clear()) #clear all and print "none"

# print(d) # {} print



# # Membership operator "in / not-in"

# d = {
#     "name" : "Sanjeev",
#     "age" : 20,
# }
# if 'name' in d: # Here we are checking the membership of the key("name"/'name')
#     print(True) # True



# d = {
#     "name" : ["Sanjeev",'kumar', 'sonu ', 'monu'],
#     "age" : 20,
#     "city" : "Jaipur",
#     "occupation" : "Engineer"
# }
# if 'name' in d: # Here we are checking the membership of the key("name"/'name')
#     print(True) # True



# d = {
#     "name" :  ["Sanjeev",'kumar', 'sonu', 'monu'],
#     "age" : 20,
#     "city" : "Jaipur",
#     "occupation" : "Engineer"
# }
# if 'sonu' in d.values(): # Here we are checking the membership of the key("name"/'name')
#     print(True) 
# else:
#     print(False) #False



# d = {
#     "name" :  ["Sanjeev",'kumar', 'sonu', 'monu'],
#     "age" : 20,
#     "city" : "Jaipur",
#     "occupation" : "Engineer"
# }
# if 'sonu' in d["name"]: # Here we are checking the membership of the key("name"/'name')
#     print(True) 
# else:
#     print(False) # True




################# other method ###################

# d = {
#     "name" :  ["Sanjeev",'kumar', 'sonu', 'monu'],
#     "age" : 20,
#     "city" : "Jaipur",
#     "occupation" : "Engineer"
# }
# if 'sonu' in list(d.values())[0]: # Here we are checking the membership of the key("name"/'name')
#         print(True) 
# else:
#     print(False) # True



# li = [[1,2,3],4]
# if 3 in li:
#     print(True)
# else:
#     print(False) # False


# li = [[1,2,3],4]
# if 3 in li[0]:
#     print(True)
# else:
#     print(False) # True