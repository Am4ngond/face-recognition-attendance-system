openFile = open("demo.txt", "r")
writeFile = open("updatedFile", "w")
#Store traversed lines
tmp = set()
for txtLine in openFile:
#Check new line
 if txtLine not in tmp:
 writeFile.write(txtLine)
#Add new traversed line to tmp
 tmp.add(txtLine)
openFile.close()
writeFile.close()
