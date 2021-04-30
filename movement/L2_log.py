# This program contains functions for logging robot parameters
# to local files.  The files can be accessed by NodeRed or other programs.
# Nodered can be found on the beagle at port 1880. ie, 192.168.8.1:1880

# Import external libraries
import csv      # for handling comma-separated-values file type


# A function for populating 2 text files with updated phi-dots
def writeFiles(current_phis):
    txt = open("/home/debian/basics/PDL.txt", 'w+')         # file for phi dot left
    txt2 = open("/home/debian/basics/PDR.txt", 'w+')        # file for phi dot right
    phi_dotL = round(current_phis[0], 1)
    phi_dotR = round(current_phis[1], 1)
    txt.write(str(round(phi_dotL, 1)))
    txt2.write(str(round(phi_dotR, 1)))
    txt.close()
    txt2.close()


# A function for populating 2 text files with updating variables
def NodeRed2(values):                                       # this function takes a -2- 7-element array called val
    txt = open("/home/debian/basics/a.txt", 'w+')           # file for generic variable a, going to be first, 0th, element in val arry, which in L3_telementry is the x-axis
    txt2 = open("/home/debian/basics/b.txt", 'w+')          # file for generic variable b
    txt3 = open("/home/debian/basics/z.txt", 'w+')          # file for generic variable z, thrid elemetn is z axis
    txt4 = open("/home/debian/basics/batt.txt", 'w+')       # file for voltage of plug
    txt5 = open("/home/debian/basics/temm.txt", 'w+')       # file for temperature
    txt6 = open("/home/debian/basics/press.txt", 'w+')       # file for pressure
    txt7 = open("/home/debian/basics/alti.txt", 'w+')       # file for altitude
    a = round(values[0], 2)
    b = round(values[1], 2)
    z = round(values[2], 2)
    batt = round(values[3], 2)
    temm = round(values[4], 2)
    press = round(values[5], 2)
    alti = round(values[6], 2)
    txt.write(str(a))
    txt2.write(str(b))
    txt3.write(str(z))
    txt4.write(str(batt))
    txt5.write(str(temm))
    txt6.write(str(press))
    txt7.write(str(alti))
    txt.close()
    txt2.close()
    txt3.close()
    txt4.close()
    txt5.close()
    txt6.close()
    txt7.close()


# A function for sending 1 value to a log file of specified name
def uniqueFile(value, fileName):                            # this function takes a 2-element array called val
    txt = open("/home/debian/basics/" + fileName, 'w+')     # file with specified name
    myValue = round(value, 2)
    txt.write(str(myValue))
    txt.close()


# A function for sending 1 value to a log file in a temporary folder
def tmpFile(value, fileName):                               # this function takes a 2-element array called val
    txt = open("/tmp/" + fileName, 'w+')                    # file with specified name
    myValue = round(value, 2)
    txt.write(str(myValue))
    txt.close()

# A function for saving a single line string to a log file in a temporary folder
def stringTmpFile(myString, fileName):     # this function takes a string and filename
    txt = open("/tmp/" + fileName, 'w+')   # file with specified name
    txt.write(myString)                    # by default the existing txt is overwritten
    txt.close()

# A function for creating a CSV file from a list of values.
def csv_write(list):
    list = [str(i) for i in list]
    with open('excel_data.csv', 'a') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerow(list)
    csvFile.close()


# A function to clear an existing CSV file
def clear_file():
    open('excel_data.csv', 'w').close()
