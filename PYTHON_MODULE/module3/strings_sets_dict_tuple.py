#strings in python Immutble :


word = "python"
print(len(word))  # Output: 6
#concat
word2="I hate"
print(word2+" "+word)
#indexing 
print(word[0])  # Output: 'p'
print(word[-1]) # Output: 'n'

for ch in word:
    print(ch)

#slicing
print(word[0:3]) # Output: 'pyt'


#formatting 
a = 5
b = 6
sum = a+b
print("sum of {} and {} is {}",format(a,b,sum))
#index based formatting 
print("sum of {0} and {1} is {2}",format(a,b,sum))
#value based formatting
print("sum of {a} and {b} is {sum}",format(a=a,b=b,sum=sum))

#f string formatting
print(f"sum of {a} and {b} is {sum}")
print(f"avg of {a} and {b} is {(a+b)/2}")


#lists mutable 

my_list = [1, 2, 3, 4, 5,"abc","ab",True]
print(my_list)
print(len(my_list))  # Output: 5
print(type(my_list))  # Output: <class 'list'>

#slicing 
print(my_list[0:3])  # Output: [1, 2, 3]
print(my_list[-5:-2]) 

my_list.append("new_item")
print(my_list)
my_list.remove(3)
print(my_list)  
my_list[0] = 10
print(my_list)
print(my_list.insert("ab",2))  
print(my_list.count(2)) 
my_list.sort()
print(my_list)

my_list.sort(reverse=True)
print(my_list)
print(my_list.reverse())
print(my_list.pop())
print(my_list.clear())
print(my_list.extend([6,7,8]))


nums = [4, 2, 9, 1, 5]
x = 1
idx=0
for val in nums:
    if(val== x):
        print(f"{x} found at idx = {idx}")
        break
    idx+=1


#tuples immutable
my_tuple = (1, 2, 3, 4, 5,"abc","ab",True)
print(my_tuple)
print(len(my_tuple))
print(type(my_tuple))  # Output: <class 'tuple'>
print(my_tuple[0])  # Output: 1
print(my_tuple[-1])  # Output: True
print(my_tuple[0:3])  # Output: (1, 2, 3)

tup = (1)
print(type(tup))  # Output: <class 'int'>
tup = (1,)
print(type(tup))  # Output: <class 'tuple'>

my_tuple.index(3)
print(my_tuple.count(2))


#dictionaries mutable
my_dict = {"key1": "value1", "key2": "value2", "key3": "value3"}
print(my_dict)
print(len(my_dict))  # Output: 3
print(type(my_dict))  # Output: <class 'dict'>
print(my_dict["key1"])  # Output: 'value1'

info={"name":"John","age":30,"city":"New York"}
print(info)
info["age"]=31
print(info)

print(info.keys())
print(info.values())
print(info.items())
info.pop("city")
print(info)
dict_keys=list(info.keys())
print(dict_keys)
dict_values=list(info.values())
print(dict_values)

print(info.get("name"))


#sets
#immutable elements inside mutable container
#no duplicates 
s={1,2,3,4,5,5,5,5}
print(s)
print(type(s))
empty_set=set()
print(type(empty_set))  
s.add(6 )
print(s)
s.remove(3)
print(s)
print(len(s))  # Output: 5
print(4 in s)  # Output: True

print(s)

s.union({7,8,9})
print(s)
s.intersection({4,5,6,7})
print(s)


