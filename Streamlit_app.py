import streamlit as st
import numpy as np
import pandas as pd

def get_thrust_available(alt):
    """Alright, so we got this thrust, right? Depends on how high we are.
       Like when you're up in the sky, things get a little...thinner. This figures that out."""
    if alt <= 0:
        return 50000 # Ground level, full power, capiche?
    elif alt <= 2000:
        return 50000 - (alt / 2000.0) * 10000 # Startin' to lose a little somethin' as we climb.
    elif alt <= 5000:
        return 40000 - ((alt - 2000) / 3000.0) * 15000 # Okay, now we're gettin' up there, see? Less oomph.
    elif alt <= 8000:
        return 25000 - ((alt - 5000) / 3000.0) * 15000 # Pretty high now, like tryin' to run in a dream.
    elif alt <= 10000:
        return 10000 - ((alt - 8000) / 2000.0) * 5000 # Almost at the top, barely breathin' up here.
    else:
        return 5000 # Way up high, that's all she wrote for the big power.

def get_power_available(alt):
    """Power's the same deal, ya know? Altitude screws with that too. This here's the calculation."""
    if alt <= 0:
        return 20 # Down low, plenty of juice.
    elif alt <= 2000:
        return 20 - (alt / 2000.0) * 4 # Startin' to dip a little.
    elif alt <= 5000:
        return 16 - ((alt - 2000) / 3000.0) * 6 # Notice a pattern here? Higher you go...
    elif alt <= 8000:
        return 10 - ((alt - 5000) / 3000.0) * 6 # Less and less, like my patience with Little Carmine.
    elif alt <= 10000:
        return 4 - ((alt - 8000) / 2000.0) * 2 # Almost nothin' left at this altitude.
    else:
        return 2 # Forget about it.

def get_thrust_required(alt, tas, weight):
    """Now, how much push we actually need? Depends on how fast we're goin', the weight we're luggin', and where we are in the sky. This figures that out...sorta for now."""
    # Listen, this here is just a stand-in, a placeholder, ya hear? Gotta get the real numbers for this later.
    rho = get_air_density(alt) # Gotta know how thick the air is, right?
    return 0.005 * rho * (tas**2) + 0.01 * weight # Speed and weight, they matter. Simple as that...for now.

def get_power_required(alt, tas, weight):
    """Same thing with power we gotta use. Speed, weight, altitude...it all adds up. This is the rough idea."""
    # This ain't the full picture, understand? Needs the real deal equations.
    rho = get_air_density(alt) # Air density, again. Important stuff.
    return (0.005 * rho * (tas**3) + 0.01 * weight * tas) / 1e6 # Speed's got a bigger say here with power. Gotta convert to MW.

def get_air_density(alt):
    """Air's thicker down here, thinner up there. This tells you how much of it there is."""
    # Standard sea level stuff.
    rho_sl = 1.225
    # It thins out as you climb, like my hairline. Simple math.
    return rho_sl * np.exp(-alt / 8400.0)

def calculate_performance(altitude, tas, weight):
    """Alright, put it all together. What we got, what we need, the difference...that's the performance. This spits it out."""
    ta = get_thrust_available(altitude) # What the engine's givin'.
    pa = get_power_available(altitude) # The power we got in the bank.
    tr = get_thrust_required(altitude, tas, weight) # What we gotta push against.
    pr = get_power_required(altitude, tas, weight) # How much juice we're burnin'.
    et = ta - tr # Extra push we got. Good thing.
    ep = pa - pr # Extra power. Also good.
    return {
        'Altitude (m)': altitude,
        'True Airspeed (m/s)': tas,
        'Weight (N)': weight,
        'Thrust Available (N)': ta,
        'Power Available (MW)': pa,
        'Thrust Required (N)': tr,
        'Power Required (MW)': pr,
        'Excess Thrust (N)': et,
        'Excess Power (MW)': ep
    }

st.title("Aircraft Performance Calculator")
st.title("Amr Ashraf Mohamed") # Gotta put your name on the thing.

# Inputs, ya know? Gotta get the numbers from the user.
true_airspeed = st.number_input("Enter True Airspeed (m/s):", min_value=0.0, step=10.0, value=100.0)
weight = st.number_input("Enter Aircraft Weight (N):", min_value=0.0, step=1000.0, value=10000.0)

# Single altitude, one shot.
st.header("Single Altitude Prediction")
altitude = st.slider("Enter Altitude (meters):", 0, 12000, 0, 100)
if st.button("Calculate Single Altitude"):
    results = calculate_performance(altitude, true_airspeed, weight)
    st.write("Results:")
    for key, value in results.items():
        st.write(f"{key}: {value:.1f}")
    if st.checkbox("Show as Table"):
        df = pd.DataFrame([results])
        st.table(df)

# Bunch of altitudes, see the trend.
st.header("Multiple Altitudes Prediction")
altitudes_input = st.text_input("Enter Altitudes (comma-separated, e.g., 0, 1000, 5000):")
if st.button("Calculate Multiple Altitudes"):
    if altitudes_input.strip():
        try:
            altitudes = [float(alt.strip()) for alt in altitudes_input.split(',')]
            altitudes = [alt for alt in altitudes if 0 <= alt <= 12000]
            if altitudes:
                all_results = [calculate_performance(alt, true_airspeed, weight) for alt in altitudes]
                st.write("Results:")
                df = pd.DataFrame(all_results)
                st.table(df)
            else:
                st.write("All altitudes must be between 0 and 12000 meters. Youse guys hear me?")
        except ValueError:
            st.write("C'mon, comma-separated numbers, huh?")