import os

# Global variable to store renaming history
renaming_history = []

def list_files(directory):
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    for index, file in enumerate(files):
        print(index, file)

def rename_files(directory):
    index = input("Choose the index of the file you want to rename: ")
    old_file_name = os.listdir(directory)[int(index)]
    print("Old file name: ", old_file_name)
    new_name = input("Enter the new file name: ")
    os.rename(os.path.join(directory, old_file_name), os.path.join(directory, new_name))
    renaming_history.append((new_name, old_file_name))
    print("File renamed successfully!")

def bulk_rename(directory):
    add_up_type = input("Enter prefix or suffix: ")
    add_up = input("Enter the add-up: ")
    files = os.listdir(directory)
    for index, file in enumerate(files):
        if os.path.isfile(os.path.join(directory, file)):
            name, ext = os.path.splitext(file)
            if add_up_type == 'prefix':
                new_name = add_up + name + ext
            elif add_up_type == 'suffix':
                new_name = name + add_up + ext
            else:
                print("Invalid add-up type.")
                return
            os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
            renaming_history.append((new_name, file))
    print("Bulk rename completed!")

def undo_rename(directory):
    while renaming_history:
        old_name, new_name = renaming_history.pop()
        # print(old_name, new_name)
        os.rename(os.path.join(directory, old_name), os.path.join(directory, new_name))
        print("Undo rename successful!")
    else:
        print("No renaming operations to undo.")

def main():
    directory = input("Enter directory path: ")
    print("File Renaming System!!")
    print("1. List Files")
    print("2. Rename Files")
    print("3. Bulk Rename")
    print("4. Undo Rename")
    print("5. Exit")
    while True:
        choice = input("Enter your choice: ")
    
        if choice == '1':
            list_files(directory)
        elif choice == '2':
            rename_files(directory)
        elif choice == '3':
            bulk_rename(directory)
        elif choice == '4':
            undo_rename(directory)
        elif choice == '5':
            exit()
        else:
            print("Invalid choice!")

main()
