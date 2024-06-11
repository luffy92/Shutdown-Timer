import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta
import os
import threading
from playsound import playsound

def shutdown():
    os.system("shutdown /s /t 1")

def sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

class CountdownApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Auto Sleep/Shutdown")
        self.root.geometry("350x250")
        
        self.hours_var = tk.IntVar()
        self.minutes_var = tk.IntVar()
        self.option_var = tk.StringVar(value="shutdown")
        self.time_left = None
        self.timer_running = False
        
        self.create_widgets()
        
    def create_widgets(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12, "bold"))
        style.configure("TRadiobutton", font=("Helvetica", 12))
        
        self.main_frame = ttk.Frame(self.root, padding="10 10 10 10")
        self.main_frame.grid(column=0, row=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.main_frame.columnconfigure(0, weight=1)
        self.main_frame.rowconfigure(0, weight=1)
        
        ttk.Label(self.main_frame, text="Hours:").grid(column=0, row=0, padx=5, pady=5, sticky="E")
        ttk.Entry(self.main_frame, textvariable=self.hours_var, width=5, font=("Helvetica", 12)).grid(column=1, row=0, padx=5, pady=5, sticky="W")
        
        ttk.Label(self.main_frame, text="Minutes:").grid(column=2, row=0, padx=5, pady=5, sticky="E")
        ttk.Entry(self.main_frame, textvariable=self.minutes_var, width=5, font=("Helvetica", 12)).grid(column=3, row=0, padx=5, pady=5, sticky="W")
        
        ttk.Radiobutton(self.main_frame, text="Shutdown", variable=self.option_var, value="shutdown").grid(column=0, row=1, padx=5, pady=5, columnspan=2, sticky="W")
        ttk.Radiobutton(self.main_frame, text="Sleep", variable=self.option_var, value="sleep").grid(column=2, row=1, padx=5, pady=5, columnspan=2, sticky="W")
        
        self.start_button = ttk.Button(self.main_frame, text="Start", command=self.toggle_timer)
        self.start_button.grid(column=0, row=2, columnspan=4, padx=5, pady=20, sticky=(tk.W, tk.E))
        
        self.countdown_label = ttk.Label(self.main_frame, text="", font=("Helvetica", 18, "bold"))
        self.countdown_label.grid(column=0, row=3, columnspan=4, padx=5, pady=5, sticky="E")
        
    def toggle_timer(self):
        if self.timer_running:
            self.stop_timer()
        else:
            self.start_timer()
    
    def start_timer(self):
        hours = self.hours_var.get()
        minutes = self.minutes_var.get()
        total_seconds = hours * 3600 + minutes * 60
        
        if total_seconds <= 0:
            return
        
        self.time_left = timedelta(seconds=total_seconds)
        self.end_time = datetime.now() + self.time_left
        self.timer_running = True
        self.start_button.config(text="Stop")
        self.update_countdown()
        
    def stop_timer(self):
        self.timer_running = False
        self.start_button.config(text="Start")
        self.countdown_label.config(text="")
        
    def update_countdown(self):
        if not self.timer_running:
            return
        
        self.time_left = self.end_time - datetime.now()
        
        if self.time_left <= timedelta(seconds=0):
            self.execute_action()
            self.stop_timer()
            return
        
        seconds_left = self.time_left.total_seconds()
        
        if seconds_left <= 10:
            self.countdown_label.config(foreground="red")
            threading.Thread(target=playsound, args=("sound.mp3",), daemon=True).start()
        else:
            self.countdown_label.config(foreground="black")
        
        self.countdown_label.config(text=str(self.time_left).split(".")[0])
        self.root.after(1000, self.update_countdown)
        
    def execute_action(self):
        if self.option_var.get() == "shutdown":
            shutdown()
        elif self.option_var.get() == "sleep":
            sleep()

if __name__ == "__main__":
    root = tk.Tk()
    app = CountdownApp(root)
    root.mainloop()
