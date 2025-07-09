
import time

def slow_print(text, delay=0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    frame_top = "+" + "-" * 24 + "+"
    message = "|   Hello, World! :)   |"
    frame_bottom = "+" + "-" * 24 + "+"

    print(frame_top)
    slow_print(message)
    print(frame_bottom)

if __name__ == "__main__":
    main()