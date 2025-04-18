#command line interface
import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(f"\r⏳ Time Left: {timer}", end="")
        time.sleep(1)
        seconds -= 1
    print("\n✅ Time's up! Take a break.")

def pomodoro_session(work=25, short_break=5, long_break=15, sessions=4):
    for i in range(1, sessions + 1):
        print(f"\n🔔 Session {i}: Work for {work} minutes.")
        countdown(work)
        
        if i != sessions:
            print(f"\n🌿 Short break for {short_break} minutes.")
            countdown(short_break)
        else:
            print(f"\n🌴 Long break for {long_break} minutes.")
            countdown(long_break)

if __name__ == "__main__":
    print("🍅 Welcome to the Pomodoro Timer!")
    pomodoro_session()
