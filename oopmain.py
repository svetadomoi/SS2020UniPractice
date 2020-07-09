class fileLine:
    
    def __init__(self,Line):
        self.Line = Line
    
    def getRunNumber(self):
        return self.RunNumber
    
    def getTimeStampLocal(self):
        return self.TimeStampLocal
    
    def getEventSource(self):
        return self.EventSource
    
    def getFileNumber(self):
        return self.RunNumber
    
    def getEventMessage(self):
        return self.RunNumber

    def infoOut(self):
        print(self.Line)

linesObjArr = []
datafile = open("Example_file.log","r")
for line in datafile.readlines():
    if 'User' in line or 'AcquisitionSystem' in line:
        linesObjArr.append(fileLine(line))

linesObjArr[0].infoOut()
