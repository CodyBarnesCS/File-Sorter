import os
import shutil

# set the path you would like to sort
file_path = r'/Users/codybarnes/Desktop/projects/python/file_sorter/test_folder/'

try:
    # get a list of all files in the source directory
    file_list = os.listdir(file_path)

    # create a folder for each file extension if one doesn't already exist
    for file_name in file_list:
        file_extension = os.path.splitext(file_name)[1][1:]
        extension_folder = os.path.join(file_path, file_extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)
        
        # move file to the appropriate folder
        original_path = os.path.join(file_path, file_name)
        new_path = os.path.join(extension_folder, file_name)
        shutil.move(original_path, new_path)

except:
    print('There was an error organizing your files.')