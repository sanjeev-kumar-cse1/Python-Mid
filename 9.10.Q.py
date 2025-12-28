# # Create the empty dictionary and add three key-value pairs representing a student's name,age,and grade

# d = {
#     # "Name" : "Sanjeev",
#     # "age" : 20,
#     # "grade" : 90
# }
# d["name"] = 'Sanjeev'
# d['age'] = 20
# d['grade'] = 90
# print(d)


# Write a program to print all keys and values of a given dictionary on separate lines.


# d = {
#     "Name" : "Sanjeev",
#     "age" : 20,
#     "grade" : 90
# }
# for item in d.items():
#     print(item)



# Given a dictionary of student marks, print the names of students who scored above 80.

# marks = {
#     'sanjeev' : 90,
#     'kumar' : 95,
#     'Abhi' : 81,
#     'Bair' : 80
# }
# for name, marks in marks.items():
#     if marks > 80:
#         print(name)




# # Write a program to check if a given key exists in a dictionary.

# d ={}
# d ['name'] ='lavi'
# d['location'] ='location'
# if 'lavi' in d.keys(): # here is key so , if present then check key and give value T/F
#     print(True)
# else :
#     print(False)




# # Write a Python script to sum all the values in a dictionary.

# d = {
#     'sanjeev' : 90,
#     'kumar' : 95,
#     'Abhi' : 81,
#     'Bair' : 80
# }
# sum = 0
# for value in d.values():
#     sum = sum + value 
# print(sum)



# # Write a program to count the frequency of each character in a given string using a dictionary.

# li = [1,2,3,4,2,1,1,5] 
# freq= {}
# for num in li:
#     if num in freq:
#         freq[num] += 1
#     else:
#         freq[num] = 1
# print(freq)



# # Given a list of numbers, create a dictionary with each number as the key and its square as the value.
# li = [1,2,3,4,5]
# d= {}
# for i in li:
#     d[i]= i** 2
# print(d)




# # Merge two dictionaries into a single one.
# d = {
#     'sanjeev' : 90,
#     'kumar' : 95,
#     'Abhi' : 81,
#     'Bair' : 80
# }
# marks = {
#     'sanjeev' : 50,
#     'kumar' : 12,
#     'Abhi' : 31,
#     'Bair' : 40
# }

# d.update(marks) 
# print(d)



# # Write a program to remove a key from a dictionary if it exists.    ISKA BATAO

# d = {
#     'name': 'Arya', 
#     'age': 20, 
#     'city': 'Jaipur'
#     }
# exist = 'age'
# if exist in d:
#     del d[exist]
#     print(f"Key '{exist}' removed successfully.")
# else:
#     print(f"Key '{exist}' not found in dictionary.")
# print("Updated dictionary:", d)


# # Create a dictionary from two lists — one for keys and one for values.

# keys = ['name', 'age', 'city']
# values = ['Arya', 20, 'Jaipur']
# one = dict(zip(keys, values))
# print("Dictionary created from lists:", one)


# # Write a program to find the key with the maximum value in a dictionary. ISE BHI BATAO

# d = {
#     'a': 10, 
#     'b': 25, 
#     'c': 15, 
#     'd': 30
#     }
# max_value = max(d, key=d.get)
# print("Dictionary:", d)
# print("Key with maximum value:", max_value)
# print("Maximum value:", d[max_value])

# # Write a program to sort a dictionary by its keys in ascending order.

# d ={
#     "a": 4,
#     "b": 3,
#     "c": 5
# }
# print(sorted(d.items(), key = lambda x : x[1]))


# # Write a program to sort a dictionary by its values in descending order.

# d ={
#     "a": 4,
#     "b": 3,
#     "c": 5
# }
# print(sorted(d.items(), key = lambda x : x[1],reverse=True))



# # Write a program that takes a sentence and returns a dictionary with each word as the key and its count as the value.

# sentence = "Python is fun and Python is powerful"
# words = sentence.split()
# word_count = {}
# for word in words:
#     word = word.lower()  
#     if word in word_count:
#         word_count[word] += 1
#     else:
#         word_count[word] = 1
# print("Sentence:", sentence)
# print("Word frequency dictionary:", word_count)


# sentence = "Python is fun and Python is powerful. The regex is good".replace('.', '').lower().upper().split()
# # sentence = "Python is fun and Python is powerful. The regex is good".replace('.', '').upper().split()
# print(sentence) # ['Python', 'is', 'fun', 'and', 'Python', 'is', 'powerful']
# d = {}
# for word in sentence:
#     if word in d: 
#         d[word] =+ 1
#     else:
#         d[word] = 1
# print(d)

# # Write a program to invert a dictionary (swap keys and values).

# d = {
#     'apple': 1,
#     'banana': 2,
#     'cherry': 3
# }
# inverted_dict = {value: key for key, value in d.items()}
# print("Original dictionary:", d)
# print("Inverted dictionary:", inverted_dict)


# # Given a dictionary of items and their prices, find the total cost of all items priced above 100.

# d = {
#     'bag': 120,
#     'shoes': 250,
#     'pen': 50,
#     'watch': 300,
#     'book': 90
# }
# sum = 0
# for item, price in d.items():
#     if price > 100:
#         sum += price
# print("Items and their prices:", d)
# print("Total cost of items priced above 100:", sum)



# # Write a program to remove duplicate values from a dictionary.

# d = {
#     'a': 10,
#     'b': 20,
#     'c': 10,
#     'd': 30,
#     'e': 20
# }
# unique_dict = {}
# for key, value in d.items():
#     if value not in unique_dict.values():
#         unique_dict[key] = value
# print("Original dictionary:", d)
# print("Dictionary after removing duplicate values:", unique_dict)

# # Write a program to combine two dictionaries by adding values for common keys.
# # Example:
# # d1 = {'a': 100, 'b': 200}
# # d2 = {'a': 300, 'b': 200, 'c': 400}
# # Output → {'a': 400, 'b': 400, 'c': 400}

# d1 = {'a': 100, 'b': 200}
# d2 = {'a': 300, 'b': 200, 'c': 400}
# combined = d1.copy()  
# for key, value in d2.items():
#     if key in combined:
#         combined[key] += value  
#     else:
#         combined[key] = value   
# print("Dictionary 1:", d1)
# print("Dictionary 2:", d2)
# print("Combined dictionary:", combined)


# # Given a nested dictionary of student marks, find the average marks for each student.
# # Example:
# # students = { 'Amit': {'Math': 80, 'Eng': 70}, 'Riya': {'Math': 90, 'Eng': 95} } #### A BHI BATAO

# students = { 
#     'Amit': {'Math': 80, 'Eng': 70}, 
#     'Riya': {'Math': 90, 'Eng': 95} 
# }
# average_marks = {}
# for name, subjects in students.items():
#     total = sum(subjects.values())
#     count = len(subjects)
#     average = total / count
#     average_marks[name] = average
# print("Student Marks:", students)
# print("Average Marks of Each Student:", average_marks)


# other Method

# students = { 
#     'Amit': {'Math': 80, 'Eng': 70}, 
#     'Riya': {'Math': 90, 'Eng': 95} 
# }
# avg1 = sum(list(students['Amit'].values()))/2
# print(avg1)

# avg2 = sum(list(students['Riya'].values()))/2
# print(avg2)





# st = { 
#     'Amit': {'Math': 80, 'Eng': 70}, 
#     'Riya': {'Math': 90, 'Eng': 95} 
# }
# for name, subjects in st.items():
#     avg = sum(subjects.values()) / len(subjects)
#     print(f"{name}'s average: {avg}")   





# # Write a program to find the most frequent value in a dictionary. #### A BHI BATAO

# d = {
#     'a': 10,
#     'b': 20,
#     'c': 10,
#     'd': 30,
#     'e': 20,
#     'f': 10
# }
# value_count = {}
# for value in d.values():
#     if value in value_count:
#         value_count[value] += 1
#     else:
#         value_count[value] = 1
# most_frequent = max(value_count, key=value_count.get)
# print("Original dictionary:", d)
# print("Value frequencies:", value_count)
# print("Most frequent value:", most_frequent)



