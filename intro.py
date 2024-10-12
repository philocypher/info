import sys
import time
import socket

def spinner_animation(duration=3):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration

    while time.time() < end_time:
        for symbol in spinner:
            sys.stdout.write(f'\r Loading [{symbol}]')
            sys.stdout.flush()
            time.sleep(0.1)  # Adjust the speed of the spinner

    sys.stdout.write('\rDone!          \n')  # Clear the line after completion

# Run the spinner for 5 seconds
if __name__ == "__main__":
    spinner_animation(5)
