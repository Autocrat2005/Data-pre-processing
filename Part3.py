import pandas as pd

dataset = pd.read_csv('loan_small.csv')

cleandata = dataset.dropna() #dropping columns and rows with missing values


DataToScale = cleandata.iloc[: , 2:5]

#This is Z transformation for normalization which has the formula [x - mean(x)]/std_dev(X).


from sklearn.preprocessing import StandardScaler

Scaler_ = StandardScaler()

ss_scaler = Scaler_.fit_transform(DataToScale)

#This is min/max scaler Normalization which has the formula [x - min(x)]/Range.

from sklearn.preprocessing import minmax_scale

minmax_scaler = minmax_scale(DataToScale)
