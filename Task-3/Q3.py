import numpy as np 
import pandas as pd 
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('../input/engineering-graduate-salary-prediction/Engineering_graduate_salary.csv')
df.head()

#getting rid of redundant columns
df = df.drop(['ID', 'DOB', 'CollegeID', '12graduation' ,'GraduationYear','10board', '12board' , 'CollegeState','CollegeCityID', 'CollegeCityTier',],axis = 1)
df.head()

#checking duplicates, cleaning data
df.duplicated().sum()

#grouping single datas into 'others'
specialization = df.Specialization.value_counts() #Store the values # in specialization
lessthan10 = specialization[specialization<=10]
lessthan10
def correctSpecialization(val):
    if val in lessthan10:
        return 'Others'
    else:
        return val
df['Specialization'] = df['Specialization'].apply(correctSpecialization)
df['Specialization'].value_counts()

#dropping insignificant data and outliners after checking in matplotlib
df = df[(df['collegeGPA'] > 40)]
df = df.replace(-1,np.nan)
cols_with_nan = [col for col in df.columns if df.isna().sum()[col]>0]
for col in cols_with_nan:
    df[col] = df[col].fillna(df[col].mean())

from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df.Gender = le.fit_transform(df.Gender)
df.Degree = le.fit_transform(df.Degree)
df.Specialization = le.fit_transform(df.Specialization)

#final
df.head()



