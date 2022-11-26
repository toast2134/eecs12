##Name: Jonathan Le, ID: 26713365
##Date: Oct 25, 2021
import os
def main():
	inName=input("What is the name of the input file: ")
	outName=inName[:-4]+"-out.txt"
	outF=open(outName,"w")
	if os.path.exists(inName)==0:
		outF.write("Cannot find the input file.")
	else:
		inF=open(inName,"r")
		EEC,CpEC,MeC,CeC,other=0,0,0,0,0
		for line in inF.readlines():
			line=line[:-1]
			listL=line.split(" ; ")
			for s in listL:
				if(s==listL[0]):
					outF.write(s)
				elif(s=="Electrical Engineering"):
					EEC+=1
					outF.write(" 1 ")
				elif(s=="Computer Engineering"):
					CpEC+=1
					outF.write(" 2 ")
				elif(s=="Mechanical Engineering"):
					MeC+=1
					outF.write(" 3 ")
				elif(s=="Civil Engineering"):
					CeC+=1
					outF.write(" 4 ")
				else:
					outF.write(" 0 ")
			outF.write("\n")
		outF.write("The number of Electrical Engineering students: "+str(EEC))
		outF.write("\nThe number of Computer Engineering students: "+str(CpEC))
		outF.write("\nThe number of Mechanical Engineering students: "+str(MeC))
		outF.write("\nThe number of Civil Engineering students: "+str(CeC))
		inF.close()
		outF.close()
main()
