def findAcqStarted(linesArr,CurrentIndex,CurrAcqStarted): # поиск ближайшего Acquisition Started
	for i in range(CurrentIndex+1,len(linesArr)):
		if "Acquisition Started" in linesArr[i]:
			if i - CurrentIndex < CurrentIndex - CurrAcqStarted:
				return i
			else:
				return CurrAcqStarted
		return CurrAcqStarted

def acqSysFormat(CurrAcqLine):
	CurrAcqLine = CurrAcqLine[10:]
	CurrAcqLine = CurrAcqLine[CurrAcqLine.find("AcquisitionSystem")+3:CurrAcqLine.find("Inflow")]
	return CurrAcqLine

def userLineFormat(CurrUsrLine): # форматирование строки со значением User в поле EventSource
	usrLine = CurrUsrLine[CurrUsrLine.find("User")-36:-17]
	if usrLine[0] != '\t':
		usrLine = '\t'+usrLine
	usrLine = usrLine[:20]+usrLine[usrLine.find("User"):]
	return usrLine

	
with open(r"Example_file.log","r") as datafile:
	lines = datafile.readlines()

outputfile = open('result.txt','w')
outputfile.write('TimeStampRelative'+'\t'+'RunNumber'+'\t'+'TimeStampLocal'+'\t'+'EventSource'+'\t'+'FileNumber'+'\t'+'EventMessage'+'\n')
AcqStarted = -1
for i in range(len(lines)):
	if "AcquisitionSystem" in lines[i] and "Acquisition Started" not in lines[i]:
		AcqSys = i
	if "AcquisitionSystem" in lines[i] and "Acquisition Started" in lines[i]:
		AcqStarted = i
	if "User" in lines[i] and i != len(lines)-1:
		if "User" in lines[i+1]:
			continue
		else:
			AcqStarted = findAcqStarted(lines,i,AcqStarted)
			outputfile.write(acqSysFormat(lines[AcqSys])+'\n')
			outputfile.write(userLineFormat(lines[i])+'\n')
			if i+1 == AcqStarted:
				outputfile.write(lines[i+2]+'\n')
			else:
				outputfile.write(lines[i+1]+'\n')

outputfile.close()