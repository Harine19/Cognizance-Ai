import csv
from csv import writer,reader
import re
from collections import defaultdict

text="Python has tools for almost every aspect of scientific computing. The Bank of America uses Python to crunch its financial data and Facebook looks upon the Python library Pandas for its data analysis. While there are many libraries available to perform data analysis in Python, here are a few: NumPy, SciPy, Pandas and Matplotlib."
#finding words with atleast 6 letters
shortword=re.compile(r'\W*\b\w{1,5}\b')
newtext=shortword.sub('',text)

writer = csv.writer(open("output.txt", 'w'), delimiter=';')
with open('about.txt.csv','a') as f: #storing in file
    writer=csv.writer(f)
    writer.writerow([])
    writer.writerow(["Words with atleast 6 letters:"])
    writer.writerow([newtext])

#finding frequently used words
textlist=text.split() 
temp=defaultdict(int)
for i in textlist:
    for j in i.split():
        temp[j] += 1
freq=max(temp,key=temp.get)
with open('about.txt.csv','a') as f: #storing in file
    writer=csv.writer(f)
    writer.writerow(["Most frequently used word:"])
    writer.writerow([str(freq)])
 
#printing file
with open('about.txt.csv','r') as f:
    contents=f.read()
    print(contents)
