import os
import time
import pyfiglet

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_time_in_ascii():
    while True:
        current_time = time.strftime("%H:%M:%S")
        ascii_art = pyfiglet.figlet_format(current_time)
        clear_screen()
        print(ascii_art)
        time.sleep(1)

if __name__ == "__main__":
    display_time_in_ascii()
