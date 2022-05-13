import csv
row=[1,'Aaa',3.5,'Maths',2,'Bbb',4.2,'Physics',3,'Ccc',7.62,'Chemistry'
     ,4,'Ddd',9.55,'Biology',5,'Eee',4.0,'Social',6,'Fff',7.6,'English'
     ,7,'Ggg',3.111,'Maths',8,'Hhh',9.99,'Physics',9,'Iii',1.23,'Civics']
row2=[]
with open('onelinefile.txt.csv','w') as file: #writing the content into file
    writer=csv.writer(file)
    writer.writerow(row)
with open('onelinefile.txt.csv','r') as file: #reading the content from file
    reader=csv.reader(file)
    for i in reader:
        for j in range(0,len(i),4):
            with open('onelinefile2.txt.csv','w') as file2: #writing the content into file2
                writer=csv.writer(file2)
                row2=row[j],row[j+1],row[j+2],row[j+3]
                writer.writerow(row2)
            with open('onelinefile2.txt.csv','r') as file2: #reading the content from file2
                reader=csv.reader(file2)
                for i in reader:
                    print(i)

        
            
            
            
   
    
