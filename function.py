

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




