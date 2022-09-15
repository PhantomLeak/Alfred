from genericpath import isfile
from terminal_colors import colors as terminal_message
import os
tc = terminal_message()

# List of directories that contain temporary files that should be deleted

def clear_local_files():
    dir = ['/mnt/c/Windows/Temp', '/mnt/c/Users/your user name/AppData/Local/Temp']
    # Loop through files in directory and delete them 
    for d in dir:
        print(tc.output_message(f'You are deleting files in {d}'))
        for (root, dir, files) in os.walk(d):
            for file in files:
                try:
                    os.remove(os.path.join(root, file))
                    print(tc.output_message(f'succesfully removed the temp file{file}'))
                except Exception as e:
                        print(tc.error_message(f'{e}'))