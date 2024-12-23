import time
import shutil
import pathlib


print("\033[1;34mFile Transfer Script\033[0m")
# TO START THE PROCESS


def FileTransfer(source, target="."):
       Source = pathlib.Path(source)
       SFiles = Source.glob("*")
       if Source.exists():
               Target = pathlib.Path(target)
               if Target.exists():
                   print(r"Starting Process!, Please don't interrupt to avoid file loss")
                   file_count = 0
                   for file in SFiles:
                       time.sleep(0.8)
                       try:
                           print(f"Transferring {file_count} Files")
                           file_count += 1
                           shutil.move(str(file), target)
                           time.sleep(1)
                       except shutil.Error:
                           print("\033[1;4;31mTransfer Error\033[0m")
                           time.sleep(1.0)
                           break
                       print("\033[1;32mTransfer Complete :)\033[0m")
                   print("")

               else:
                   print("\033[1;31mInvalid Path\033[0m")
                   time.sleep(0.9)
                   print("\033[34mDon't fret try again\033[0m")
       else:
           print("Oops!, you passed in an invalid path!!, but don't fret try again")
           time.sleep(1)

def create_folder(name):
    try:
        pathlib.Path(name).mkdir()
        print(f"\033[1;3;32mCreated \033[4m{name}\033[0m")
    except FileExistsError:
        print("\033[1;31mFolder Already Exist\033[0m")
    time.sleep(1)
def delete_folder(name):
    try:
        pathlib.Path(name).rmdir()
        print(f"\033[1;32mDeleted {name}\033[0m")
    except FileNotFoundError:
        print("\033[1;31mFolder Doesn't Exist\033[0m")
    time.sleep(1)

while True:
    print("""----------------------------------------
Enter:
1. Create a Folder
2. Delete a Folder
3. Transfer Files
4. Exit""")
    choice = input("Enter your choice: ")
    if choice == "1":
        folder_name = input("Folder Name: ")
        create_folder(folder_name)

    elif choice == "2":
        folder_name = input("Folder Name: ")
        delete_folder(folder_name)

    elif choice == "3":
        Source = input("Path to source folder: ")
        Target = input("Path to target folder: ")
        if Target:
            FileTransfer(Source, Target)
        elif not Target:
            FileTransfer(Source)

    elif choice == "4":
        print("Exiting...")
        time.sleep(2.0)
        print("Exited")
        break