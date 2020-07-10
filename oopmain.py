class fileLine:
    
    def __init__(self,Line):
        self.Line = Line
    
    def getLineType(self):
        return self.Type

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
onlyNeededLines = []
datafile = open("Example_file.log","r")
for line in datafile.readlines():
    if 'User' in line or 'AcquisitionSystem' in line:
        linesObjArr.append(fileLine(line))
datafile.close()

for i in range(len(linesObjArr)):
    if 'AcquisitionSystem' in linesObjArr[i].Line and 'Acquisition Started' not in linesObjArr[i].Line:
        acqIndex = i
    if 'User' in linesObjArr[i].Line and i!=len(linesObjArr)-1:
        if 'User' in linesObjArr[i+1].Line:
            continue
    else:
        onlyNeededLines.append(linesObjArr[acqIndex])
        onlyNeededLines.append(linesObjArr[i])




