# 🧮 Smart Calculator (Tkinter Multi-Tool App)

A modern **multi-functional calculator desktop application** built using Python and Tkinter.
This app combines a calculator with useful daily tools like BMI calculator, currency converter, stopwatch, timer, and more — all in one place.

---

## 🚀 Features

### 🔢 Calculator

* Basic arithmetic operations (+, −, ×, ÷)
* Decimal support
* Clear (C) and Backspace (⌫)
* Calculation history (last 10 entries)

### 🧰 Tools Included

* 🎂 Age Calculator
* ⚖️ Weight Converter (kg → lbs)
* 🧍 BMI Calculator
* 📏 Height Converter (cm → ft)
* 🌡 Temperature Converter (°C → °F)
* 💱 Currency Converter (INR → USD/EUR)
* ⏰ Current Time Viewer
* 📅 Calendar (Today's Date)
* 💲 Discount Calculator
* 🧾 Split Bill Calculator
* 🏷 GST Calculator

### ⏱ Time Utilities

* Stopwatch (Start / Stop / Reset)
* Timer (Custom minutes & seconds)

---

## 🖥️ Tech Stack

* **Python 3**
* **Tkinter (GUI Framework)**
* Standard Libraries:

  * `datetime`
  * `tkinter.messagebox`
  * `tkinter.simpledialog`

---

## 📂 Project Structure

```
smart-calculator/
│
├── main.py        # Main application file
├── README.md      # Project documentation
```

---

## ⚙️ Installation & Setup

1. **Clone the repository**

```bash
git clone https://github.com/your-username/smart-calculator.git
cd smart-calculator
```

2. **Run the application**

```bash
python main.py
```

---

## 🧠 How It Works

* The app uses **multiple frames** to switch between pages (Calculator, Tools, Stopwatch, Timer).
* Button clicks dynamically update the input field.
* Tools use pop-up dialogs for input and results.
* Timer and stopwatch use `after()` method for real-time updates.

---

## ⚠️ Notes

* Currency conversion uses **fixed rates (approximate)**.
* Calculator uses `eval()` (can be improved for safety).
* Designed for **desktop use only**.

---

## 🔮 Future Improvements

* Scientific calculator (sin, cos, log, etc.)
* Dark/Light theme toggle
* Keyboard input support
* Save history to file
* Live currency API integration
* Mobile app version (Kivy / Flutter)

---

## 🤝 Contributing

Feel free to fork this repo and improve it!
Pull requests are welcome.

---

## 📄 License

This project is open-source and available under the MIT License.

---

⭐ If you like this project, consider giving it a star!
