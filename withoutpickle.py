import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
from imblearn.over_sampling import RandomOverSampler
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np


df=pd.read_csv('oversampled.csv')
df.Sex.replace({'F':0,'I':1,'M':2},inplace=True)


x1=df[['Sex','Length','Diameter','Height','Whole weight','Shucked weight','Viscera weight','Shell weight']].values
y1=df['Rings'].values

xtrain,xtest,ytrain,ytest=train_test_split(x1,y1,random_state=1,test_size=.30,stratify=y1)
def show(xtest):
    Random=RandomForestClassifier(n_estimators= 600,
     min_samples_split= 2,
     min_samples_leaf= 1,
     max_features= 'sqrt',
     max_depth= 120,
     criterion= 'entropy'
    )
    Random.fit(xtrain,ytrain)
    return Random.predict(xtest)


