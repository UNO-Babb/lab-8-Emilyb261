#ProcessData.py
#Name: Emily Billings
#Date:
#Assignment:

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')

  #Process each line of the input file and output to the CSV file
  #line = inFile.readline()
  for line in inFile: 
    data = line.split()
    first = data[0] 
    last = data[1] 
    major = data[2] 
    idNum = data[3] 
    year = data[4].upper()

    student_id = makeID(first, last, idNum) 
    
  

    major_year = major[:3].upper() + "-" + year 

    output = f"{last},{first},{student_id},{major_year}\n"
    outFile.write(output)

    #print(student_id) 

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()
  
def makeID(first, last, idNum):
  #print(first, last, idNum) 
  IdLen = len(idNum) 

  while len(last) < 5:
    last = last + "X" 

  id = first[0] + last + idNum[IdLen - 3: ] 

  #print(id) 
  return id 



if __name__ == '__main__':
  main()
