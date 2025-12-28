# .sort is used to sort original list and return nothing



# sorted is return the sorted list or modify and original list not changes

# li1 = [4,3,2,5]
# print(sorted(li1)) #modify
# print(li1)



# d ={
#     "a": 4,
#     "b": 3,
#     "c": 5
# }
# print(sorted(d.items(), key = lambda x : x[1])) # [('b', 3), ('a', 4), ('c', 5)]


# t = [('a',4), ('b',2), ('c',3)]
# print(sorted(t)) # [('a', 4), ('b', 2), ('c', 3)]



# t = [('a',4), ('d',2), ('c',3)]
# print(sorted(t)) # [('a', 4), ('b', 2), ('c', 3)]



t = (3,4)
s = lambda x, i:x[i]
print(s(t,0)) # 3


