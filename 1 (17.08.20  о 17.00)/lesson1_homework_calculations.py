a = input("Enter the first number: ")
b = input("Enter the second number: ")

try:
    a = int(a)
    b = int(b)
    print("Addition: ",(a + b))
    #print("Addition: "+str(a + b))
    print("Subtractiona: ",(a-b))
    #print("Subtractiona: "+str(a-b))
    print("Multiplication: ",(a*b))
    #print("Multiplication: "+str(a*b))
    print("Division: ",(a/b))
    #print("Division: "+str(a/b))
    print("Degree: ",(a**b))
    #print("Degree: ",str(a**b))
except ValueError:
    a = input("Maybe, that's not an number. Re-Enter the first number: ")
    b = input("Re-Enter the second number: ")
    a = int(a)
    b = int(b)
    print("Addition: ", (a + b))
    # print("Addition: "+str(a + b))
    print("Subtractiona: ", (a - b))
    # print("Subtractiona: "+str(a-b))
    print("Multiplication: ", (a * b))
    # print("Multiplication: "+str(a*b))
    print("Division: ", (a / b))
    # print("Division: "+str(a/b))
    print("Degree: ", (a ** b))
    # print("Degree: ",str(a**b))