#Python project to play stone paper and scissor
#first we will take input from user and after that we will write actual code
name1=input("to start the game first enter user 1 name\n")
name2=input("to start the game first enter user 2 name\n")
input1= int(input("choose stone =1 , paper =2 , scissor=3\n"))
input2= int(input("choose stone =1 , paper =2 , scissor=3\n"))
if input1==1:
    if input2==1:
        print("the game is draw")
    elif input2==2:
        print(name2," wins")
    elif input2==3:
        print(name1," wins")
elif input1==2:
    if input2==1:
        print(name1," wins")
    elif input2==2:
        print("the game is draw")
    elif input2==3:
        print(name2," wins")
elif input1==3:
    if input2==1:
        print(name2,"wins")
    elif input2==2:
        print(name1," wins")
    elif input2==3:
        print("game is draw")     
else:
    print("invalid input")           