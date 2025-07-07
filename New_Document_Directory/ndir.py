import os

# Specify the directory name
directory_name = "Directory"

# Creating Directory (Single Directory)
try:
    os.mkdir(directory_name)
    print(os.path)
    print(f"Directory '{directory_name}' created successfully.")
except FileExistsError:
    print(f"Directory '{directory_name}' already exists.")
except PermissionError:
    print(f"Permission denied: Unable to create '{directory_name}'.")
except Exception as e:
    print(f"An error occurred: {e}")


# Creating Multiple Directories
num = input("Enter any number for Directories to be Created:")
stnum = 5  # Can use an num variable tto for multiple directories
# print(stnum)

for i in range(stnum):
    try:
        irng = str(i)

        # In present directory
        os.mkdir(irng)

        # For any specific path
        # os.mkdir('C:\work@taneshka\dev_env\TM\Documents\%s' %n)
        
        print(os.path)
        print(f"Directory '{irng}' created successfully.")
    except FileExistsError:
        print(f"Directory '{irng}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{irng}'.")
    except Exception as e:
        print(f"An error occurred: {e}")
