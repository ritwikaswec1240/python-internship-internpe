import tkinter as tk
import time

def update_time():
    """Update the clock and date every second."""
    current_time = time.strftime("%H:%M:%S %p")  
    current_date = time.strftime("%A, %d %B %Y")  
    time_label.config(text=current_time)
    date_label.config(text=current_date)
    root.after(1000, update_time)  


root = tk.Tk()
root.title("Digital Clock")
root.geometry("400x250")
root.configure(bg="black")  


frame = tk.Frame(root, bg="cyan", bd=5)
frame.pack(pady=10, padx=10, fill="both", expand=True)


heading_label = tk.Label(frame, text="DIGITAL CLOCK", font=("Helvetica", 20, "bold"), fg="black", bg="cyan")
heading_label.pack(pady=5)


time_label = tk.Label(frame, font=("Helvetica", 40, "bold"), fg="white", bg="black")
time_label.pack()


date_label = tk.Label(frame, font=("Helvetica", 16), fg="yellow", bg="black")
date_label.pack(pady=5)

update_time()  

root.mainloop()
