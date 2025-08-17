# 💱 Currency Converter

A simple **Flask Web Application** to convert currencies using real-time exchange rates from the [Fixer.io API](https://fixer.io/).

---

## 🚀 Features

- Convert between 32 different currencies
- Get real-time exchange rates
- User-friendly and responsive interface

---

## ⚙️ Technologies Used

- Python
- Flask
- HTML, CSS (Bootstrap 4)
- Requests (for API calls)

---

## 📦 How to Run

1. **Install dependencies**
    ```bash
    pip install flask requests
    ```

2. **Navigate to the project folder**
    ```bash
    cd Flask-CurrencyConverter
    ```

3. **Run the Flask app**
    ```bash
    python app.py
    ```

4. **Open in your browser**
    ```
    http://127.0.0.1:5000/
    ```

---

## 🖼️ Screenshots

![Currency Converter Screenshot](screenshots/output.png)

---

## 💡 Notes

- Make sure you have a valid **Fixer.io API key** in `app.py` (`api_key` variable) before running the application.

- The result will only display after entering the amount, selecting currencies, and clicking **Convert**.
