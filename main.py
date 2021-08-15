while True:
  print("\n1.Calculator")
  print("2.Number Function")
  print("3.Exit")
  #Entering the operation to be performed
  choice1=int(input("\nSelect Choice : "))
  #If the user choses Calculator
  if choice1==1:

    def add(x,y):
      return x+y

    def sub(x,y):
      return x-y

    def multiply(x,y):
      return x*y

    def divide(x,y):
       return x/y

    num1=float(input("Enter the first number: "))
    num2=float(input("Enter the second number: "))
    print("\nOperators : +.Addition")
    print("\t\t\t-.Subraction")
    print("\t\t\t*.Multiplication")
    print("\t\t\t/.Division")
    print("\t\t\t!.Back")
    #Entering operator
    choice2=input("\nEnter Operator : ")
    if choice2=="+":
      print("\nResult : ",add(num1,num2))
    elif choice2=="-":
      print("\nResult : ",sub(num1,num2))
    elif choice2=="*":
      print("\nResult : ",multiply(num1,num2))
    elif choice2=="/":
      print("\nResult : ",divide(num1,num2))
    elif choice2=="!":
      break;
    else:
      print("Invalid output")

  #If the user selects number function
  elif choice1==2:
    num=int(input("Enter a number: "))
    while True:
      print("\n1.Prime or not")
      print("2.Armstrong")
      print("3.Odd or even")
      print("4.Factorial")
      print("5.Back")
      choice3=int(input("Select Function : "))
      if choice3==1:
        if num<=1:
          print(num," is not a prime number")
        else:
          for i in range(2,num):
            if(num%i)==0:
              print(num,"is not a prime number")
              break
          else:
              print(num,"is a prime number")

      elif choice3==2:
        sum=0
        temp=num
        n=len(str(num))
        while temp>0:
          digit=temp%10
          sum+=digit**3
          temp//=10
        if sum == num:
          print(num,"is Armstrong number")
        else:
          print(num,"is not Armstrong number")

      elif choice3==3:
        if (num%2)==0:
          print(num,"is even")
        else:
          print(num,"is odd")

      elif choice3==4:
        result=1
        if num<0:
          print("Invalid")
        else:
          for i in range(num,0,-1):
            result = result*i
          print(f"Factorial of {num} is: {result}")

      elif choice3==5:
        break

      else:
        print("Wrong choice")

  elif choice1==3:
    print("Exiting....")
    break;
  
  else:
    print("Wrong Choice")
