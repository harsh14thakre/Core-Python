def leapyear(n):
    if(n%4==0 and n%100!=0):
       print("This is a leap year")
    elif(n%400==0 and n%100!=0):
       print("This is a leap year")   
    else:
       print("This is not  leap year")

n=int(input("Enter your year"))
leapyear(n)       




