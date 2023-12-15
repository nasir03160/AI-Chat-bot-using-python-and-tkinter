import os

def move_files(source, target):
    try:
        for root, dirs, files in os.walk(source):
            for file in files:
                source_path = os.path.join(root, file)
                target_path = os.path.join(target, file)
                
                if not os.path.exists(target_path):  # Check if the file exists in the target directory
                    os.rename(source_path, target_path)
                    
        print('All files moved successfully!')
        
    except Exception as e:
        print(f'Error occurred: {e}')

# Call the function with your source and target paths
source_path = r"C:\target"  # Replace with your source directory
target_path = r"E:\OneDrive\Desktop\os projecr\move"  # Replace with your target directory
move_files(source_path, target_path)
