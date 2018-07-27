'''
Creator: Juan Sebastian Rojas
Developed with Python Version 3.7.0
Modules Requirements: numpy and liac-arff
This module enables to load a WEKA ARFF file into Python using numpy arrays
and liac-arff module.
'''
import arff
import numpy as np

#This is the recommended way to load any data file since the with statement
#closes the data handler on its own. In the open function 'r+' is the mode to
#read and write the file.
def loadArffFile(filePath):
    with open(filePath, 'r+') as fh:
        dataset = arff.load(fh)
        if(dataset != None):
            print('ARFF Loaded!')
            return dataset
        else:
            print('ARFF not loaded')

#This function obtains the attributes from the dictionary created by liac-arff
#and prints them on console.
def showDatasetAttributes(dataset):
    #For loop to obtain the names of the attributes
    attributes = [] #New list to save the attribute names
    for key,value in dataset['attributes']:
        attributes.append(key)
    print(attributes)

#This function obtains the instances from the dictionary created by liac-arff
#and returns them in a numpy array.
def setDataInArray(dataset):
    arrayData = np.array(dataset['data'])
    return arrayData
