import streamlit as st
import numpy as np
from scipy.optimize import curve_fit

# Chart data
chart_data = {
    0: {"TA": 50000, "PA": 20e6, "TR": 10000, "PR": 4e6, "excess_thrust": 40000, "excess_power": 16e6},
    2000: {"TA": 40000, "PA": 16e6, "TR": 9800, "PR": 3.9e6, "excess_thrust": 30200, "excess_power": 12.1e6},
    5000: {"TA": 25000, "PA": 10e6, "TR": 9500, "PR": 3.8e6, "excess_thrust": 15500, "excess_power": 6.2e6},
    8000: {"TA": 10000, "PA": 4e6, "TR": 9300, "PR": 3.7e6, "excess_thrust": 700, "excess_power": 0.3e6},
    10000: {"TA": 5000, "PA": 2e6, "TR": 9200, "PR": 3.6e6, "excess_thrust": -4200, "excess_power": -1.6e6}
}

default_weight = 50000.0  # N
default_wing_span = 7.32  # m
default_aspect_ratio = 7.0
default_oswald_efficiency = 0.8

# Function to estimate air density based on altitude
def get_air_density(altitude):
    rho_0 = 1.225
    return rho_0 * np.exp(-altitude / 8000)

# Streamlit UI - Title and Inputs
st.title("Aerodynamic Calculator")
st.title("**By Amr Ashraf**")

st.header("Input Parameters")
reference_velocity = st.number_input("Reference Velocity for CD_parasite Fit (m/s)", min_value=100.0, max_value=3000.0, value=400.0, step=10.0)
altitude = st.slider("Altitude (meters)", 0, 10000, 0, step=100)
weight = st.number_input("Weight (N)", min_value=10000.0, max_value=10000000.0, value=default_weight, step=1000.0)
velocity = st.number_input("Velocity (m/s)", min_value=100.0, max_value=3000.0, value=reference_velocity, step=10.0)
wing_span = st.number_input("Wing Span (m)", min_value=1.0, max_value=50.0, value=default_wing_span, step=0.1)
aspect_ratio = st.number_input("Aspect Ratio (AR)", min_value=1.0, max_value=20.0, value=default_aspect_ratio, step=0.1)
oswald_efficiency = st.slider("Oswald Efficiency Factor (e)", 0.7, 0.9, default_oswald_efficiency, step=0.01)

# Wing Area
S = (wing_span ** 2) / aspect_ratio

# Prepare CD_parasite values for curve fit
altitudes_chart = sorted(chart_data.keys())
cd_parasite_values = []

for alt in altitudes_chart:
    rho = get_air_density(alt)
    TR_chart = chart_data[alt]["TR"]
    dynamic_pressure = 0.5 * rho * (reference_velocity ** 2)
    CL = default_weight / (dynamic_pressure * S)
    CD_induced = (CL ** 2) / (np.pi * aspect_ratio * oswald_efficiency)
    CD_total_required = TR_chart / (dynamic_pressure * S)
    CD_parasite = CD_total_required - CD_induced
    cd_parasite_values.append(max(0, CD_parasite))

# Polynomial fit function
def cd_parasite_model(h, a, b, c):
    return a * h**2 + b * h + c

# Curve fit
popt, pcov = curve_fit(cd_parasite_model, altitudes_chart, cd_parasite_values, p0=[0, 0, 0.02])

# Function to get CD_parasite at any altitude
def get_cd_parasite(altitude):
    return max(0.0001, cd_parasite_model(altitude, *popt))

# Calculate air density
rho = get_air_density(altitude)

# Calculate CL
dynamic_pressure = 0.5 * rho * velocity ** 2
CL = weight / (dynamic_pressure * S)

# Calculate drag coefficients
CD_induced = (CL ** 2) / (np.pi * aspect_ratio * oswald_efficiency)
CD_parasite_calculated = get_cd_parasite(altitude)
CD_total = CD_parasite_calculated + CD_induced

# Total Drag and Power Required
total_drag = dynamic_pressure * S * CD_total
power_required_calculated = total_drag * velocity

# Interpolation for Available Thrust and Power
def interpolate_chart(altitude, param):
    altitudes = sorted(chart_data.keys())
    values = [chart_data[alt][param] for alt in altitudes]
    if altitude <= altitudes[0]: return values[0]
    if altitude >= altitudes[-1]: return values[-1]
    for i in range(len(altitudes) - 1):
        if altitudes[i] <= altitude <= altitudes[i + 1]:
            frac = (altitude - altitudes[i]) / (altitudes[i + 1] - altitudes[i])
            return values[i] + frac * (values[i + 1] - values[i])
    return None

TA = interpolate_chart(altitude, "TA")
PA = interpolate_chart(altitude, "PA")
TR_chart_ref = interpolate_chart(altitude, "TR")
PR_chart_ref = interpolate_chart(altitude, "PR")

# Excess values
excess_thrust = TA - total_drag
excess_power = PA - power_required_calculated

# Display Results
st.header("Calculated Parameters")
st.write(f"**Lift Coefficient (C_L)**: {CL:.4f}")
st.write(f"**Induced Drag Coefficient (C_D_induced)**: {CD_induced:.4f}")
st.write(f"**Parasite Drag Coefficient (C_D_parasite)**: {CD_parasite_calculated:.4f}")
st.write(f"**Total Drag Coefficient (C_D)**: {CD_total:.4f}")
st.write(f"**Weight (W)**: {weight:.1f} N")
st.write(f"**Velocity (V)**: {velocity:.1f} m/s")
st.write(f"**Wing Area (S)**: {S:.2f} m²")
st.write(f"**Aspect Ratio (AR)**: {aspect_ratio:.2f}")

st.header("Thrust and Power Results")
st.write(f"**Thrust Required (Calculated)**: {total_drag:.1f} N")
st.write(f"**Thrust Required (from Chart at this Altitude)**: {TR_chart_ref:.1f} N")
st.write(f"**Power Required (Calculated)**: {power_required_calculated/1e6:.2f} MW")
st.write(f"**Power Required (from Chart at this Altitude)**: {PR_chart_ref/1e6:.2f} MW")
st.write(f"**Thrust Available (Interpolated)**: {TA:.1f} N")
st.write(f"**Power Available (Interpolated)**: {PA/1e6:.2f} MW")
st.write(f"**Excess Thrust**: {excess_thrust:.1f} N")
st.write(f"**Excess Power**: {excess_power/1e6:.2f} MW")
