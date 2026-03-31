from sklearn.impute import SimpleImputer
import numpy as np

data=np.array([
    [1,2,np.nan],
    [4,np.nan,6],
    [np.nan,4,5]
])

imputer=SimpleImputer(strategy='constant',fill_value=4)
imputed_data=imputer.fit_transform(data)
print(data)
print(imputed_data)