import numpy as np     
foodli=[]
while 1:
    ch=int(input("1 - Enter data \n2 - Exit: "))
    if ch==1:
        n=int(input("\nEnter the number of rows :"))
        for i in range(n):
            name=input("Enter Name: ")
            price=input("Enter Price: ")
            rating=int(input("Enter Rating[1- Worst, 5-Best]: "))
            l=(name,price,rating)
            foodli.append(l)
        data_type=[('Name','S15'), ('Price',float), ('Rating',int)]
        food=np.array(foodli,dtype=data_type)
        print("Sorted from lowest to highest rating")
        print(np.sort(food, order='Rating'))
        print("")
    if ch==2:
        break
