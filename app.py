import pandas as pd
from sklearn import preprocessing



train=pd.read_csv('train.csv')
test=pd.read_csv('test.csv')


def clean(data):
    cols=["SibSp","Parch","Age","Fare"]
    for col in cols:
        data[col]=data[col].fillna(data[col].mean(),inplace=True)
    data.Embarked.fillna("U",inplace=True)
    return data

# clean(train)
# clean(test)


le=preprocessing.LabelEncoder()

cols=["Sex","Embarked"]




