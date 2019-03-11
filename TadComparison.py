import os, glob

# The file we are comparing all other files to
for filename_a in glob.iglob("C:/Users/bdcas/Dropbox/UHD_Spring_2019/SeniorProject/TAD/tads/*.txt", recursive=True):
    # use the module glob to get all the files in our directory, and make a list of files we will compare with
    for filename_b in glob.iglob("C:/Users/bdcas/Dropbox/UHD_Spring_2019/SeniorProject/TAD/tads/*.txt", recursive=True):

        with open('results.txt', 'a') as i: 
        #open both files we are comparing
            file1 = open(filename_a, "r")
            file2 = open(filename_b,"r")
    
            #find the differences in the files
            same = set(file1).intersection(file2)
    
            #get lines in file1
            file1 = open(filename_a, "r")
            file1_lines = file1.readlines()    
            file1_count_lines = 0
            for f in file1_lines:
                file1_count_lines += 1 
    
            # get percent match and then print out
            percentsame = 0
            percentsame = (len(same) / file1_count_lines) * 100
   
   
            print('Our index file is -> ' + str(filename_a), file=i)
            print('', file=i)
            print('Comparing against file -> ' + str(file2), file=i)
            print(same, file=i) 
            print('', file=i)
            print('Number of lines in file to be compared against: ', file=i)
            print(file1_count_lines, file=i)
            print('Number of matches: ', file=i)
            print(len(same), file=i)
            print('Percent matched with file: ', file=i)
            print(str(round(percentsame, 2)) + ' %', file=i)
            print('', file=i) 
            file2.close()
            file1.close()
i.close()
