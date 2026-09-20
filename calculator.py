while True:
   
   
   
    num1=int(input("enter a number:"))
    num2=int(input("enter second number:"))
    operator=input("choose operator:{+/-/*//}")
    if operator not in ["+","-","*","/"]:
            print("invalid operator")
            break

   
    if operator=='+':
                print(num1+num2)
    elif operator=='-':
                    print(num1-num2)        
    elif operator=='*':
                    print(num1*num2)

    else:
                    print(num1/num2)
            
            
            

        



    