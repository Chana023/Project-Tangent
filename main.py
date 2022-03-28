import csv
from posixpath import split


#Read csv files
def readFile(filename):
    """Read in csv files for mock data provided
    
    Parameters: 
    Filename including extension must be provided as a string

    Returns:
    list: list of the csv data is returned as a list of strings
    
    """
    rawData = []
    with open(filename,newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            rawData.append(row)

    return rawData

def get_unique_user_story(dataList):
    """Takes in a 2 dimensional list and returns the unique values in column 1
    
    Parameters: 
    Two dimensional list

    Returns:
    list: list of unique values in the first column of a two-dimensional list 
    
    """

    uniqueValues = []

    for text in range(1, len(dataList),1):
        itemData = dataList[text][0]
        if itemData not in uniqueValues:
            uniqueValues.append(itemData)
        
    return uniqueValues
        

#Main code to invoke functions
dataset1 = 'dummy.csv'
dataset2 = 'source_data.csv'

datalist = readFile(dataset1)

print(get_unique_user_story(datalist))

