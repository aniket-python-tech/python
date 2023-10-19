blank_distionary={}
while True:
 key=input("enter the key ")
 value=input("enter the value")
 blank_distionary[key]=value
 stop_data=input("do you want to continue or not y/n:")
 if stop_data!="y":
     break
print(blank_distionary)
