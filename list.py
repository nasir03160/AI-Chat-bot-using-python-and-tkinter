import os

directory_path = r'E:\OneDrive\Desktop\os projecr'  # Replace with the path to your directory
file_list = os.listdir(directory_path)

for file in file_list:
    print(file)