import os
import shutil
from pathlib import Path

def processFolder(folder):
    print(folder)
    upper_folder_name = os.path.basename(folder)
    upper_folder = Path(folder).parent
    for count, filename in enumerate(os.listdir(folder)):
        current_file_path = os.path.join (folder, filename)
        new_file_path = os.path.join (upper_folder, upper_folder_name + '_' + filename)
        print (current_file_path + ' -> ' + new_file_path)
        shutil.move(current_file_path, new_file_path)

def applyOnSubfolders(folder, func):
    for root, directories, files in os.walk(folder, topdown=False):
        for name in directories:
            func(os.path.join(folder,  name))


def main():

    folder = r"C:\Users\Tsonski\Desktop\GoogleDrive\h11135912_Photos_Best\Photos_012_Best\2012"   
    
    applyOnSubfolders(folder, processFolder)


# Driver Code
if __name__ == '__main__':
     
    # Calling main() function
    main()