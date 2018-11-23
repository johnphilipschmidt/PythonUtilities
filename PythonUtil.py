# JP Schmidt Nov 2018
# Utility for Python features. Similar to Java/PHP util for me so the naming convention and implementaiton can be the same.


class PythonUtil:
    def __init__(self,name):
        self.name=name
        mydict={
            "name":"Utility",
            "fileDirectory":"/tmp/"
        }

    def fileOpenForRead(self,fileName):
        fh = open(self.mydict("fileDirectory")+fileName, "r")
        return fh

    def fileRead(self,fileHandle):
        fileHandle.read()

    def fileReadline(self,fileHandle):
        fileHandle.realine()

    def fileOpenForWrite(self,fileName):
        fh = open(self.mydict("fileDirectory")+fileName, "rw")
        return fh

    def fileWriteText(self,fileHandle,inputText):
        fileHandle.write(inputText)
        return

    def fileOpenForAppend(self,fileName):
        fh = open(self.mydict("fileDirectory")+fileName, "a")
        return fh

    def fileClose(self,fileName):
        fh = open(self.mydict("fileDirectory")+fileName, "a")
        return fh

    def featuresList(self):
        print "Main Utility Features"
        print "     1) openFileForRead"
        print "     2) openFileForWrite"
        print "     3) openFileForAppend"
        print "     4) closeFile"
        return ""

#implmentation
util=PythonUtil("util")
util.featuresList()

