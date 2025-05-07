import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def get_thrust_available(alt):
    """Calculate thrust available (N) based on altitude (m) using piecewise linear interpolation."""
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
    """Calculate power available (MW) based on altitude (m) using piecewise linear interpolation."""
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

def get_thrust_required(alt):
    """Calculate thrust required (N) based on altitude (m) using piecewise linear interpolation."""
    if alt <= 0:
        return 10000
    elif alt <= 2000:
        return 10000 - (alt / 2000.0) * 200
    elif alt <= 5000:
        return 9800 - ((alt - 2000) / 3000.0) * 300
    elif alt <= 8000:
        return 9500 - ((alt - 5000) / 3000.0) * 200
    elif alt <= 10000:
        return 9300 - ((alt - 8000) / 2000.0) * 100
    else:
        return 9200

def get_power_required(alt):
    """Calculate power required (MW) based on altitude (m) using piecewise linear interpolation."""
    if alt <= 0:
        return 4
    elif alt <= 2000:
        return 4 - (alt / 2000.0) * 0.1
    elif alt <= 5000:
        return 3.9 - ((alt - 2000) / 3000.0) * 0.1
    elif alt <= 8000:
        return 3.8 - ((alt - 5000) / 3000.0) * 0.1
    elif alt <= 10000:
        return 3.7 - ((alt - 8000) / 2000.0) * 0.1
    else:
        return 3.6

def calculate_performance(altitude):
    """Calculate all performance metrics for a given altitude."""
    ta = get_thrust_available(altitude)
    pa = get_power_available(altitude)
    tr = get_thrust_required(altitude)
    pr = get_power_required(altitude)
    et = ta - tr
    ep = pa - pr
    return {
        'Altitude (m)': altitude,
        'Thrust Available (N)': ta,
        'Power Available (MW)': pa,
        'Thrust Required (N)': tr,
        'Power Required (MW)': pr,
        'Excess Thrust (N)': et,
        'Excess Power (MW)': ep
    }

st.title("Aircraft Performance Calculator")

# Single Altitude Prediction
st.header("Single Altitude Prediction")
altitude = st.slider("Enter Altitude (meters):", 0, 12000, 0, 100)
if st.button("Calculate Single Altitude"):
    results = calculate_performance(altitude)
    st.write("Results:")
    for key, value in results.items():
        st.write(f"{key}: {value:.1f}")
    if st.checkbox("Show as Table"):
        df = pd.DataFrame([results])
        st.table(df)

    # Plotting
    alt_plot = np.linspace(0, 12000, 100)
    ta_plot = np.array([get_thrust_available(a) for a in alt_plot])
    pa_plot = np.array([get_power_available(a) for a in alt_plot])
    tr_plot = np.array([get_thrust_required(a) for a in alt_plot])
    pr_plot = np.array([get_power_required(a) for a in alt_plot])
    et_plot = ta_plot - tr_plot
    ep_plot = pa_plot - pr_plot

    fig, axs = plt.subplots(1, 2, figsize=(14, 6))
    fig.suptitle(f'Performance vs. Altitude (Current Altitude: {altitude:.0f} m)', fontsize=16)

    axs[0].plot(alt_plot, ta_plot, label='Thrust Available (N)')
    axs[0].plot(alt_plot, tr_plot, label='Thrust Required (N)')
    axs[0].plot(alt_plot, et_plot, label='Excess Thrust (N)')
    axs[0].scatter([0, 2000, 5000, 8000, 10000], [50000, 40000, 25000, 10000, 5000], color='red', marker='o', label='Data Points')
    axs[0].axvline(altitude, color='gray', linestyle='--', label=f'Current Altitude')
    axs[0].set_xlabel('Altitude (m)')
    axs[0].set_ylabel('Thrust (N)')
    axs[0].legend()
    axs[0].grid(True)
    axs[0].axhline(0, color='black', linestyle='-', linewidth=0.5)

    axs[1].plot(alt_plot, pa_plot, label='Power Available (MW)')
    axs[1].plot(alt_plot, pr_plot, label='Power Required (MW)')
    axs[1].plot(alt_plot, ep_plot, label='Excess Power (MW)')
    axs[1].scatter([0, 2000, 5000, 8000, 10000], [20, 16, 10, 4, 2], color='red', marker='o', label='Data Points')
    axs[1].axvline(altitude, color='gray', linestyle='--', label=f'Current Altitude')
    axs[1].set_xlabel('Altitude (m)')
    axs[1].set_ylabel('Power (MW)')
    axs[1].legend()
    axs[1].grid(True)
    axs[1].axhline(0, color='black', linestyle='-', linewidth=0.5)

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    st.pyplot(fig)

# Multiple Altitudes Prediction
st.header("Multiple Altitudes Prediction")
altitudes_input = st.text_input("Enter Altitudes (comma-separated, e.g., 0, 1000, 5000):")
if st.button("Calculate Multiple Altitudes"):
    if altitudes_input.strip():
        try:
            altitudes = [float(alt.strip()) for alt in altitudes_input.split(',')]
            altitudes = [alt for alt in altitudes if 0 <= alt <= 12000]
            if altitudes:
                all_results = [calculate_performance(alt) for alt in altitudes]
                st.write("Results:")
                df = pd.DataFrame(all_results)
                st.table(df)

                alt_plot = np.linspace(0, 12000, 100)
                ta_plot = np.array([get_thrust_available(a) for a in alt_plot])
                pa_plot = np.array([get_power_available(a) for a in alt_plot])
                tr_plot = np.array([get_thrust_required(a) for a in alt_plot])
                pr_plot = np.array([get_power_required(a) for a in alt_plot])

                fig, axs = plt.subplots(1, 2, figsize=(14, 6))
                fig.suptitle('Performance for Multiple Altitudes', fontsize=16)

                axs[0].plot(alt_plot, ta_plot, label='Thrust Available (N)')
                axs[0].plot(alt_plot, tr_plot, label='Thrust Required (N)')
                axs[0].scatter(altitudes, [get_thrust_available(a) for a in altitudes], color='blue', marker='o', label='Input Altitudes')
                axs[0].set_xlabel('Altitude (m)')
                axs[0].set_ylabel('Thrust (N)')
                axs[0].legend()
                axs[0].grid(True)
                axs[0].axhline(0, color='black', linestyle='-', linewidth=0.5)

                axs[1].plot(alt_plot, pa_plot, label='Power Available (MW)')
                axs[1].plot(alt_plot, pr_plot, label='Power Required (MW)')
                axs[1].scatter(altitudes, [get_power_available(a) for a in altitudes], color='blue', marker='o', label='Input Altitudes')
                axs[1].set_xlabel('Altitude (m)')
                axs[1].set_ylabel('Power (MW)')
                axs[1].legend()
                axs[1].grid(True)
                axs[1].axhline(0, color='black', linestyle='-', linewidth=0.5)

                plt.tight_layout(rect=[0, 0.03, 1, 0.95])
                st.pyplot(fig)
            else:
                st.write("All altitudes must be between 0 and 12000 meters.")
        except ValueError:
            st.write("Please enter altitudes as comma-separated numbers.")
