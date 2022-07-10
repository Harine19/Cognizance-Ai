#Q2.B) Split a text column into 2 columns using pandas
import pandas as pd

#input
df=pd.DataFrame({'STD':[33,44,40,80],
                 'City':['Mumbai  Maharashtra','Chennai  TamilNadu','Vishakapatnam  Telangana','Bangalore  Karnataka']})
print("Given dataframe is: \n",df)

#splitting
df[['City','State']]=df.City.apply(lambda x: pd.Series(str(x).split("  ")))
print("\nDataframe after splitting is: \n",df)

