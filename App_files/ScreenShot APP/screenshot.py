import time
import pyautogui
import tkinter as tk
import os

if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

def screenshot():
    name = f"screenshots/{int(round(time.time() * 1000))}.png"
    time.sleep(5)  # Delay for the user to adjust screen
    img = pyautogui.screenshot()
    img.save(name)
    img.show()
    print(f"Screenshot saved: {name}")

# GUI setup
root = tk.Tk()
root.title("Screenshot App")

frame = tk.Frame(root)
frame.pack(pady=20)

button = tk.Button(frame, text="Take Screenshot", command=screenshot)
button.pack(side=tk.LEFT, padx=10)

close = tk.Button(frame, text="QUIT", command=root.quit)
close.pack(side=tk.LEFT, padx=10)

root.mainloop()
