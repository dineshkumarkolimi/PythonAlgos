'''
Created on 18-Feb-2020

@author: dineshkumars
'''

import os

def checkIfDuplicates_2(listOfElems):
    ''' Check if given list contains any duplicates '''
    flag = False 
    duplicateElements = []   
    for elem in listOfElems:
        if listOfElems.count(elem) > 1:
            duplicateElements.append(elem)
            flag = True
    print duplicateElements
    print duplicateElements.__len__()
    return flag

def checkForMissingEntry(finalData):
    missingEmpID = []
    for root, dirs, files in os.walk("/Users/dineshkumars/comp6521-proj1-tpmms/files/output"):
        for fileName in files:
            # Opening Input data file for reading
            fr = open("/Users/dineshkumars/comp6521-proj1-tpmms/files/output/" + fileName, "r")
            # Reads a line from input matrix
            while(1):    
                read_line = fr.readline()
                if read_line == '':
                    break
                empID = read_line.split("-")[0][0:8]
                if empID not in finalData:
                    missingEmpID.append(empID)
    print "missing employee id's count: " + str(missingEmpID.__len__())
    print missingEmpID
    
def checkForMissingEntryFromMainFiles(finalData):
    missingEmpID = []
    for root, dirs, files in os.walk("/Users/dineshkumars/comp6521-proj1-tpmms/files/input"):
        for fileName in files:
            # Opening Input data file for reading
            fr = open("/Users/dineshkumars/comp6521-proj1-tpmms/files/input/" + fileName, "r")
            # Reads a line from input matrix
            while(1):    
                read_line = fr.readline()
                if read_line == '':
                    break
                empID = read_line.split("-")[0][0:8]
                if empID not in finalData:
                    missingEmpID.append(empID)
    print "missing employee id's count from input files: " + str(missingEmpID.__len__())
    print missingEmpID

def main():
    fpFinal = open("/Users/dineshkumars/comp6521-proj1-tpmms/files/final/mergedOutputFile.txt")
    finalDataSet = []
    while(1):    
        read_line = fpFinal.readline()
        if read_line == '':
            break
        finalDataSet.append(read_line.split("-")[0][0:8])
    if (checkIfDuplicates_2(finalDataSet)):
        print "list contains duplicates"
    else:
        print "duplicates are not there"
    checkForMissingEntry(finalDataSet)
    checkForMissingEntryFromMainFiles(finalDataSet)
        
main()


                




