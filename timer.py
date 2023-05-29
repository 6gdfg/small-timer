import tkinter as tk
import time
import winsound

class Timer:
    def __init__(self, master):
        self.master = master
        self.master.title("timer")
        self.master.geometry("900x400")
        self.master.resizable(False, False)

        self.hour = 0
        self.minute = 30
        self.second = 0
        self.running = False

        self.timer_label = tk.Label(self.master, text="{}:{}:{}".format(self.hour, self.minute, self.second), font=("Arial", 30))
        self.timer_label.pack(pady=20)

        self.start_button = tk.Button(self.master, text="start", font=("Arial", 20), command=self.start_timer)
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(self.master, text="stop", font=("Arial", 20), command=self.stop_timer)
        self.stop_button.pack(pady=10)

        self.hour_button = tk.Button(self.master, text="h+1", font=("Arial", 16), command=self.add_hour)
        self.hour_button.pack(side=tk.LEFT, padx=10)

        self.minute_button = tk.Button(self.master, text="min+1", font=("Arial", 16), command=self.add_minute)
        self.minute_button.pack(side=tk.LEFT, padx=10)

        self.second_button = tk.Button(self.master, text="s+1", font=("Arial", 16), command=self.add_second)
        self.second_button.pack(side=tk.LEFT, padx=10)

        self.hour_subtract_button = tk.Button(self.master, text="h-1", font=("Arial", 16), command=self.subtract_hour)
        self.hour_subtract_button.pack(side=tk.LEFT, padx=10)

        self.minute_subtract_button = tk.Button(self.master, text="min-1", font=("Arial", 16), command=self.subtract_minute)
        self.minute_subtract_button.pack(side=tk.LEFT, padx=10)

        self.second_subtract_button = tk.Button(self.master, text="s-1", font=("Arial", 16), command=self.subtract_second)
        self.second_subtract_button.pack(side=tk.LEFT, padx=10)
        
        self.one_minute_button = tk.Button(self.master, text="1min", font=("Arial", 16), command=self.set_one_minute)
        self.one_minute_button.pack(side=tk.LEFT, padx=10)

        self.five_minutes_button = tk.Button(self.master, text="5min", font=("Arial", 16), command=self.set_five_minutes)
        self.five_minutes_button.pack(side=tk.LEFT, padx=10)

        self.ten_minutes_button = tk.Button(self.master, text="10min", font=("Arial", 16), command=self.set_ten_minutes)
        self.ten_minutes_button.pack(side=tk.LEFT, padx=10)

        self.thirty_minutes_button = tk.Button(self.master, text="30min", font=("Arial", 16), command=self.set_thirty_minutes)
        self.thirty_minutes_button.pack(side=tk.LEFT, padx=10)

        self.one_hour_button = tk.Button(self.master, text="1h", font=("Arial", 16), command=self.set_one_hour)
        self.one_hour_button.pack(side=tk.LEFT, padx=10)

    def start_timer(self):
        self.start_button.config(state=tk.DISABLED)
        self.running = True
        total_seconds = self.hour * 3600 + self.minute * 60 + self.second
        while total_seconds > 0 and self.running:
            self.hour = total_seconds // 3600
            self.minute = (total_seconds - self.hour * 3600) // 60
            self.second = total_seconds - self.hour * 3600 - self.minute * 60
            self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))
            self.master.update()
            time.sleep(1)
            total_seconds -= 1
        if total_seconds == 0:  # Check if the timer reached 0
            self.play_ringtone()  # Play the ringtone
        self.start_button.config(state=tk.NORMAL)
    
    def stop_timer(self):
        self.running = False

    def add_hour(self):
        self.hour += 1
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def add_minute(self):
        self.minute += 1
        if self.minute == 60:
            self.hour += 1
            self.minute = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def add_second(self):
        self.second += 1
        if self.second == 60:
            self.minute += 1
            self.second = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))
    
    def subtract_hour(self):
        self.hour -= 1
        if self.hour < 0:
            self.hour = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def subtract_minute(self):
        self.minute -= 1
        if self.minute < 0:
            self.minute = 0
        if self.minute == 59:
            self.hour -= 1
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def subtract_second(self):
        self.second -= 1
        if self.second < 0:
            self.second = 0
        if self.second == 59:
            self.minute -= 1
        if self.minute < 0:
            self.minute = 0
            self.hour -= 1
        if self.hour < 0:
            self.hour = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))
    
    def set_one_minute(self):
        self.hour = 0
        self.minute = 1
        self.second = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def set_five_minutes(self):
        self.hour = 0
        self.minute = 5
        self.second = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def set_ten_minutes(self):
        self.hour = 0
        self.minute = 10
        self.second = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def set_thirty_minutes(self):
        self.hour = 0
        self.minute = 30
        self.second = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))

    def set_one_hour(self):
        self.hour = 1
        self.minute = 0
        self.second = 0
        self.timer_label.config(text="{}:{}:{}".format(self.hour, self.minute, self.second))
    def play_ringtone(self):
        frequency = 2500  # Set frequency to 2500 Hz
        duration = 1000  # Set duration to 1000 ms (1 second)
        for i in range(3):  # Play the ringtone 3 times
            winsound.Beep(frequency, duration)
            time.sleep(0.5)  # Wait half a second between each ringtone

root = tk.Tk()
timer = Timer(root)
root.mainloop()
