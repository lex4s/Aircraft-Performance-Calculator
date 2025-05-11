# ✈️ Aircraft Performance Calculator

A sleek, interactive web application engineered for precise calculation of essential aircraft performance metrics across varying altitudes. Powered by **Streamlit**, this tool now incorporates user-defined True Airspeed and Weight, offering a more nuanced analysis of flight dynamics.

## Check it out here, https://aircraftpcl.streamlit.app/
---

## 📖 Overview

This project meticulously computes critical aircraft performance metrics, now enhanced with True Airspeed and Weight considerations:
- **Thrust Available (N)**
- **Thrust Required (N)**
- **Excess Thrust (N)**
- **Power Available (MW)**
- **Power Required (MW)**
- **Excess Power (MW)**

It leverages piecewise linear interpolation to accurately estimate performance values based on user-specified altitudes, True Airspeed, and Aircraft Weight.

---

## 🎯 Features

- 🔢 **Comprehensive Single and Multiple Altitude Predictions:** Analyze performance at specific altitudes or across a range.
- ⚙️ **Integrated True Airspeed and Weight Inputs:** Achieve more precise calculations by factoring in these crucial parameters.
- 📋 **Clear Tabular Display of Results:** Review all calculated metrics in an organized, easy-to-understand table.
- 🖥️ **Seamless In-Browser Operation:** Runs smoothly within your web browser, thanks to Streamlit.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** (for the intuitive web interface)
- **NumPy** (for efficient numerical operations)
- **Pandas** (for structured data handling and tabular displays)

---

## 🚀 Installation & Run

1. **Clone the repository**
   ```bash
   git clone [https://github.com/lex4s/Aircraft-Performance-Calculator.git](https://github.com/lex4s/Aircraft-Performance-Calculator.git)
   cd Aircraft-Performance-Calculator
