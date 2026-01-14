''' ==================== File Orangnizer ==================== '''
# to keep the desktop organized and file handing operations like create, update, copy and delete

import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File name {filename}: created succesfully!")
            
    except FileExistsError:
        print(f"file name {filename} already exists!")
        
    except Exception as e:
        print(f'An Error occurred -> {e}')
        
def view_all_files():
    files = os.listdir()
    if not files:
        print('No file found.')
    else:
        print('Files in directory.')
        for file in files:
            print(file)
            
def delete_file(filename):
    try:
        os.remove(filename)
        print(f'{filename} has been deleted succesfully!')
    except FileNotFoundError:
        print('file not found.')
        
    except Exception as e:
        print(f'An Error occurred -> {e}')
        
def read_file(filename):
    try:
        with open(filename, 'r') as f:
            content = f.read()
            print(f"Content of {filename} :\n{content}")
            
    except FileNotFoundError:
        print("file not found.")
    
    except Exception as e:
        print(f"An Error occurred -> {e}")
        
def edit_file(filename):
    try:
        with open(filename, 'a') as f:
            content = input('Enter content to add -> ')
            f.write(content + "\n")
            print(f'Content added to {filename} successfully!')
            
    except FileNotFoundError:
        print("File not found.")
        
    except Exception as e:
        print(f"An error occurred -> {e}")
        
        
def main():
    while True:
        print("=================== Terminal File Organizer ====================")
        print(f"1 - Create a file")
        print(f"2 - delete a file")
        print(f"3 - Edit the file")
        print(f"4 - Read the file")
        print(f"5 - View all file")
        print(f"6 - Exit the code")
        
        choice = input(f"Enter your choice [1-6] -> ")
        if choice == '1':
            filename = input("Enter the file-name to create -> ")
            create_file(filename)
            print("\n")
            
        elif choice == '2':
            filename = input("Enter the file name to delete -> ")
            delete_file(filename)
            print("\n")
            
        elif choice == '3':
            filename = input("Enter the name of the file to edit -> ")
            edit_file(filename)
            print("\n")
             
        elif choice == '4':
            filename = input("Enter the file name to Read -> ")
            read_file(filename)
            print("\n")
            
        elif choice == '5':
            view_all_files()
            print("\n")
            
        elif choice == '6':
            print("Closing the terminal file...")
            break
            
        else:
            print('In-valid syntax')
            
if __name__ == "__main__":
    main()