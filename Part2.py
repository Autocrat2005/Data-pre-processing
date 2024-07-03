import pandas as pd

dataset = pd.read_csv('loan_small.csv')

#to find number of missing values

dataset.isnull().sum(axis=0)


#Encoding labels for string(alphabetical) based categories such as gender where we'll replace them with number so we can use them in formulas, e.g. we can assign Male = 0 and Female = 1

#using pandas

dc.dtypes

dc[missing1] = dc[missing1].astype('category')


for missing1 in missing1 :
    dc[missing1] = dc[missing1].cat.codes #this replaces our string codes into int so that we have a int based data.

#Hot encoding for data. this is to make sure we dont do some stupid mathematical operations for categories such as if male is assigned 1 and female 0. according to operations 1 > 0 but we believe in equality so we do Hot encoding.
#dropping columns not necessary for predictions.

df2 = dataset.drop(['Loan_ID'], axis=1)

#creating dummy variables
df2 = pd.get_dummies(df2)
