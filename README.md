Aircraft Performance Calculator
Overview
This project is an interactive Jupyter Notebook application that calculates and visualizes aircraft performance metrics as a function of altitude. The metrics include:

Thrust Available (N)
Power Available (MW)
Thrust Required (N)
Power Required (MW)
Excess Thrust (N)
Excess Power (MW)

The application allows users to input a single altitude or multiple altitudes and provides detailed performance data, optionally displayed as a table, along with plots showing how these metrics vary with altitude. The calculations are based on piecewise linear interpolation of data points derived from a realistic chart of aircraft performance at various altitudes.
Data Source
The performance data is based on the following chart values at specific altitudes:



Requirements

Python 3.x
Jupyter Notebook
Required Python libraries:
matplotlib
numpy
ipywidgets
pandas



Installation

Install Python: Ensure you have Python 3.x installed on your system. You can download it from python.org.

Install Jupyter Notebook:
pip install jupyter


Install Required Libraries:
pip install matplotlib numpy ipywidgets pandas


Clone the Repository:
git clone https://github.com/<lex4s>/Aircraft-Performance-Calculator.git
cd Aircraft-Performance-Calculator



Usage

Launch Jupyter Notebook:
jupyter notebook

This will open Jupyter Notebook in your default web browser.

Open the Notebook:

Navigate to the aircraft_performance.ipynb file in the Jupyter Notebook interface and open it.


Interact with the Notebook:

Single Altitude Prediction:
Enter an altitude (in meters) in the "Enter Altitude (meters)" field.
Optionally check "Show as Table?" to display results in a table format.
Click the "Predict for Single Altitude" button to see the performance metrics and a plot.


Multiple Altitudes Prediction:
Enter comma-separated altitudes (e.g., 0, 1000, 5000) in the "Enter Altitudes (comma-separated)" field.
Optionally check "Show as Table?" to display results in a table format.
Click the "Predict for Multiple Altitudes" button to see the results and a plot.

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

The performance data is derived from a realistic chart provided for educational purposes.
Built with Python, Jupyter Notebook, and associated libraries.

