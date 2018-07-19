#!/usr/bin/python3
from xml.dom import minidom
import subprocess

xmldoc = minidom.parse('strings.xml')
itemList = xmldoc.getElementsByTagName('string')
numofstrings = print(len(itemList))
f =  open("newfile.xml", "w")

# print(itemList[0].firstChild.nodeValue)
# translated.decode('UTF-8')

for item in itemList:
    print("Translating " + item.firstChild.nodeValue)
    args = ['vertaler', 'en:hi', item.firstChild.nodeValue]
    translated = subprocess.check_output(args)
    # translated = translated.strip()
    item.firstChild.nodeValue = translated.decode('utf-8').rstrip()
    # item.firstChild.nodeValue = bytes(translated, 'utf-8').decode('utf-8', 'ignore')
    print("Done " + item.firstChild.nodeValue)

f.write(xmldoc.toxml())
f.close()

    