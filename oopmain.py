class fileLine:
    
    def __init__(self,Line,Index):
        self.Line = Line
    	self.Index = Index
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

#linesObjArr = []
onlyNeededLines = []
AcqStartedLines = []

datafile = open("Example_file.log","r")
lines = datafile.readlines()
datafile.close()

for i in range(len(lines)):
	if 'AcquisitionSystem' in lines[i] and 'Acquisition Started' not in lines[i]:
		AcqSysIndex = i
		continue
	if 'Acquisition Started' in lines[i]:
		AcqStartedLines.append(fileLine(lines[i],i))
		continue
	if 'User' in lines[i]:
		if 'User' in lines[i+1]:
			continue
		else:
			onlyNeededLines.append(fileline(lines[AcqSysIndex],AcqSysIndex))
			onlyNeededLines.append(fileline(lines[i],i))

			if 'Acquisition Started' in lines[i+1]:
				AcqStartedLines.append(fileLine(lines[i+1],i+1))
				onlyNeededLines.append(fileline(lines[i+2],i+2))
			else:
				onlyNeededLines.append(fileline(lines[i+1],i+1))






#for line in datafile.readlines():
    #if 'User' in line or 'AcquisitionSystem' in line:
        #linesObjArr.append(fileLine(line))


#for i in range(len(linesObjArr)):
    #if 'AcquisitionSystem' in linesObjArr[i].Line and 'Acquisition Started' not in linesObjArr[i].Line:
        #acqIndex = i
    #if 'User' in linesObjArr[i].Line and i!=len(linesObjArr)-1:
        #if 'User' in linesObjArr[i+1].Line:
            #continue
    #else:
        #onlyNeededLines.append(linesObjArr[acqIndex])
        #onlyNeededLines.append(linesObjArr[i])




