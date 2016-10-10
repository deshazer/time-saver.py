import re

#   usage: process_csv_separate_addr( inputfile, outputfile )
#   Opens the file specified by param inputfile
#   Reads the entire file into a string
#   Processes the string to separate out the address into 4 columns
#   Writes the output to the file name specified by the param outputfile
#   Closing of the opened files should be handled outside the call to this method
def process_csv_separate_addr(inputfile, outputfile):


    #Get rid of first line containing column headers (this line is discarded)
    inputfile.readline()

    #Read in the rest of the file
    originaltext = inputfile.read()

    # Handles situations where the package is being shipped care-of someone
    # Comment this out if you don't want c/o...etc to appear in the same cell as the street address
    # NOTE: If you comment this line out the c/o case will have to be handled manually before processing
    output = re.sub(r"(\"c/o .+)(?<=[\w])[\r\n]+", r"\1 ", originaltext, flags=re.MULTILINE)

    #print output   #debug print statement

    #find and replace address in one cell with address split into 4 cells:
    #Street Address, City, State, Zip Code
    output = re.sub(r"\"([^\"]+)\n(.+) (\w{2}) (\d{5})\"", r"\1,\2,\3,\4", output, flags=re.MULTILINE)

    #print output   #debug print statement

    #remove \n from other cells
    # ---DOESN'T WORK YET---
    #output = re.sub(r"\"([^\"]+)\n([^\"]+)\"", r"\1 or \2", output, flags=re.MULTILINE)

    #print output   #debug print statement


    outputfile.write("Order Number / RMA #,Serial Number,Date,Customer Name,Address,City,State,Zip,"
                    "Phone Number,Email Address,Special Instructions\n")
    outputfile.write(output)
