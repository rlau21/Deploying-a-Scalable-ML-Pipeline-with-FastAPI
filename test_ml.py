import pytest
# TODO: add necessary import

# TODO: implement the first test. Change the function name and input as needed
def test_rowcounts():
    """
    confirm the data has more than 1000 rows after 30% slice
    """
    # Your code here
    data_path = './data/census.csv'
    data = pd.read_csv(data_path)
    train, test = train_test_split(data, test_size = .3)
    assert len(test) >= 1000
    pass


# TODO: implement the second test. Change the function name and input as needed
def test_two():
    """
    # add description for the second test
    """
    # Your code here
    pass


# TODO: implement the third test. Change the function name and input as needed
def test_three():
    """
    # add description for the third test
    """
    # Your code here
    pass
