# # 66. Count frequency of elements in a list using a dictionary.

# list = [1, 2, 2, 3, 4, 4, 4, 5]
# freq = {}
# for item in list:
#     if item in freq:
#         freq[item] += 1
#     else:
#         freq[item] = 1
# print(freq) # {1: 1, 2: 2, 3: 1, 4: 3, 5: 1}


# 67. Merge two dictionaries summing values of common keys.



# 68. Find the key with the second highest value.


# # 69. Remove dictionary items with values below a threshold.

# scores = {'A': 45, 'B': 78, 'C': 30, 'D': 90, 'E': 55}
# threshold = 50
# for key in list(scores.keys()):
#     if scores[key] < threshold:
#         del scores[key]
# print(scores) # {'B': 78, 'D': 90, 'E': 55}


# # 70. Group list elements into a dictionary by their first character.

# words = ['apple', 'ant', 'ball', 'bat', 'cat', 'car']
# grouped = {}
# for word in words:
#     first_char = word[0]
#     if first_char not in grouped:
#         grouped[first_char] = [word]
#     else:
#         grouped[first_char].append(word)
# print(grouped) # {'a': ['apple', 'ant'], 'b': ['ball', 'bat'], 'c': ['cat', 'car']}



# 71. Create a dictionary with indices as values for repeated elements.




# 72. Swap keys and values in a dictionary safely.


# # 73. Find all keys with a particular value.

# my_dict = {
#     'a': 10,
#     'b': 20,
#     'c': 10,
#     'd': 30
# }
# target_value = 10
# keys_with_value = []
# for key, value in my_dict.items():
#     if value == target_value:
#         keys_with_value.append(key)
# print(keys_with_value) # ['a', 'c']




# # 74. Count vowels in a string using a dictionary.

# text = "Hello World, Python is fun!"
# vowel_count = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
# for char in text.lower(): 
#     if char in vowel_count:
#         vowel_count[char] += 1
# print(vowel_count) # {'a': 0, 'e': 1, 'i': 1, 'o': 3, 'u': 1}




# # 75. Count words in a sentence ignoring punctuation.

# sentence = "Hello, world! Python is fun; isn't it?"
# punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
# cleaned_sentence = ""
# for char in sentence:
#     if char not in punctuation:
#         cleaned_sentence += char
# words = cleaned_sentence.split()
# word_count = len(words)
# # print("Words:", words)
# print("Total words:", word_count)



# 76. Sort a dictionary by value in descending order.




# # 77. Invert a dictionary with list of keys for duplicate values.

# my_dict = {'a': 1, 'b': 2, 'c': 1, 'd': 3, 'e': 2}
# inverted_dict = {}
# for key, value in my_dict.items():
#     if value not in inverted_dict:
#         inverted_dict[value] = [key]
#     else:
#         inverted_dict[value].append(key)
# print(inverted_dict) # {1: ['a', 'c'], 2: ['b', 'e'], 3: ['d']}




# # 78. Create a dictionary of squares for numbers divisible by 3.

# squares = {}
# for i in range(1, 21):  
#     if i % 3 == 0:
#         squares[i] = i ** 2
# print(squares)




# # 79. Find common keys in two dictionaries.

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}
# common_keys = list(set(dict1) & set(dict2))
# print(common_keys) # ['c', 'b']



# # 80. Find keys present in one dictionary but not in another.

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'b': 4, 'c': 5, 'd': 6}
# unique_keys = dict1.keys() - dict2.keys()
# print(unique_keys) # {'a'} 



# # 81. Group numbers by modulo in a dictionary.

# numbers = [10, 15, 20, 25, 30, 35]
# mod = 4
# grouped = {}
# for num in numbers:
#     remainder = num % mod
#     if remainder not in grouped:
#         grouped[remainder] = [num]
#     else:
#         grouped[remainder].append(num)
# print(grouped) # {2: [10, 30], 3: [15, 35], 0: [20], 1: [25]}




# # 82. Create a nested dictionary from a list of tuples.

# data = [
#     ('fruit', 'apple', 50),
#     ('fruit', 'banana', 30),
#     ('vegetable', 'carrot', 20),
#     ('vegetable', 'spinach', 10)
# ]
# nested_dict = {}
# for parent, child, value in data:
#     if parent not in nested_dict:
#         nested_dict[parent] = {}
#     nested_dict[parent][child] = value
# print(nested_dict) # {'fruit': {'apple': 50, 'banana': 30}, 'vegetable': {'carrot': 20, 'spinach': 10}}




# 83. Filter a dictionary for numeric values greater than a threshold.






# # 84. Count occurrence of each character in a string, ignoring case.

# text = "Hello World"
# text = text.lower()   
# char_count = {}
# for ch in text:
#     if ch != " ":     
#         if ch in char_count:
#             char_count[ch] += 1
#         else:
#             char_count[ch] = 1
# print(char_count) # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}





# # 85. Merge multiple dictionaries keeping the maximum value for common keys.

# dict1 = {'a': 10, 'b': 5, 'c': 8}
# dict2 = {'a': 7, 'b': 12, 'd': 3}
# dict3 = {'a': 15, 'c': 4, 'e': 9}
# merged = {}
# for d in [dict1, dict2, dict3]:
#     for key, value in d.items():
#         if key in merged:
#             if value > merged[key]:
#                 merged[key] = value
#         else:
#             merged[key] = value
# print(merged) # {'a': 15, 'b': 12, 'c': 8, 'd': 3, 'e': 9}




# # 86. Convert dictionary keys into a sorted list.

# data = {'b': 2, 'a': 5, 'c': 1}
# sorted_keys = sorted(data.keys())
# print(sorted_keys) # ['a', 'b', 'c']




# # 87. Find the sum of values for keys starting with a specific letter.

# data = {'apple': 10, 'banana': 5, 'apricot': 8, 'berry': 3}
# letter = 'a' 
# total = 0
# for key in data:
#     if key[0] == letter:  
#         total += data[key]
# print(total) # 18 ,jo jo words a se start ho rha hai uska sum




# # 88. Count frequency of tuples in a list using a dictionary.

# data = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (3, 4)]
# freq = {}
# for t in data:
#     if t in freq:
#         freq[t] += 1
#     else:
#         freq[t] = 1
# print(freq) # {(1, 2): 2, (3, 4): 3, (5, 6): 1}




# # 89. Find duplicate values in a dictionary.

# data = {'a': 10, 'b': 5, 'c': 10, 'd': 3, 'e': 5}
# duplicates = []
# seen = []
# for value in data.values():
#     if value in seen and value not in duplicates:
#         duplicates.append(value)
#     else:
#         seen.append(value)
# print(duplicates) # [10, 5]





# # 90. Replace dictionary values based on a condition.

# data = {'a': 5, 'b': 15, 'c': 8, 'd': 20}
# for key in data:
#     if data[key] > 10:   
#         data[key] = 100 
# print(data) # {'a': 5, 'b': 100, 'c': 8, 'd': 100}





# 91. Create a dictionary from two lists with one-to-many mapping.






# # 92. Count words of different lengths in a string.

# text = "I love Python programming"
# words = text.split()  
# length_count = {}
# for word in words:
#     length = len(word)
#     if length in length_count:
#         length_count[length] += 1
#     else:
#         length_count[length] = 1
# print(length_count) # {1: 1, 4: 1, 6: 1, 11: 1}





# # 93. Group strings by length in a dictionary.

# words = ["I", "love", "Python", "is", "fun"]
# grouped = {}
# for word in words:
#     length = len(word)
#     if length in grouped:
#         grouped[length].append(word)
#     else:
#         grouped[length] = [word]
# print(grouped) # {1: ['I'], 4: ['love'], 6: ['Python'], 2: ['is'], 3: ['fun']}





# # 94. Create a dictionary of squares for odd numbers only.

# numbers = [1, 2, 3, 4, 5, 6, 7]
# squares = {}
# for n in numbers:
#     if n % 2 != 0:  
#         squares[n] = n**2
# print(squares) # {1: 1, 3: 9, 5: 25, 7: 49}




# # 95. Filter out keys containing a specific substring.

# data = {'apple': 10, 'banana': 5, 'apricot': 8, 'berry': 3}
# substring = 'ap'  
# filtered = {}
# for key, value in data.items():
#     if substring not in key:
#         filtered[key] = value
# print(filtered) # {'banana': 5, 'berry': 3}





# # 96. Find keys whose values are prime numbers.

# data = {'a': 2, 'b': 4, 'c': 5, 'd': 6, 'e': 7}
# def is_prime(n):
#     if n < 2:
#         return False
#     for i in range(2, n):  
#         if n % i == 0:
#             return False
#     return True
# prime_keys = []
# for key in data:
#     if is_prime(data[key]):
#         prime_keys.append(key)
# print(prime_keys) # ['a', 'c', 'e']





# # 97. Increment dictionary values based on a list of keys.

# data = {'a': 5, 'b': 3, 'c': 8}
# keys_to_increment = ['a', 'c', 'd']  
# for key in keys_to_increment:
#     if key in data:
#         data[key] += 1
#     else:
#         data[key] = 1  
# print(data) # {'a': 6, 'b': 3, 'c': 9, 'd': 1}






# 98. Find keys with maximum length in a dictionary of strings.

data = {'apple': 'fruit', 'banana': 'fruit', 'kiwi': 'fruit', 'watermelon': 'fruit'}
max_len = 0
max_keys = []
for key in data:
    if len(key) > max_len:
        max_len = len(key)
        max_keys = [key]
    elif len(key) == max_len:
        max_keys.append(key)
print(max_keys) # ['watermelon']





# # 99. Merge two dictionaries keeping minimum values for common keys.

# dict1 = {'a': 10, 'b': 5, 'c': 8}
# dict2 = {'a': 7, 'b': 12, 'd': 3}
# merged = {}
# for key in dict1:
#     merged[key] = dict1[key]
# for key in dict2:
#     if key in merged:
#         if dict2[key] < merged[key]:
#             merged[key] = dict2[key]  
#     else:
#         merged[key] = dict2[key]  
# print(merged) # {'a': 7, 'b': 5, 'c': 8, 'd': 3}






# # 100. Create a dictionary of cumulative sums from a list.

# numbers = [1, 2, 3, 4, 5]
# cumsum_dict = {}
# total = 0
# for n in numbers:
#     total += n
#     cumsum_dict[n] = total
# print(cumsum_dict) # {1: 1, 2: 3, 3: 6, 4: 10, 5: 15}



