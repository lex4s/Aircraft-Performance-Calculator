# ✈️ Aircraft Performance Calculator

A lightweight, interactive web application for calculating key aircraft performance metrics across various altitudes. Built with **Streamlit**, it visualizes how thrust and power parameters behave in different flight conditions.

## Try it from here, https://aircraftpcl.streamlit.app/
---

## 📖 Overview

This project computes and plots aircraft performance metrics such as:
- **Thrust Available (N)**
- **Thrust Required (N)**
- **Excess Thrust (N)**
- **Power Available (MW)**
- **Power Required (MW)**
- **Excess Power (MW)**

It uses piecewise linear interpolation to estimate performance values based on user-defined altitudes.

---

## 🎯 Features

- 📊 **Real-time plotting** of thrust and power curves vs. altitude  
- 🔢 **Single and multiple altitude predictions**  
- 📋 **Tabular display of results**  
- 🖥️ **Runs entirely in your browser** using Streamlit  

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** (for the web interface)
- **Matplotlib** (for graph plotting)
- **NumPy**
- **Pandas**

---

## 🚀 Installation & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/lex4s/Aircraft-Performance-Calculator.git
   cd Aircraft-Performance-Calculator
   ```

2. **(Optional) Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

---

## 📊 How It Works

- Adjust the **altitude slider** or enter multiple altitudes.
- Click **Calculate** to get performance metrics.
- View results in both tabular and graphical forms.
- Graphs show:
  - Thrust Available / Required and Excess Thrust  
  - Power Available / Required and Excess Power  

---

## 📌 Project Status

✅ **Current**: Working, tested, and clean interface.  
🔜 **Planned**:
- Aircraft database integration  
- Export to CSV / PDF  
- Configurable performance profiles  

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 📬 Contact

**[Amr Ashraf]** – [elhadidy169@gmail.com]  
GitHub: [https://github.com/lex4s](https://github.com/lex4s)

---
