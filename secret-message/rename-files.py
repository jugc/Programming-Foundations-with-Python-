import os
def rename_files(folder):
    # (1) get file names from a folder
    file_list = os.listdir(folder)
    print file_list
    saved_path = os.getcwd()
    # (2) for each file, rename file
    os.chdir(folder)
    for file_name in file_list:
        os.rename(file_name,file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

#Photo_folder = "/Users/jk_home/Documents/Juan/Code/udacity/Programming-Foundations-with-Python-/secret-message/prank"
photo_folder_mini_proj = "/Users/jk_home/Documents/Juan/Code/udacity/Programming-Foundations-with-Python-/secret-message/my-secret-message"
rename_files(photo_folder_mini_proj)
