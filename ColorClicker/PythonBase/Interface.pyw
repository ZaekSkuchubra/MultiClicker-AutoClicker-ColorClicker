import tkinter as tk
import subprocess 
import os
def open_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, "ColorClicker.py")
    try:
        subprocess.run(["xdg-open", filepath])
    except FileNotFoundError:
        try:
            subprocess.run(["open", filepath])
        except FileNotFoundError:
            subprocess.run(["start", "", filepath], shell=True)
def open_file1():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, "AutoClicker.py")
    try:
        subprocess.run(["xdg-open", filepath])
    except FileNotFoundError:
        try:
            subprocess.run(["open", filepath])
        except FileNotFoundError:
            subprocess.run(["start", "", filepath], shell=True)
root = tk.Tk()
root.title("ColorClicker ^-^ ")
root.geometry("400x250")
root.resizable(False, False)
root.config(bg=("LavenderBlush2"))
button = tk.Button(root, text=("Run Color Clicker"), borderwidth=0, bg= "LightPink2", command=open_file, width=200, height=2,font=("Raavi", 25, "bold"),)
button.pack(pady=10, padx= 10,)
button1 = tk.Button(root, text=("Run Simple Autoclicker"), borderwidth=0, bg= "LightPink2", command=open_file1, width=200, height=2,font=("Raavi", 25, "bold"),)
button1.pack(pady=10, padx= 10,)
root.mainloop()