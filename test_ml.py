import pytest
# TODO: add necessary import

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
def test_rfclass():
    """
    confirm the model is the RF classifier
    """
    fake_x = [[1,2,3], [4,5,6]] #fake values for testing
    fake_y = ['low', 'high']
    model = train_model(fake_x, fake_y) #pull the train model
    assert type(model) == type(RandomForestClassifier) #assert the type is RFC
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
