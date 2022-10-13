# conditional statement 

q = 11
t = 5

print("q is greater") if q > t else print("t is greater")

if(q > t):
    print("q is greater")
else :
    print("t is greater")

# not 

# program 2
# fruits = ["apple","mango","banana"]
# print("apple" in fruits)
# print("mango" not in fruits)

# if("apple" in fruits):
#     print("Apple is available")
# else:
#     print("Apple is not available")

# if("mango" not in fruits):
#     print("Mango is not available")
# else:
#     print("Mango is available")


#program3

# fruits = ["apple","mango","banana"]
# userinput = input('Enter the fruit name: ')
# if(userinput in fruits):
#     print('fruit is available')
# else:
#     print('fruit is not available')


# program 4

m1 = int(input('Enter the maths marks:'))
m2 = int(input('Enter the physics marks: '))
m3 = int(input('Enter the chemistry marks: '))

#print(type(m1))
print((m1+m2+m3)/3)

print("The marks for maths {}".format(m1))
print("The marks for chemistry {}".format(m2))
print("The marks for physics {}".format(m3))

print(float(23))
print(str(34))
print(int('34'))