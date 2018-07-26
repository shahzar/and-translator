#!/usr/bin/python3
from xml.dom import minidom
import subprocess

def translate(value):
    print("Translating " + value)
    args = ['vertaler', 'en:hi', value]
    translated = subprocess.check_output(args)
    return translated.decode('utf-8').rstrip()

def writeToFile(data):
    f =  open("newfile.xml", "w")
    f.write(data)
    f.close()
    
def splitAndTranslate(xmlStringsList):
    singleLineString = ""
    for item in xmlStringsList:
        singleLineString += item.firstChild.nodeValue + "\n"
     
    singleLineString = translate(singleLineString)
    
    retrievedList = singleLineString.split("\n")

    print("Retrieved list length:")
    print(len(retrievedList))

    for index in range(len(xmlStringsList)):
        xmlStringsList[index].firstChild.nodeValue = retrievedList[index]

    return xmlStringsList
    
    
def initTest():
    xmldoc = minidom.parse('strings.xml')
    translateddoc = xmldoc
    itemList = xmldoc.getElementsByTagName('string')
    numofstrings = print(len(itemList))

    
    # Split logic
    charCount = 0
    chunkCount = 0
    lastIndex = 0
    chunks = {}
    for index in range(len(itemList)):
        item = itemList[index]
        charCount += len(item.firstChild.nodeValue)
        if (charCount >= 3000 or index == len(itemList)-1):
            print("Chunks length ")
            print(len(chunks))
            # chunks[chunkCount] = list(range(lastIndex, index-1))
            chunks[chunkCount] = itemList[lastIndex:index]
            chunkCount += 1
            lastIndex = index
            charCount = 0

    print("Size ")
    print(chunks)
    

    for index in range(len(chunks)):
        splitAndTranslate(chunks[index])

    # itemList = splitAndTranslate(itemList)

    print("Done")
    writeToFile(xmldoc.toxml())
    

def init():
    xmldoc = minidom.parse('strings.xml')
    translateddoc = xmldoc
    itemList = xmldoc.getElementsByTagName('string')
    numofstrings = print(len(itemList))

    
    for item in itemList:
        translated = translate(item.firstChild.nodeValue)
        item.firstChild.nodeValue = translated
        print("Done " + item.firstChild.nodeValue)

    writeToFile(xmldoc.toxml())


def initOld():
    xmldoc = minidom.parse('strings.xml')
    translateddoc = xmldoc
    itemList = xmldoc.getElementsByTagName('string')
    numofstrings = print(len(itemList))

    # print(itemList[0].firstChild.nodeValue)
    # translated.decode('UTF-8')

    for item in itemList:
        
        # translated = translated.strip()
        translated = translate(item.firstChild.nodeValue)
        item.firstChild.nodeValue = translated
        # item.firstChild.nodeValue = bytes(translated, 'utf-8').decode('utf-8', 'ignore')
        print("Done " + item.firstChild.nodeValue)

    writeToFile(xmldoc.toxml())


initTest()