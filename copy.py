import imp
import os
import shutil


def copy_files(source, target):
    try:
        for path, _, files in os.walk(source):
            if files:
                for file in files:
                    source_file = os.path.join(path, file)
                    if not os.path.isfile(os.path.join(target, file)):
                        shutil.copy(source_file, target)
                        print("All files copied")
    except Exception as e:
        print(f"Error occurred: {e}")


# Call the function with your source and target paths
source_path = r"C:\target"  # Replace with your source directory
target_path = r"E:\OneDrive\Desktop\os projecr\move"  # Replace with your target directory
copy_files(source_path, target_path)
