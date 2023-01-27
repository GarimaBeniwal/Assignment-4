import random
x=1
while x<=10:
    n1=random.randint(0,10)
    n2=random.randint(0,10)
    answer=n1*n2
    
    print(n1,"X",n2,"=",end="")
    response=int(input(""))

    if response==answer:
        print("correct answer")
    else:
        print("Wrong.The correct answer is",answer)
    x=x+1




  


