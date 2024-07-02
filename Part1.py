import pandas as pd

dataset = pd.read_csv('loan_small.csv')  # we're reading csv file using pandas here

subset = dataset[['LoanAmount', 'ApplicantIncome']] #This will show only 2 columns from the dataset creating a new variable

subset = dataset[['LoanAmount', 'ApplicantIncome']][0:3] #This will show the first 3 records 0 meaning from the first index and 3 meaning either consider it till n-1th record or total no of records

#to read txt files in our case seprated by a 't'ab space 
import pandas as pd
datasettxt = pd.read_csv('loan_small_tsv.txt', sep= '\t')

#functions of pandas
#https://pandas.pydata.org/docs/reference/general_functions.html

#shape - get rowsxcolumns info
dataset.shape

#to find number of missing values
dataset.isnull().sum(axis=0)

#replacing missing values in data.
import pandas as pd

dataset = pd.read_csv('loan_small.csv') 

dc = dataset.copy()

missing1 = ['Gender', 'Area', 'Loan_Status']

dc[missing1] = dc[missing1].fillna(dc.mode().iloc[0])


missing = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount']

dc[missing] = dc[missing].fillna(dc[missing].median())

