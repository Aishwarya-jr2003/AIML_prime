# age = 17
# if age>=18:
#     print("you can vote in elections")

# else:
#     print("you cannot vote in elections")   
# print("you are an adult")

# username=input("enter username:")
# password=input("enter password:")

# if(username=="admin" and password=="pass"):
#     print("login successful")
# else:
#     if(username!="admin"):
#         print("username incorrect")
#     if(password!="pass"):
#         print("password incorrect")
#     print("login failed")

# color=input("enter your favorite color:")   
# match color:
#     case "red": 
#         print("your favorite color is red")
#     case "blue":            
#         print("your favorite color is blue")
#     case "green":   
#         print("your favorite color is green")
#     case _:
#         print("your favorite color is not red, blue or green")

count=1
while(count<=5):
    print("hello world",count)
    count+=1    

num=int(input("enter a number:"))
count=1
while(count<=10):
    print(num,"x",count,"=",num*count)
    count+=1
    
string ="hello"
for char in string:
    print(char)
if 'o' in string:
    print("character found")
#in membership operator
for i in range(1,6):
    print(i)



word="pythonoooooooooooooooooooo"
count=0
for char in word:
    if(char=='o'):
       
      count+=1

print("the count of o in the word is",count)


#range(start,stop,step)
sum = 0
for i in range(1,6):
    sum+= i
print("the sum is",sum)


def hello():
    print("hello world from function")
hello()

def sum(a,b=1):
    return a+b
print(sum(4))

avg = lambda x,y:(x+y)/2
print("the average is",avg(5,15))

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print("the factorial is",factorial(5))

def cal(n):
    fact=1
    for i in range(1,n+1):
        fact*=i 
    return fact

n=int(input("enter a number to find factorial:"))
print("the factorial using iterative method is",cal(n)) 