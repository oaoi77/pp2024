#check the file exist or not 
#if exist, decompress and load data from the file

import zipfile
import os

#check file exist or not - os,path.exist()
file_zip = "student.dat"
ex_folder = "extract" #get the current directory working on 

if os.path.exists(file_zip):
    # Create a directory for extracted files if it doesn't exist
    if not os.path.exists(ex_folder):
        os.makedirs(ex_folder)
    
    #extract file zip
    with zipfile.ZipFile(file_zip, 'r') as zf:
        zf.extractall(ex_folder)

    #list file in extract folder
    extracted_file = os.listdir(ex_folder)
    for file in extracted_file:
        #too create path: /ex_folder/extracted_file.txt
        #if not, it cannot find the file in current directory because files 
        #are extracted to new directory
        file_path = os.path.join(ex_folder, file)
        #check if extracted file is a regular file
        if os.path.isfile(file_path):
            with open(file_path, 'r') as f:
                print("From", file, ": ")
                print(f.read())
                

else:
    print("File does NOT exist")