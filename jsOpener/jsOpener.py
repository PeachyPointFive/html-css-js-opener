import os
from pathlib import Path
downloads = str(os.path.join(Path.home(), "Downloads"))

path = input("Enter folder name: ")

if not os.path.exists(path):
    os.mkdir(downloads + "/" + path)

    print("Folder %s has been created!" % path)
    
else:
    print("Folder %s already exists" % path)


os.startfile(downloads + "/" + path)



fileName = downloads + "/" + path + "/index.html"
fileName2 = downloads + "/" + path + "/styles.css"
fileName3 = downloads + "/" + path + "/script.js"
    
fp = open(fileName, 'a')
skel = open("txtFiles/htmlSkeleton.txt", "r").read()
fp.write(skel)



fp = open(fileName2, 'a')
cssBase = open("txtFiles/cssBase.txt", "r").read()
fp.write(cssBase)
fp = open(fileName3, 'a')
jsBase = open("txtFiles/jsBase.txt", "r").read()
fp.write(jsBase)

fp.close()
