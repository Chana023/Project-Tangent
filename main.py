from audioop import reverse
from binascii import Incomplete
import csv
from distutils.command.clean import clean
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
    list: list of unique values in the first column of a given two-dimensional list 
    
    """

    uniqueValues = []

    for text in range(0, len(dataList),1):
        itemData = dataList[text][0]
        if itemData not in uniqueValues:
            uniqueValues.append(itemData)

    uniqueValues.sort(key=lambda x: int(x[5:]))
        
    return uniqueValues

def itemCompletionStatus(dataList):
    """Takes in a 2 dimensional list and returns whether every task for a specific item was completed
    
    Parameters: 
    Two dimensional list

    Returns:
    list: yes and no response in each element of the list, the response is sorted based on the item number
    
    """
    uniqueItems = get_unique_user_story(dataList)
    #Ignore heading list
    ResponseList = []
    tempList = []

    for x in uniqueItems:
        for itemIndex in range(0,len(dataList),1):
            if x == dataList[itemIndex][0]:
                if dataList[itemIndex][2] == 'Yes':
                    tempList.append(True)
                    #print(x + ' ' + dataList[itemIndex][0] + ' ' + dataList[itemIndex][2])
                elif dataList[itemIndex][2] == 'No':
                    #print(x + ' ' + dataList[itemIndex][0] + ' ' + dataList[itemIndex][2])
                    tempList.append(False)
                else:
                    tempList.append('BadData')
        #Check if all values in templist are 'True' then append Yes to ResponseList else return 'No'
        if all(tempList) == True:
            ResponseList.append('Yes')
        else:
            ResponseList.append('No')
         #clear all values in the list   
        tempList.clear()
        
    return ResponseList 


def removeDuplicatesWithYes(dataList):
    """Takes in a 2 dimensional list and removes duplicates values
    
    Parameters: 
    Two dimensional list

    Returns:
    list: Removes duplicates and if the item has a yes and no only the no index is returned to indicate 
    the item is incomplete.
    
    """

    dataList.pop(0)
    
    #Remove duplicates besides yes and no extras
    tempList = []
    for x in dataList:
        if x not in tempList:
            tempList.append(x)
    
    dataList = tempList
    tempList = []
    indexToBeDeleted = []

    #Remove yes response where there exists a no already
    for y in dataList:
        for z in dataList:
            if y[0] == z[0] and y[1] == z[1] and y[2] != z[2]:
                if z[2] == 'Yes':
                    indexToBeDeleted.append(z)

    for index in indexToBeDeleted:
        dataList.remove(index)

    return dataList

def taskChecker(dataList, bool):
    uniqueItems = get_unique_user_story(dataList)
    completeCounter = 0
    incompleteCounter = 0
    completeList = []
    inCompleteList = []

    for item in uniqueItems:
        for x in dataList:
            if item == x[0] and x[2] == 'Yes':
                completeCounter += 1
            elif item == x[0] and x[2] == 'No':
                incompleteCounter += 1
                pass
        
        completeList.append(completeCounter)
        inCompleteList.append(incompleteCounter)
        completeCounter = 0
        incompleteCounter = 0

    if bool == True:
        return completeList
    elif bool == False:
        return inCompleteList

def maxTaskIDCompleted(dataList):
    uniqueItems = get_unique_user_story(dataList)
    listOfLargestTaskCompleted = []
    largestTask = 0

    for item in uniqueItems:
        for task in dataList:
            if item == task[0]:
                if int(largestTask) < int(task[1]) and task[2] == 'Yes':
                    largestTask = task[1]

        listOfLargestTaskCompleted.append(largestTask)
        largestTask = 0

    return listOfLargestTaskCompleted
    
#Main code to invoke functions
dataset1 = 'dummy.csv'
dataset2 = 'source_data.csv'        #Main test data
dataset3 = 'sample-creation-3.csv'

datalist = readFile(dataset2)
cleanList = removeDuplicatesWithYes(datalist)



print(str(get_unique_user_story(cleanList)))
print(str(itemCompletionStatus(cleanList)))
print(taskChecker(cleanList, True))
print(taskChecker(cleanList, False))
print(maxTaskIDCompleted(cleanList))
