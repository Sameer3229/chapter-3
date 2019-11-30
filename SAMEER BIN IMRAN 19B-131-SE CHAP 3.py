#!/usr/bin/env python
# coding: utf-8

# # Chapter 3 pythone SAMEER BIN IMRAN 19B-131-SE

# In[1]:


line1="Hello python developer..."
line2="welcome to the world of python!"
print(line1)
print(line2)


# In[2]:


print(0)


# In[4]:


print(0,0,0)


# In[5]:


print("zero")


# In[6]:


x=0
print(x)


# In[1]:


name=input("Enter your name: ")
print(name)


# In[2]:


first=input("Enter your first name: ")
last=input("Enter your last name: ")
line1="Hello "+first+" "+last+"---"
print(line1)
print("Welcome to the world of python!")


# In[3]:


print(eval("9"))


# In[4]:


print(eval("6+4"))


# In[5]:


eval('len([5,5,5,5])')


# In[6]:


x=eval(input("Enter x:  "))
print(x==5)
print(x=="5")


# # PRACTICE PROBLEM 3.1

# In[7]:


#practice problem 3.1
fahrenhiet=eval(input("Enter the tempreture in fahrenhiet:  "))
celsius=5/9*(fahrenhiet-32)
print("The tempreture in degree celsius is ",celsius)


# In[8]:


temp=eval(input("Enter the tempretur:  "))

if temp>86:
    print("it is hot")
    print("be sure to dring liquids.")
print("Good bye.")    


# In[9]:


temp=eval(input("Enter the tempretur:  "))

if temp>86:
    print("it is hot")
    print("be sure to dring liquids.")
print("Good bye.") 


# # PRACTICE PROBLEM 3.2

# In[10]:


#3.2 practice problem
age=eval(input("Enter your age:  "))
if age>67:
    print("You can get your pension benefits.")


# In[12]:


listOfStrings=["Musial","Aaron","Williams","Gehrig","Ruth"]
player= str(input("Enter the plyer name: "))
if player in listOfStrings :
    print("One of the top 5 best player, ever!")


# In[13]:


if north or south or east or west: 
    print( "I can escape." )
    


# In[1]:


temp=eval(input("Enter the tempretur:  "))

if temp>86:
    print("it is hot")
    print("be sure to dring liquids.")
else:
    print("It is not hot.")
    print("Bring a jacket.")
print("Good bye.") 


# # problem 3.3

# In[2]:


#3.3 problem
year=int(input("Enter the year in digit form: "))
if year % 4 == 0:
    print("Could be a leap year.")
else:
    print("Definitely not a leap year.")


# In[3]:


ticket= 441
lottery =int(input("Enter the ticket number:"))
if ticket == lottery:
    print("You won!")
else:
    print("Better luck next time...")


# # problem 3.4

# In[4]:


#3.4
valid_ids = ['joe','sue','hani','sophie']
current_id = input( "Login: " )
if current_id in valid_ids:
     print("You are in!")
else:
     print("User unknown.")
print("Done.")


# In[5]:


valid_ids = ['joe','sue','hani','sophie']
current_id = input( "Login: " )
if current_id in valid_ids:
     print("You are in!")
else:
     print("User unknown.")
print("Done.")


# In[6]:


name=input("Enter the name: ")
print("The word spelled out:")
for char in name:
    print(char)


# In[59]:


animals=["cat","fish","dog"]
for animal in animals:
    print(animal)


# In[7]:


phrase=input("Enter a phrase: ")
for c in phrase:
    if c in "aeiouAEIOU":
        print(c)


# In[8]:


lst=["stop","desktop","top","post"]
for element in lst:
    if len(element) == 4:
        print(element)


# In[63]:


for i in range(5):
    print(i)


# # program 3.6

# In[67]:


#3-6
for i in range(10):
    print(i)
print("=-=-=-=-")
    
for i in range(2):
     print(i)


# In[69]:


for i in range(2,5):
    print(i)


# In[70]:


for i in range(1,14,3):
    print(i)


# # problem 3.7

# In[72]:


#3.7
for i in range(3, 13): 
    print(i)



# In[71]:


for i in range(0, 10, 2):
    print(i)


# In[73]:


for i in range(0, 24, 3): 
    print(i)


# In[74]:


for i in range(3,12, 5): 
    print(i)


# In[75]:


len("goldfish")


# In[76]:


len(["goldfish","cat","dog"])


# In[77]:


max(4,7)


# In[81]:


sum([4,5,6,7])


# In[82]:


def f(x):
    res=(x**2)+1
    return res
print(f(9))


# In[84]:


def f(x):
    res=(x**2)+1
    return res
print(3*f(3)+4)


# # problem 3.8

# In[9]:


#3.8
import math
def perimeter(r):
    per = 2*math.pi*r
    return per
print(perimeter(5))


# In[10]:


#3.8
import math
def perimeter(r):
    per = 2*math.pi*r
    return per
print(perimeter(7))


# In[88]:


def squaresum(x,y):
    return x**2 + y**2
print(squaresum(2,4))


# # problem 3.9

# In[89]:


#3.9
def average(n, n1):
    avg = (n + n1) / 2
    return avg
print(average(1,2))


# In[90]:


def average(n, n1):
    avg = (n + n1) / 2
    return avg
print(average(2,3.5))


# # problem 3.10

# In[11]:


#3.10
def noVowel(s):
    for c in s:
        if (c in 'aeiou') or (c in 'AEIOU'):
            return False
    return True
print(noVowel("crypt"))
print(noVowel("cwm"))
print(noVowel("car"))


# # problem 3.11

# In[102]:


#3.11
def allEven(lst):
    for x in lst:
        if x%2 != 0:
            return False
    return True
print(allEven([8,0,-2,4,-6,10]))
print(allEven([8,0,-1,4,-6,10]))


# In[12]:


def hello(name):
    print("Hello,"+name+ "!")
    return""
print(hello("sam"))    


# # problem 3.12

# In[114]:


#3.12
def negatives(lst):
     for x in lst:
        if x < 0:
            print(x)
print(negatives([4,0,-1,-3,6,-9]))        


# In[19]:



if s=="square":
    def g(x):
        return x*x
else:
    def f(y):
        return y*y*y

print(f(3))
print(f(6))


# In[118]:


def f(x):
    res=x**2+1
    return res
print(f(2))


# # problem 3.13

# In[20]:


#3.13

def average(s1, s2):
    'Calculates and return average of 2 numbers s1 and s2.'
    avg = (s1 + s2) / 2
    return avg
print(average(2,4))


# In[125]:


def negatives(list):
    'prints all negative numbers in list list one in a line.'
    for x in list:
         if x < 0:
            print(x)
print(negatives([4,0,-1,-3,6,-9]))


# In[127]:


d=[2,3,5,8,11]
d[3]=7
print(d)


# In[129]:


a=[2,3,4]
b=a
print(a,b)
b[1]=8
print(b)


# # problem 3.14

# In[132]:


#3.14
a=[5,6,7]
b=a
print(b)
a=3
print(a)


# In[133]:


a=6
b=3
a,b=b,a
print(a)
print(b)


# In[134]:


#3.15
team=["Ava","Elenor","clare","sarah"]
team[0],team[-1] = team[-1],team[0]
print(team)


# In[137]:


def h(lst):
    lst[0]=5
    return lst
mylst=[3,6,9,12]
print(h(mylst))


# In[142]:


#3.16
def swap(team):
    team[0],team[-1] = team[-1],team[0]
    return""
ingredients=["flour","sugar","butter","apples"]
print(swap(ingredients))
print(ingredients)


# # Exercises

# In[163]:


print(eval("2*3+1"))
eval("'hello'")
eval("'hello'+''+'world!'")
eval("'ASCII'.count('I')")
eval('x=5')#eror can't take varaible assignment


# In[166]:


a,b,c=3,4,5
if a < b :
    print("OK")

if c < b :
    print("OK")
else: 
    print("not ok")
    
if a+b == c :
    print("OK")
else: 
    print("not ok")
if a**2+b**2 == c**2 :
    print("OK")


# In[167]:


lst=["January","February","March"]
for word in lst:
    print(word[:3])


# In[170]:


lst=[2,3,4,5,6,7,8,9]
for x in lst:
    if x%2 ==0:
        print(x)


# In[171]:


lst=[2,3,4,5,6,7,8]
for x in lst:
    if(x**2)%8==0:
        print(x)


# In[175]:


for i in range(2):
    print(i,end="")


# In[176]:


for i in range(1):
    print(i,end="")


# In[177]:


for i in range(3,7):
    print(i,end=" ")


# In[178]:


for i in range(1,2):
    print(i,end=" ")


# In[179]:


for i in range(0,4,3):
    print(i,end=" ")


# In[180]:


for i in range(5,22,4):
    print(i,end=" ")


# In[181]:


lst=["cia","secret","mi6","lsi"]
for word in lst:
    if word != "secret":
        print(word)


# In[5]:


lst = str(input("Enter list: " ))
for word in lst:
    if word[0] >= "A" and word[0] <= "M":
        print(word)


# In[2]:


list = eval(input("Enter a list: " ))
print("The first list element is",list[0])
print("The last list element is",list[-1])


# In[6]:


number = eval(input("Enter n: " ))
for i in range(number):
    print(i*i)


# In[3]:


number = eval(input("Enter n: " ))
for i in range(1,number+1):
    if(number%i==0):
        print(i)


# In[ ]:


m = eval(input("Enter n: " ))
for i in range(4):
        print(i*m,end=" ")


# In[7]:


n1 = eval(input("Enter first number: " ))
n2 = eval(input("Enter second number: " ))
n3 = eval(input("Enter third number: " ))
n4 = eval(input("Enter last number: " ))
if (n1+n2+n3)/3 == n4:
    print("Equal")


# In[8]:


x = eval(input("Enter x: " ))
y = eval(input("Enter y: " ))
if x**2+y**2 < 8**2:
    print("It is in!")


# In[31]:


n = (input("Enter 4-digit number: "))
for y in n:
    print(y)


# In[19]:


def reverse_string(s):
    return s[::-1]
print(reverse_string("hello"))


# In[25]:


def pay(wage,hours):
    payment = 0
    if(hours > 40):
        payment = payment + (hours-40)*wage*1.5
        payment = payment + (40)*wage
    else:
        payment = payment + hours*wage
    return payment
print(pay(10,35))
print(pay(10,45))


# In[27]:


def prob(n):
    return 2**(-n)
print(prob(1))
print(prob(2))


# In[35]:


def reverse_int(n):
    x=0
    while(n!=0):
        x*=10
        x+=n%10
        n=n//10
    return x
print(reverse_int(123))
print(reverse_int(908))


# In[40]:


import math
def points(x1,y1,x2,y2):
    distance = str(math.sqrt((x1-x2)**2+(y1-y2)**2))
    if(x1==x2):
        slope = "infinity"
    else:
        slope = str((y2-y1)/(x2-x1))
    print("The slope is "+slope+" and the distance is "+distance)
print(points(0,0,1,1))
print(points(0,0,0,1))


# In[44]:


def abbre(day):
    if(day == "Monday"):
        return "Mon"
    elif(day == "Tuesday"):
        return "Tu"
    elif(day == "Wednesday"):
        return "Wed"
    elif(day == "Thursday"):
        return "Th"
    elif(day == "Friday"):
         return "Fri"
    elif(day == "Saturday"):
        return "Sat"
    elif(day == "Sunday"):
        return "Sun"
print(abbre("Tuesday"))    


# In[47]:


def collision(x1,y1,r1,x2,y2,r2):
    if(math.sqrt((x1-x2)**2+(y1-y2)**2) > r1+r2):
        return False
    else:
        return True
print(collision(0,0,3,0,5,3))   
print(collision(0,0,1.4,2,2,1.4)) 


# In[52]:


def partition(list):
    for name in list:
          if name[0] >= "A" and name[0] <= "M":
                print(name)
    return""           
print(partition(["Eleanor","Evelyn","Sammy","Owen","Gavin"]))                


# In[54]:


def lastF(firstname,lastname):
    return lastname+", "+firstname[0]+"."
print(lastF("Albert","campus"))


# In[57]:


def avg(lists):
     for list in lists:
        print(sum(list)/len(list))
     return''  
print(avg([[95,92,86,87],[66,54],[89],[89,72,100],[33,0,0]]))        


# In[59]:


import math
def hit(x1,y1,r,x2,y2):
    if(math.sqrt((x1-x2)**2+(y1-y2)**2) > r):
        return True
    else:
        return False
    return""
print(hit(0,0,3,3,0))
print(hit(0,0,3,4,0))


# In[62]:


def distance(n):
    return n*340.29/1000
print(distance(3))

