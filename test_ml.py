import pytest
# TODO: add necessary import
import pandas as pd
from sklearn.model_selection import train_test_split
from ml.model import train_model
from sklearn.ensemble import RandomForestClassifier
import os

# TODO: implement the first test. Change the function name and input as needed
def test_rowcounts():
    """
    confirm the census data has more than 1000 rows after 30% slice
    """
    # Your code here
    data_path = './data/census.csv' #census path
    data = pd.read_csv(data_path) #read the file
    train, test = train_test_split(data, test_size = .3) #split into 30%
    assert len(test) >= 1000 #check rowcounts of test
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_featurecheck():
    """
    ensure that all the features are present
    """
    data_path = './data/census.csv' #census path
    data = pd.read_csv(data_path) #read the file

    features = {
        'age',
        'workclass',
        'fnlgt',
        'education',
        'education-num',
        'marital-status',
        'occupation',
        'relationship',
        'race',
        'sex',
        'capital-gain',
        'capital-loss',
        'hours-per-week',
        'native-country',
        'salary'
    }
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_censuspopulated():
    """
    validating that the census data is not blank or empyt
    """
    data_path = './data/census.csv' #census path
    data = pd.read_csv(data_path) #read the file
    assert not data.empty
    assert data.shape[0] > 0 # more than 0 rows
    pass
