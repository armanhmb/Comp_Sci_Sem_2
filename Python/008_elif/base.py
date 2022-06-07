x = int(input('please enter a number'))
y = str(input("Please enter an operator"))
z = int(input("please enter another number"))
Op1=("+")
Op2=("-")
Op3=("*")
Op4=("/")
if y == Op1:
    print (x+z)
elif y == Op2:
    print (x-z)
elif y == Op3:
    print (x*z)
elif y == Op4: 
    print (x/z)
    