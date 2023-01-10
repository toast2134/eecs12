# Name: Jonathan Le
# Date: Oct 25, 2021
#
# import os library
import os

# main function
def main():

	# getting user input
	inName = input("What is the name of the input file: ")

	# removes .txt and replaces it with -out.txt for output file name
	outName = inName[:-4]+"-out.txt"

	#open output file and set it to write mode
	outF = open(outName,"w")

	# checks if file exists (same directory)
	# if file doesn't exist -> prints "Can't find to an input file" into the name of the output file
	if os.path.exists(inName)==0:
		outF.write("Cannot find the input file.")

	# if file exists, process data
	else:
		# open input file and set it to read mode
		inF=open(inName,"r")

		# initialize variables
		EEC,CpEC,MeC,CeC,other=0,0,0,0,0

		# data processing
		# sets line equal to a line in the file up until a new line
		for line in inF.readlines():

			# remove newline character
			line=line[:-1]

			# split at semicolons 
			listL=line.split(" ; ")

			# process spliced string
			for s in listL:

				# first element will always be the name, so if s equals first element, we write essentially write the name into the output file
				if(s==listL[0]):
					outF.write(s)

				# encounter "Electrical Engineering major", increment counter for EEC, categorize as '1' in output file
				elif(s=="Electrical Engineering"):
					EEC+=1
					outF.write(" 1 ")
				
				# encounter "Computer Engineering", increment counter for CpEC, categorize as '2' in output file
				elif(s=="Computer Engineering"):
					CpEC+=1
					outF.write(" 2 ")

				# encounter "Mechanical Engineering", increment counter for MeC, categorize as '3' in output file
				elif(s=="Mechanical Engineering"):
					MeC+=1
					outF.write(" 3 ")

				# encounter "Civil Engineering", increment counter for CeC, categorize as '4' in output file
				elif(s=="Civil Engineering"):
					CeC+=1
					outF.write(" 4 ")

				# if not an engineering major, categorize as 0 and don't increment anything
				else:
					outF.write(" 0 ")

			# end of each line in output file, insert a newline
			outF.write("\n")
		
		# output totals after going through whole file
		outF.write("The number of Electrical Engineering students: "+str(EEC))
		outF.write("\nThe number of Computer Engineering students: "+str(CpEC))
		outF.write("\nThe number of Mechanical Engineering students: "+str(MeC))
		outF.write("\nThe number of Civil Engineering students: "+str(CeC))

		# close input and output files
		inF.close()
		outF.close()

main()
