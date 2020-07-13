class fileLine:
	def __init__(self,Line,Index,EventSource):
		self.Line = Line
		self.Index = Index
		self.EventSource = EventSource
	def getRunNumber(self):
		self.RunNumber = self.Line[self.Line.find('\t',self.Line.find('run'))+1:self.Line.find('\t',self.Line.find('\t',self.Line.find('run'))+1)]
    
	def getTimeStampLocal(self):
		ColonIndex = self.Line.find(':')
		i = ColonIndex
		while self.Line[i] != '\t':
			i-=1
		self.TimeStampLocal = self.Line[i+1:ColonIndex+3]
    
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
		self.scndsTime = 3600*int(self.TimeStampLocal[self.TimeStampLocal.find(' ')+1:self.TimeStampLocal.find(':')])+60*int(self.TimeStampLocal[self.TimeStampLocal.find(':')+1:])
	def infoOut(self):
		print(self.scndsTime)
		print(self.EventMessage)
		print(self.EventSource)
		print(self.FileNumber)
		print(self.TimeStampLocal)
		print(self.RunNumber)
		print(self.Line)

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
		AcqStartedLines.append(fileLine(lines[i],i,'Acquisition Started'))
		continue
	if 'User' in lines[i]:
		if 'User' in lines[i+1]:
			continue
		else:
			onlyNeededLines.append(fileLine(lines[AcqSysIndex],AcqSysIndex,'AcquisitionSystem'))
			onlyNeededLines.append(fileLine(lines[i],i,'User'))
			if 'Acquisition Started' in lines[i+1]:
				AcqStartedLines.append(fileLine(lines[i+1],i+1,'Acquisition Started'))
				onlyNeededLines.append(fileLine(lines[i+2],i+2,'AcquisitionSystem'))
			else:
				onlyNeededLines.append(fileLine(lines[i+1],i+1,'AcquisitionSystem'))
for i in range