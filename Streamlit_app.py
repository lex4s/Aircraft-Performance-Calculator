import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_thrust_available(alt):
    if alt <= 0:
        return 50000
    elif alt <= 2000:
        return 50000 - (alt / 2000.0) * 10000
    elif alt <= 5000:
        return 40000 - ((alt - 2000) / 3000.0) * 15000
    elif alt <= 8000:
        return 25000 - ((alt - 5000) / 3000.0) * 15000
    elif alt <= 10000:
        return 10000 - ((alt - 8000) / 2000.0) * 5000
    else:
        return 5000

def get_power_available(alt):
    if alt <= 0:
        return 20
    elif alt <= 2000:
        return 20 - (alt / 2000.0) * 4
    elif alt <= 5000:
        return 16 - ((alt - 2000) / 3000.0) * 6
    elif alt <= 8000:
        return 10 - ((alt - 5000) / 3000.0) * 6
    elif alt <= 10000:
        return 4 - ((alt - 8000) / 2000.0) * 2
    else:
        return 2

def get_air_density(alt):
    rho_sl = 1.225
    return rho_sl * np.exp(-alt / 8400.0)

def knots_to_ms(knots):
    return knots * 0.514444

def get_thrust_required(alt, tas_knots, weight):
    tas = knots_to_ms(tas_knots)
    rho = get_air_density(alt)
    return 0.005 * rho * (tas**2) + 0.01 * weight

def get_power_required(alt, tas_knots, weight):
    tas = knots_to_ms(tas_knots)
    rho = get_air_density(alt)
    return (0.005 * rho * (tas**3) + 0.01 * weight * tas) / 1e6

def calculate_performance(altitude, tas_knots, weight):
    ta = get_thrust_available(altitude)
    pa = get_power_available(altitude)
    tr = get_thrust_required(altitude, tas_knots, weight)
    pr = get_power_required(altitude, tas_knots, weight)
    et = ta - tr
    ep = pa - pr
    return {
        'Altitude (m)': altitude,
        'Thrust Available (N)': ta,
        'Thrust Required (N)': tr,
        'Excess Thrust (N)': et,
        'Power Available (MW)': pa,
        'Power Required (MW)': pr,
        'Excess Power (MW)': ep
    }


st.title("Aircraft Performance Calculator ✈️")
st.title("By Amr Ashraf Mohamed")

true_airspeed_knots = st.number_input("Enter True Airspeed (knots):", min_value=0.0, step=10.0, value=777.0)
weight = st.number_input("Enter Aircraft Weight (N):", min_value=0.0, step=1000.0, value=900000.0)

altitude_input = st.text_input("Enter Altitudes (comma-separated, e.g. 0,2000,5000,8000):", "0, 2000, 5000, 8000, 10000")

if st.button("Calculate Performance"):
    try:
        altitudes = [float(a.strip()) for a in altitude_input.split(",")]
        results = []
        for alt in altitudes:
            result = calculate_performance(alt, true_airspeed_knots, weight)
            results.append(result)

        df = pd.DataFrame(results)
        df.set_index("Altitude (m)", inplace=True)

        st.subheader("📊 Performance Matrix Table")
        st.dataframe(df.style.format("{:.2f}"))

        st.subheader("📈 Thrust & Power vs Altitude")

        fig, ax = plt.subplots(2, 1, figsize=(8, 8))

        ax[0].plot(df.index, df['Thrust Available (N)'], marker='o', label='Thrust Available')
        ax[0].plot(df.index, df['Thrust Required (N)'], marker='o', label='Thrust Required')
        ax[0].set_ylabel("Thrust (N)")
        ax[0].set_xlabel("Altitude (m)")
        ax[0].legend()
        ax[0].grid(True)

        ax[1].plot(df.index, df['Power Available (MW)'], marker='s', label='Power Available')
        ax[1].plot(df.index, df['Power Required (MW)'], marker='s', label='Power Required')
        ax[1].set_ylabel("Power (MW)")
        ax[1].set_xlabel("Altitude (m)")
        ax[1].legend()
        ax[1].grid(True)

        st.pyplot(fig)

    except ValueError:
        st.error("Please enter valid altitudes separated by commas.")

