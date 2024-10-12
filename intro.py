import sys
import time

def spinner_animation(duration):
    spinner = ['|', '/', '-', '\\']
    end_time = time.time() + duration

    while time.time() < end_time:
        for symbol in spinner:
            sys.stdout.write(f'\r{symbol} Loading...')
            sys.stdout.flush()
            time.sleep(0.1)  # Adjust the speed of the spinner

    sys.stdout.write('\rDone!          \n')  # Clear the line after completion

# Run the spinner for 5 seconds
spinner_animation(5)
