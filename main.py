import csv


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

#Main code to invoke functions
dataset1 = 'dummy.csv'
dataset2 = 'source_data.csv'

datalist = readFile(dataset1)
for x in datalist:
    print(x)
