print("Welcome to the Health Management Portal\n")
def getdate():
    import datetime
    return datetime.datetime.now()
getdate()
a=int(input("Press 1 for Harry 2 for Rohan and 3 for Parag"))
b=int(input("Enter 1 for log and 2 for retrieve"))
c=int(input("Type 1 for diet and 2 for exercise"))

if a==1 and b==1 and c==1:
    with open("harry-diet.txt","a") as f1:
        print("Enter the diet")
        x= input()
        f1.write("["+str(getdate())+"]"+" "+x+"\n")
elif a==2 and b==1 and c==1:
    with open("rohan-diet.txt","a") as f2:
        print("Enter the diet")
        y= input()
        f2.write("["+str(getdate())+"]"+" "+y+"\n")
elif a==3 and b==1 and c==1:
    with open("Parag-diet.txt","a") as f3:
        print("Enter the diet")
        z= input()
        f3.write("["+str(getdate())+"]"+" "+z+"\n")
elif a==1 and b==1 and c==2:
    with open("harry-exer.txt","a") as f4:
        print("Enter the exercise")
        k= input()
        f4.write("["+str(getdate())+"]"+" "+k+"\n")
elif a==2 and b==1 and c==2:
    with open("rohan-exer.txt","a") as f5:
        print("Enter the exercise")
        l= input()
        f5.write("["+str(getdate())+"]"+" "+l+"\n")
elif a==3 and b==1 and c==2:
    with open("parag-exer.txt","a") as f6:
        print("Enter the exercise")
        m= input()
        f6.write("["+str(getdate())+"]"+" "+m+"\n")
elif a==1 and b==2 and c==1:
    with open("harry-diet.txt") as f7:
        print(f7.read())
elif a==2 and b==2 and c==1:
    with open("rohan-diet.txt") as f8:
        print(f8.read())
elif a==3 and b==2 and c==1:
    with open("Parag-diet.txt") as f9:
        print(f9.read())
elif a==1 and b==2 and c==2:
    with open("harry-exer.txt") as f10:
        print(f10.read())
elif a==2 and b==2 and c==2:
    with open("rohan-exer.txt") as f11:
        print(f11.read())
elif a==3 and b==2 and c==2:
    with open("parag-exer.txt") as f12:
        print(f12.read())
else:
    print("Invalid Input!!")


