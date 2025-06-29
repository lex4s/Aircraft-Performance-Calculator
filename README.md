
# ✈️ Aircraft Performance Calculator

An interactive and accurate web application for calculating essential aircraft performance metrics across different altitudes and speeds. Powered by **Streamlit**, it now integrates advanced aerodynamic modeling with user-defined aircraft parameters for a deeper and more dynamic analysis.

👉 **Check it out live:** [here/](https://aerocalc.streamlit.app/)

---

## 📖 Overview   
   
This project precisely computes key aircraft performance parameters, factoring in real-time user inputs for **True Airspeed**, **Weight**, **Wing Span**, **Aspect Ratio**, and **Oswald Efficiency Factor**. It dynamically evaluates:

- **Thrust Available (N)**
- **Thrust Required (N)**
- **Excess Thrust (N)**
- **Power Available (MW)**
- **Power Required (MW)**
- **Excess Power (MW)**
- **Lift Coefficient (C_L)**
- **Induced Drag Coefficient (C_D_induced)**
- **Parasite Drag Coefficient (C_D_parasite)**
- **Total Drag Coefficient (C_D)**
   
It uses **polynomial fitting** to estimate Parasite Drag Coefficient as a function of altitude based on empirical chart data, offering refined accuracy across varying altitudes.

---

## 🎯 Features

- 🔢 **Real-Time Performance Predictions:** Adjust altitude, speed, weight, and aerodynamic parameters on the fly.
- 📈 **Polynomial Parasite Drag Modeling:** Calculates C_D_parasite from altitude using a curve-fitted model.
- ⚙️ **Detailed Aerodynamic Breakdown:** Live display of lift, drag coefficients, and induced vs parasite drag contributions.
- 🔍 **Comparison with Reference Chart Values:** See how your calculated Thrust and Power Required stack up against empirical chart data.
- 🖥️ **Seamless Browser Operation:** All computations and visualizations run smoothly within your browser via Streamlit.

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit**
- **NumPy**
- **SciPy**

---

## 🚀 Installation & Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/lex4s/Aircraft-Performance-Calculator.git
   cd Aircraft-Performance-Calculator
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   streamlit run app.py
   ```
##### Developed by Amr Ashraf
