import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("480x700")
root.config(bg="black")

# -------------------------------
# Page Switching
# -------------------------------
def show_frame(frame):
    frame.tkraise()

# Frames
calculator_frame = tk.Frame(root, bg="black")
tools_frame = tk.Frame(root, bg="black")
stopwatch_frame = tk.Frame(root, bg="black")
timer_frame = tk.Frame(root, bg="black")

for frame in (calculator_frame, tools_frame, stopwatch_frame, timer_frame):
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

# -------------------------------
# Calculator
# -------------------------------
entry = tk.StringVar()
history = []

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(entry.get()))
            history.append(entry.get() + " = " + result)
            entry.set(result)
        except Exception:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    elif text == "⌫":
        entry.set(entry.get()[:-1])
    else:
        entry.set(entry.get() + text)

def show_history():
    if not history:
        messagebox.showinfo("History", "No history yet")
    else:
        messagebox.showinfo("History", "\n".join(history[-10:]))

input_field = tk.Entry(calculator_frame, textvar=entry, font="Arial 22", bg="black", fg="orange",
                       bd=4, relief="solid", justify="right", highlightthickness=2, highlightbackground="orange")
input_field.pack(fill="x", ipadx=8, pady=15, padx=10, ipady=10)

# Rounded buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"],
    ["C", "⌫"]
]

for row in buttons:
    frame = tk.Frame(calculator_frame, bg="black")
    frame.pack(expand=True, fill="both")
    for btn in row:
        b = tk.Button(frame, text=btn, font=("Arial", 16, "bold"),
                      bd=2, relief="solid", width=4, height=2,
                      bg="black", fg="orange",
                      highlightbackground="orange", highlightthickness=2)
        b.pack(side="left", expand=True, fill="both", padx=8, pady=8, ipadx=10, ipady=10)
        b.bind("<Button-1>", click)

# Tools + History at bottom
bottom_frame = tk.Frame(calculator_frame, bg="black")
bottom_frame.pack(pady=10)

tools_btn = tk.Button(bottom_frame, text="→ Tools", font=("Arial", 14, "bold"),
                      fg="orange", bg="black", relief="solid", highlightbackground="orange",
                      command=lambda: show_frame(tools_frame))
tools_btn.pack(side="left", padx=10)

history_btn = tk.Button(bottom_frame, text="⋮", font=("Arial", 16, "bold"),
                        command=show_history, bg="black", fg="orange", relief="solid")
history_btn.pack(side="right", padx=10)

# -------------------------------
# Tool Functions
# -------------------------------
def age_calc():
    birth = simpledialog.askstring("Age Calculator", "Enter your birth year (YYYY):")
    if birth and birth.isdigit():
        age = datetime.now().year - int(birth)
        messagebox.showinfo("Age", f"Your age is {age} years.")

def weight_calc():
    kg = simpledialog.askfloat("Weight Converter", "Enter weight in kg:")
    if kg:
        pounds = kg * 2.20462
        messagebox.showinfo("Weight", f"{kg} kg = {pounds:.2f} lbs")

def bmi_calc():
    h = simpledialog.askfloat("BMI", "Enter height in meters:")
    w = simpledialog.askfloat("BMI", "Enter weight in kg:")
    if h and w:
        bmi = w / (h**2)
        messagebox.showinfo("BMI", f"Your BMI is {bmi:.2f}")

def height_calc():
    cm = simpledialog.askfloat("Height Converter", "Enter height in cm:")
    if cm:
        ft = cm / 30.48
        messagebox.showinfo("Height", f"{cm} cm = {ft:.2f} ft")

def temp_calc():
    c = simpledialog.askfloat("Temperature Converter", "Enter temp in Celsius:")
    if c is not None:
        f = (c * 9/5) + 32
        messagebox.showinfo("Temperature", f"{c}°C = {f:.2f}°F")

def currency_calc():
    amount = simpledialog.askfloat("Currency Converter", "Enter amount in INR:")
    if amount:
        usd = amount * 0.012
        eur = amount * 0.011
        messagebox.showinfo("Currency", f"₹{amount} = ${usd:.2f} / €{eur:.2f}")

def time_calc():
    now = datetime.now().strftime("%H:%M:%S")
    messagebox.showinfo("Time", f"Current Time: {now}")

def calendar_calc():
    today = datetime.now().strftime("%d-%m-%Y")
    messagebox.showinfo("Calendar", f"Today: {today}")

def discount_calc():
    price = simpledialog.askfloat("Discount Calculator", "Enter original price:")
    disc = simpledialog.askfloat("Discount Calculator", "Enter discount %:")
    if price and disc:
        final = price - (price * disc / 100)
        messagebox.showinfo("Discount", f"Final Price = ₹{final:.2f}")

def split_bill():
    total = simpledialog.askfloat("Split Bill", "Enter total amount:")
    people = simpledialog.askinteger("Split Bill", "Number of people:")
    if total and people:
        per_person = total / people
        messagebox.showinfo("Split Bill", f"Each person pays ₹{per_person:.2f}")

def gst_calc():
    price = simpledialog.askfloat("GST Calculator", "Enter base price:")
    gst = simpledialog.askfloat("GST Calculator", "Enter GST %:")
    if price and gst:
        total = price + (price * gst / 100)
        messagebox.showinfo("GST", f"Total Price (with GST) = ₹{total:.2f}")

# -------------------------------
# Stopwatch Page
# -------------------------------
stopwatch_running = False
stopwatch_time = 0

def update_stopwatch():
    global stopwatch_time
    if stopwatch_running:
        stopwatch_time += 1
        stopwatch_label.config(text=f"{stopwatch_time} sec")
        root.after(1000, update_stopwatch)

def start_stopwatch():
    global stopwatch_running
    stopwatch_running = True
    update_stopwatch()

def stop_stopwatch():
    global stopwatch_running
    stopwatch_running = False

def reset_stopwatch():
    global stopwatch_running, stopwatch_time
    stopwatch_running = False
    stopwatch_time = 0
    stopwatch_label.config(text="0 sec")

tk.Label(stopwatch_frame, text="Stopwatch", font=("Arial", 18, "bold"), bg="black", fg="orange").pack(pady=20)
stopwatch_label = tk.Label(stopwatch_frame, text="0 sec", font=("Arial", 20), bg="black", fg="orange")
stopwatch_label.pack(pady=20)

sw_btns = tk.Frame(stopwatch_frame, bg="black")
sw_btns.pack()
tk.Button(sw_btns, text="Start", command=start_stopwatch, bg="black", fg="orange", relief="solid").pack(side="left", padx=10)
tk.Button(sw_btns, text="Stop", command=stop_stopwatch, bg="black", fg="orange", relief="solid").pack(side="left", padx=10)
tk.Button(sw_btns, text="Reset", command=reset_stopwatch, bg="black", fg="orange", relief="solid").pack(side="left", padx=10)

tk.Button(stopwatch_frame, text="← Tools", font=("Arial", 14, "bold"),
          fg="orange", bg="black", relief="solid",
          command=lambda: show_frame(tools_frame)).pack(pady=20)

# -------------------------------
# Timer Page
# -------------------------------
timer_running = False
timer_time = 0

def update_timer():
    global timer_time
    if timer_running and timer_time > 0:
        timer_time -= 1
        mins, secs = divmod(timer_time, 60)
        timer_label.config(text=f"{mins:02}:{secs:02}")
        root.after(1000, update_timer)
    elif timer_time == 0 and timer_running:
        messagebox.showinfo("Timer", "Time’s up!")

def start_timer():
    global timer_time, timer_running
    try:
        mins = int(min_entry.get())
        secs = int(sec_entry.get())
        timer_time = mins * 60 + secs
        timer_running = True
        update_timer()
    except:
        messagebox.showerror("Error", "Enter valid numbers")

def stop_timer():
    global timer_running
    timer_running = False

def reset_timer():
    global timer_running, timer_time
    timer_running = False
    timer_time = 0
    timer_label.config(text="00:00")

tk.Label(timer_frame, text="Timer", font=("Arial", 18, "bold"), bg="black", fg="orange").pack(pady=20)

entry_frame = tk.Frame(timer_frame, bg="black")
entry_frame.pack()
min_entry = tk.Entry(entry_frame, width=5, font=("Arial", 14))
min_entry.pack(side="left", padx=5)
tk.Label(entry_frame, text="min", font=("Arial", 12), bg="black", fg="orange").pack(side="left")

sec_entry = tk.Entry(entry_frame, width=5, font=("Arial", 14))
sec_entry.pack(side="left", padx=5)
tk.Label(entry_frame, text="sec", font=("Arial", 12), bg="black", fg="orange").pack(side="left")

timer_label = tk.Label(timer_frame, text="00:00", font=("Arial", 20), bg="black", fg="orange")
timer_label.pack(pady=20)

tm_btns = tk.Frame(timer_frame, bg="black")
tm_btns.pack()
tk.Button(tm_btns, text="Start", command=start_timer, bg="black", fg="orange", relief="solid").pack(side="left", padx=10)
tk.Button(tm_btns, text="Stop", command=stop_timer, bg="black", fg="orange", relief="solid").pack(side="left", padx=10)
tk.Button(tm_btns, text="Reset", command=reset_timer, bg="black", fg="orange", relief="solid").pack(side="left", padx=10)

tk.Button(timer_frame, text="← Tools", font=("Arial", 14, "bold"),
          fg="orange", bg="black", relief="solid",
          command=lambda: show_frame(tools_frame)).pack(pady=20)

# -------------------------------
# Tools Page
# -------------------------------
tk.Label(tools_frame, text="Tools", font=("Arial", 18, "bold"), bg="black", fg="orange").pack(pady=10)

grid_frame = tk.Frame(tools_frame, bg="black")
grid_frame.pack()

tools = [
    ("🎂", "age", age_calc),
    ("⚖️", "weight", weight_calc),
    ("🧍", "bmi", bmi_calc),
    ("📏", "height", height_calc),
    ("🌡", "temp", temp_calc),
    ("💱", "currency", currency_calc),
    ("⏰", "time", time_calc),
    ("📅", "calendar", calendar_calc),
    ("💲", "discount", discount_calc),
    ("🧾", "split bill", split_bill),
    ("🏷", "gst", gst_calc),
    ("⏱", "stopwatch", lambda: show_frame(stopwatch_frame)),
    ("⏲", "timer", lambda: show_frame(timer_frame))
]

row, col = 0, 0
for icon, name, cmd in tools:
    frame = tk.Frame(grid_frame, bg="black")
    frame.grid(row=row, column=col, padx=20, pady=20)
    btn = tk.Button(frame, text=icon, font=("Arial", 30), bg="black", fg="orange",
                    relief="flat", command=cmd)
    btn.pack()
    tk.Label(frame, text=name, font=("Arial", 10), bg="black", fg="orange").pack()
    col += 1
    if col > 3:
        col = 0
        row += 1

back_btn = tk.Button(tools_frame, text="← Calculator", font=("Arial", 14, "bold"),
                     fg="orange", bg="black", relief="solid",
                     command=lambda: show_frame(calculator_frame))
back_btn.pack(pady=10)

# -------------------------------
# Start
# -------------------------------
show_frame(calculator_frame)
root.mainloop()







