import time

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        time_format = "{:02d}:{:02d}" .format(mins, secs)
        print(time_format, end="\r")
        time.sleep(1)
        time_sec -= 1
    
    print("Stopped")

def main():
    print("==== Countdown Timer ====")

    hours = int(input("Enter the number of hours: "))
    mins = int(input("Enter the number of minutes: ")) 
    secs = int(input("Enter the number of seconds: "))

    time_sec = (hours * 3600) + (mins * 60) + secs
    countdown(time_sec)

if __name__ == "__main__":
    main()


