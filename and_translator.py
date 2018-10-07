#!/usr/bin/python3
from xml.dom import minidom
import sys, subprocess, getopt

inputFile = ''
outputFile = ''
toFromLangs = ''

def translate(value):
    # print("Translating " + value)
    args = ['vertaler', toFromLangs, value]
    translated = subprocess.check_output(args)
    return translated.decode('utf-8').rstrip()

def writeToFile(data):
    f =  open(outputFile, "w")
    f.write(data)
    f.close()
    
def splitAndTranslate(xmlStringsList):
    singleLineString = ""
    for item in xmlStringsList:
        singleLineString += item.firstChild.nodeValue + "\n"
     
    singleLineString = translate(singleLineString)
    
    retrievedList = singleLineString.split("\n")

    print("\nRetrieved list length:", len(retrievedList))

    for index in range(len(xmlStringsList)):
        xmlStringsList[index].firstChild.nodeValue = retrievedList[index]

    return xmlStringsList
    
def handleParameters(argv):
    global inputFile
    global outputFile
    global toFromLangs

    try:
        opts, args = getopt.getopt(argv,"hi:o:l:",["ifile=","ofile=","lang="])
    except getopt.GetoptError:
        displayHelp()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            displayHelp()
            sys.exit()
        elif opt in ("-i", "--ifile"):
            inputFile = arg
        elif opt in ("-o", "--ofile"):
            outputFile = arg
        elif opt in ("-l", "--lang"):
            toFromLangs = arg
        else:
            displayHelp()

    if inputFile == '' or outputFile == '' or toFromLangs == '':
        displayHelp()
        sys.exit()

    print("\nSource File: " + inputFile)
    print("Translate File: " + outputFile)
    

def displayHelp():
    print('Usage:')
    print('test.py -i <inputfile> -o <outputfile> -l {srcLang:translateLang}')

def init():

    handleParameters(sys.argv[1:])

    xmldoc = minidom.parse(inputFile)
    translateddoc = xmldoc
    itemList = xmldoc.getElementsByTagName('string')
    numofstrings = print("\nNumber of strings to translate: ", len(itemList))

    
    # Split content into seperate chunks
    charCount = 0
    chunkCount = 0
    lastIndex = 0
    chunks = {}
    for index in range(len(itemList)):
        item = itemList[index]
        charCount += len(item.firstChild.nodeValue)
        if (charCount >= 3000 or index == len(itemList)-1):
            # print("Chunks length ")
            # print(len(chunks))
            # chunks[chunkCount] = list(range(lastIndex, index-1))
            chunks[chunkCount] = itemList[lastIndex:index]
            chunkCount += 1
            lastIndex = index
            charCount = 0

    print("Chunk size ", len(chunks))
    
    for index in range(len(chunks)):
        splitAndTranslate(chunks[index])

    # itemList = splitAndTranslate(itemList)

    writeToFile(xmldoc.toxml())
    print("\nDone")

init()