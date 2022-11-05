# # positional arguments
# # def sum(a,b):
# #     print(a+b)
# # sum(12)
# # Keyword arguments 
# # program1
# def displayCityandState(city,state):
#     print(city)
#     print(state)

# #displayCityandState("MH","pune")
# displayCityandState(state = "MH" , city = "Pune")

# # program2 
# # Default arguments 
# def Calculator(x = 50 ,y = 25):
#     print(x+y)
#     print(x-y)
#     print(x*y)
#     print(x/y)
#     print(x%y)
# #Calculator(12,6)
# Calculator()
# Calculator(80,40)


# # program3 
# # variable length arguments 

# # number of arguments know
# def Calculator(a,b,c):
#     print(a+b+c)
# Calculator(11,22,33)

# # program 4
# # number of arguments not known
# def CalculatorB(*args):
#     print(args)
#     print(type(args))
#     sum = 0 
#     for i in args:
#         sum += i
#     return sum

# q1 = CalculatorB(12,3,4,5,6,7,8,7,8,5,6,7,8,8)
# print(q1)

# # program 5
# def CalculatorA(a,b,*args):
#     print(a) # 10
#     print(b) # 44
#     print(args) # (44,55,66,77,88)
# CalculatorA(10,44,55,66,77,88)
# # keyword variable length argument
# # program 6
# def info(**kwargs):
#     print(kwargs)
#     print(type(kwargs))
#     for key ,val in kwargs.items():
#         print(key,val)
# info(firstName="chinmay",lastName="deshpande",age =33,city = "pune")

#program7
# def printT():
#     t = 900
#     print(t) #900
# printT()
# print(t)

# z = 450
# def printZ():
#     z = 900
#     print(z)  # 900
# printZ()
# print(z) # 450

# x = 450
# def printX():
#     print(x)   # 450
# printX()
# print(x) # 450

# def printR():
#     global r 
#     r= 100
#     print(r) # 100
#     r = 700

# printR()
# print(r) # 700

# program 8
# Lamda function
f = lambda x:x*x
print(f(5))

q  = lambda j,y:j+y
print(q(12,13))

q2 = lambda x,y: x if x > y else y
print(q2(22,399))
