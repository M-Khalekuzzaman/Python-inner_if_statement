num1 = float(input(("Enter your first number :")))
num2 = float(input(("Enter your second number :")))
num3 = float(input(("Enter your third number :")))
'''
if num1>num2 and num1>num3 :
    print("Large number is :",num1)
elif num2>num1 and num2>num3 :
    print("Large number is : ",num2)
elif num3>num1 and num3>num2 :
    print("large number is : ",num3)
else:
    print("Your number is not correct")
    
if num1>num2 :
    if num1>num3 :
        print("Large number is : ",num1)
    else:
        print("Lower number is : ",num3)
'''
#Using ternary operator
max = num1 if num1>num2 else num2
print(max)


