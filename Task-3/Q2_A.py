#Q2.A) Make all values <15 to 15, >45 to 45
import numpy as np

#getting cutoff as 15 and 45 as per question
x=101
y=101
while (x and y >100):
    x=int(input("Enter your cutoff minumum: "))
    y=int(input("Enter your cutoff maximum: "))

#making the array and clipping it 
np.random.seed(100) 
a=np.random.uniform(1,50,20)
a=np.clip(a,x,y)

#printing array elements
a=str(a).replace('[', '').replace(']', '')
a=a.split()
for i in a:
    print(i)

