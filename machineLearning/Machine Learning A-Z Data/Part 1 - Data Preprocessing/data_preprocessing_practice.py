# -*- coding: utf-8 -*-

# Importing the libararies
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('Data.csv')

X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 3].values
# iloc [모든 row, 모든 칼럼]
# [:, :-1] 는 모든 라인을 선택할꺼고, :-1 하면 마지막 줄 빼고 선택하라는 뜻

# 오래된 방법 이제는 deprecated 됨
#from sklearn.preprocessing import Imputer
#imputer = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
#imputer = imputer.fit(X[:,1:3])
#X[:, 1:3] = imputer.transform(X[:, 1:3])

# 위 방법은 오래된 방법이고, 이제 새로운 방법이 생김
from sklearn.impute import SimpleImputer
missingvalues = SimpleImputer(missing_values = np.nan, strategy = 'mean', verbose = 0)
missingvalues = missingvalues.fit(X[:, 1:3])
X[:, 1:3]=missingvalues.transform(X[:, 1:3])

# Encoding categorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
labelencoder_X.fit_transform(X[:, 0])
# 실행 결과
# array([0, 2, 1, 2, 1, 0, 2, 0, 1, 0])
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])
# 어떤 줄을 기준으로 분류할 지 정해준다.
onehotencoder = OneHotEncoder(categorical_features = [0])
# 데이터 형태로 만들어준다.
X = onehotencoder.fit_transform(X).toarray()


labelencoder_y = LabelEncoder()
y = labelencoder_y.fit_transform(y)



# Splitting the dataset into the Training set and Test set
# 테스트 만들기
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)

# Feature Scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_test)






