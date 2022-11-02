

x = 100
y = 20 

print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x%y)

s = 100
t = 50

print(s+t)
print(s*t)
print(s/t)
print(s%t)
print(s%t)

# 10 50 lines ---- function


# program 1

# def  keyword
# calculator - functionName
# a, b -- parameter
#  :  print(a+b)  staments
    # print(a-b)
    # print(a*b)
    # print(a/b)
    # print(a%b)

def calculator(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a%b)
calculator(12,6) # function call , arguments
calculator(40,20)

# function without parameter and without return type

def sum():
    print(9+9)
sum()
sum()
sum()
sum()

# function with parameter and without return type
def sumB(a,b):
    print(a+b)
sumB(12,6)
sumB(100,50)


# 100 show 
# 100 given

# function with parameter and with return type 
def sumC(a,b):
    return a + b
q1 = sumC(100,50)
print(q1)
print(q1 + q1)
print(q1 -50)
print(q1 * 0.50)


# print("hello")
a = print("hello")
print(a)

def sub(x,y):
    print(x-y)
    return x - y
q2 = sub(12,3)
print(q2)


# even or odd 
q3 = 100
if(q3 % 2 == 0):
    print("number is even")
else:
    print("number is odd")

# avoid repeattion using function
def even_odd(x):
    if(x % 2 == 0):
        print("number is even")
    else:
        print("number id odd")

even_odd(12)
even_odd(13)


# function returning more than one value 


def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return q1

q2 = calculator(12,1)
print(q2)
################################################
# list , tuple , dictionary , set
def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return [q1,q2,q3,q4,q5]

listC = calculator(12,1)
print(listC)

###########################################
def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return q1,q2,q3,q4,q5

listD = calculator(12,1)
print(listD)
#####################################################

def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return {
        'addition':q1,
        'subtraction':q2,
        'multiplication':q3,
        'division':q4,
        'modulus':q5
        }

listE = calculator(12,1)
print(listE)



def calculator(a,b):
    q1 = a + b
    q2 = a - b
    q3 = a * b
    q4 = a / b
    q5 = a % b
    return {q1,q2,q3,q4,q5}

listE = calculator(20,5)
print(listE)

# int 
# float 
# boolean 
# string 
# dictionary 
# tuple 
# list 
# set 

# number as a parameter and number as return type 
r1 = 10
r2 = 5
def Addition(x,y):
    #x = r1 # separate memory
    #y = r2 # separate memory
    return x + y
w3 = Addition(r1,r2)
print(w3)


# passing list as param

cities = ["pune","mumbai","nagpur","kolkalta"]
def AddCity(listC):
    # listC = cities # reference added to same memory
    listC.append("wardha")
    print(listC) 
AddCity(cities)
print(cities) 

#----------------------------------------------
# passing dict as param
# city ---- pune
info = {
    'firstName':"chinmay",
    'lastName':"deshpande",
    'age':12,
}

def addCity(dictInfo):
    # dictInfo = info
    dictInfo['city'] = "pune"
    print(dictInfo) # output
addCity(info)
print(info) # output

# passing function as parameter to another funtion
# function class function
def sum(x,y):
    return x + y
def addition(a,b,fn):
    #fn = sum
    # def fn(x,y):
    #     return x+ y

    q9 = fn(a,b)
    print(q9)

addition(120,20,sum)

# print(sum) # printing function reference
# sum(12,3) # call function





















