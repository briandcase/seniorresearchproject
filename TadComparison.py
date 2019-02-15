import os, glob

# The file we are comparing all other files to
index_file = 'C:/Users/bdcas/eclipse-workspace/TadComparison/Spleen_Donor-PX1-raw_TADS.txt'   

# use the module glob to get all the files in our directory, and make a list of files we will compare with
file_list = [f for f in glob.iglob('C:/Users/bdcas/eclipse-workspace/TadComparison/comparison/*.txt', recursive=True) if os.path.isfile(f)]
        
for f in file_list:
    with open('results.txt', 'a') as i: 
    #open both files we are comparing
        file1 = open(index_file, "r")
        file2 = open(f,'r')
    
        #find the differences in the files
        same = set(file1).intersection(file2)
    
        #get lines in file1
        file1 = open(index_file, "r")
        file1_lines = file1.readlines()    
        file1_count_lines = 0
        for f in file1_lines:
            file1_count_lines += 1 
    
        # get percent match and then print out
        percentsame = 0
        percentsame = (len(same) / file1_count_lines) * 100
   
   
        print('Our index file is -> ' + str(index_file), file=i)
        print('', file=i)
        print('Comparing against file -> ' + str(file2), file=i)
        print(same, file=i) 
        print('', file=i)
        print('Number of lines in file to be compared against: ', file=i)
        print(file1_count_lines, file=i)
        print('Number of matches: ', file=i)
        print(len(same), file=i)
        print('Percent matched with file: ', file=i)
        print(str(round(percentsame, 2)) + ' %%', file=i)
        print('', file=i) 
        file2.close()
        
# cleanup

file1.close()
i.close()
