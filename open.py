import os
import shutil

def list_files(directory):
    files_list = []
    for root, dirs, files in os.walk(directory):
        for name in files:
            files_list.append(os.path.join(root, name))
    return files_list

def display_options_and_choose_drive():
    print("Options:")
    print("1. C Drive")
    print("2. E Drive")
    drive_option = int(input("Choose a drive (1 or 2): "))

    if drive_option == 1:
        return "C:/"
    elif drive_option == 2:
        return "E:/"
    else:
        print("Invalid drive option")
        return None

def display_and_choose_file(files_list):
    print("Files in the chosen drive:")
    for i, file_path in enumerate(files_list, start=1):
        print(f"{i}. {file_path}")
    
    file_option = int(input("Choose a file by entering its number: "))
    
    if 1 <= file_option <= len(files_list):
        return files_list[file_option - 1]
    else:
        print("Invalid file option")
        return None

def open_application(application_path):
    try:
        os.startfile(application_path)
    except Exception as e:
        print(f"Error: {e}")

def copy_file(source_path, target_path):
    try:
        shutil.copy(source_path, target_path)
        print(f"Copied: {source_path} to {target_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

def delete_file(file_path):
    try:
        os.unlink(file_path)
        print(f"Deleted: {file_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except PermissionError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

# Main code
drive_path = display_options_and_choose_drive()
if drive_path is not None:
    files_list = list_files(drive_path)
    
    if not files_list:
        print("No files found in the chosen drive.")
    else:
        chosen_file_path = display_and_choose_file(files_list)
        
        if chosen_file_path is not None:
            # Display options for copy or delete
            print("Options:")
            print("1. Copy file")
            print("2. Delete file")
            option = int(input("Choose an option (1 or 2): "))
            
            if option == 1:  # Copy file
                target_folder = input("Enter the target folder: ")
                target_path = os.path.join(drive_path, target_folder)
                
                copy_file(chosen_file_path, target_path)
                
            elif option == 2:  # Delete file
                delete_file(chosen_file_path)
                
            else:
                print("Invalid option")
