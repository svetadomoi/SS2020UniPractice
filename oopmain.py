class fileLine:
	def __init__(self,Line,Index,EventSource):
		self.Line = Line
		self.Index = Index
		self.EventSource = EventSource
		self.scndsTime = 0
	def getRunNumber(self):
		self.RunNumber = self.Line[self.Line.find('\t',self.Line.find('run'))+1:self.Line.find('\t',self.Line.find('\t',self.Line.find('run'))+1)]
    
	def getTimeStampLocal(self):
		ColonIndex = self.Line.find(':')
		i = ColonIndex
		while self.Line[i] != '\t':
			i-=1
		self.TimeStampLocal = self.Line[i+1:ColonIndex+3]
		self.scndsTime = 3600*int(self.TimeStampLocal[self.TimeStampLocal.find(' ')+1:self.TimeStampLocal.find(':')])+60*int(self.TimeStampLocal[self.TimeStampLocal.find(':')+1:])
	def getFileNumber(self):
		self.FileNumber = self.Line[self.Line.find('\t',self.Line.find(self.EventSource))+1:self.Line.find('\t',self.Line.find('\t',self.Line.find(self.EventSource))+1)]

	def getEventMessage(self):
		if self.EventSource == 'AcquisitionSystem':
			pointIndex = self.Line.find('.sgy')
			i = pointIndex
			while self.Line[i] != '\t':
				i-=1
			self.EventMessage = self.Line[i+1:pointIndex+4]
		else:
			slashIndex = self.Line.find('/min')
			i = slashIndex
			while self.Line[i] != '\t':
				i-=1
			self.EventMessage = self.Line[i+1:slashIndex+4]

	def getTimeStampRelative(self):
		for i in range(len(AcqStartedLines)-1):
			if self.Index > AcqStartedLines[i].Index and self.Index < AcqStartedLines[i+1].Index:
				self.TimeStampRelative = self.scndsTime - AcqStartedLines[i].scndsTime
	def writeInfoToFile(self,filename):
		self.getRunNumber()
		self.getTimeStampLocal()
		self.getFileNumber()
		self.getEventMessage()
		self.getTimeStampRelative()
		filename.write(str(self.TimeStampRelative)+self.RunNumber+self.TimeStampLocal+self.EventSource+self.FileNumber+self.EventMessage+'\n')

onlyNeededLines = []
AcqStartedLines = []

datafile = open("Example_file.log","r")
lines = datafile.readlines()
datafile.close()
j = 0
for i in range(len(lines)):
	if 'AcquisitionSystem' in lines[i] and 'Acquisition Started' not in lines[i]:
		AcqSysIndex = i
		continue
	if 'Acquisition Started' in lines[i]:
		AcqStartedLines.append(fileLine(lines[i],i,'Acquisition Started'))
		AcqStartedLines[j].getTimeStampLocal()
		j+=1
		continue
	if 'User' in lines[i]:
		if 'User' in lines[i+1]:
			continue
		else:
			onlyNeededLines.append(fileLine(lines[AcqSysIndex],AcqSysIndex,'AcquisitionSystem'))
			onlyNeededLines.append(fileLine(lines[i],i,'User'))
			if 'Acquisition Started' in lines[i+1]:
				onlyNeededLines.append(fileLine(lines[i+2],i+2,'AcquisitionSystem'))
			else:
				onlyNeededLines.append(fileLine(lines[i+1],i+1,'AcquisitionSystem'))
AcqStartedLines.insert(0,fileLine(AcqStartedLines[0].Line,AcqStartedLines[0].Index,AcqStartedLines[0].EventSource))
AcqStartedLines[0].Index = -1
AcqStartedLines.append(fileLine(AcqStartedLines[len(AcqStartedLines)-1].Line,AcqStartedLines[len(AcqStartedLines)-1].Index,AcqStartedLines[len(AcqStartedLines)-1].EventSource))
AcqStartedLines[len(AcqStartedLines)-1].Index = len(lines)

fileForOut = open('oop_result.txt','w')
for i in range(len(onlyNeededLines)):
	onlyNeededLines[i].writeInfoToFile(fileForOut)
fileForOut.close()