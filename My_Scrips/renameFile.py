import os
import time

initial_path = r"C:\Users\Charalampos\Downloads\0- OVT\Κτηματολόγιο\temp\HotFolder\TestCase\ΒΙΒΛΙΟ ΥΠΟΘΗΚΩΝ - ΤΟΜΟΣ 1_00000006.TIF"

directory, original_filename = os.path.split(initial_path)
base_name, extension = os.path.splitext(original_filename)

current_path = initial_path

for counter in range(1, 31):
    new_filename = f"{base_name}_{counter}{extension}"
    new_path = os.path.join(directory, new_filename)
    
    try:
        os.rename(current_path, new_path)
        print(f"Renamed to: {new_filename}")
        
        current_path = new_path
    except FileNotFoundError:
        print(f"Error: The file '{current_path}' was not found.")
        break
    except PermissionError:
        print(f"Error: Permission denied when renaming '{current_path}'.")
        break
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    time.sleep(1)

print("Renaming process completed.")
