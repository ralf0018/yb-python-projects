# Read the txt file "sample_text.txt" and printout the first and last line of the file. See below

path = "./week4/inclass_activities/sample_text.txt"
with open(path , "r") as file:
    lines = file.readlines() # read all lines into a list
    
    # Print first and last line if file is not empty
    if lines:
        print("First line:", lines[0].rstrip())
        print("Last line:", lines[-1].rstrip())
    else:
        print("The file is empty")
