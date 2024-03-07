import os
import zipfile

def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created successfully.")
    else:
        print(f"Directory '{directory}' already exists.")

def extract_zip(zip_file, extract_to):
    create_directory(extract_to)
    print("Processing file "+zip_file);
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
        print("Extracted "+ zip_file)

print("Enter valid dir path ")
path = input()
dir_list = os.listdir(path)
print(dir_list)
for d in dir_list:
    # Create the full path to the item
    full_path = os.path.join(path, d)
    if os.path.isfile(full_path):
        textName = os.path.splitext(d)
        extension = textName[1]
#print("Is a file: " + textName[0])
#print("extension =  " + textName[1])
        if extension == ".zip":
#print("It is a zip file......");
            extract_zip(full_path, os.path.join(path,textName[0]))
