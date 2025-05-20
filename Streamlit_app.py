import streamlit as st
import math

# --- Constants ---
# Standard air crap at sea level
rho_sl = 1.225      # kg/m^3

# Kinda how high the air thins out. It's approximate, don't freak out.
h_scale = 8500.0      # m

# Gravity... yeah, it pulls stuff down. Not directly used right now, but good to know.
g = 9.80665          # m/s^2

# --- Helper Function ---
def calc_rho(alt_m: float) -> float:
    """Figure out how thick the air is way up there using a simple model."""
    return rho_sl * math.exp(-alt_m / h_scale)

# --- Streamlit App Starts Here ---
st.title("Aircraft Performance Quick Check")
st.write("Punch in the deets, see what this bird's doing.")

st.subheader("Input Parameters")
st.write("Tell me about the plane and the situation.")

# Layout inputs side-by-side
col1, col2 = st.columns(2)

with col1:
    # How much lift the wing's making right now
    cl = st.number_input("Coefficient of Lift (CL)", min_value=0.001, max_value=2.5, value=0.3, format="%.3f")
    # How much drag is fighting ya
    cd = st.number_input("Coefficient of Drag (CD)", min_value=0.001, max_value=1.0, value=0.03, format="%.4f")
    # Wingtip to wingtip distance
    span_m = st.number_input("Wing Span (m)", min_value=0.1, value=10.0, format="%.2f")
    # Wing shape-ish parameter
    ar = st.number_input("Aspect Ratio (AR)", min_value=0.1, value=7.0, format="%.2f")

with col2:
    # How heavy this beast is (in Newtons, not pounds, 'cause we're fancy)
    weight_n = st.number_input("Aircraft Weight (N)", min_value=1.0, value=10000.0, format="%.2f")
    # How fast it's hauling ass (meters per second)
    v_mps = st.number_input("Velocity (m/s)", min_value=0.1, value=50.0, format="%.2f")
    # How high off the ground it is
    alt_m = st.number_input("Altitude (m)", min_value=0.0, value=1000.0, format="%.1f")
    # Max grunt the engine gives ya parked at sea level
    thrust_sl_n = st.number_input("Max Static Thrust (Sea Level, N)", min_value=0.1, value=2500.0, format="%.2f")

st.markdown("---") # Little line to break things up

# --- Calculations ---
# Okay, time to crunch some numbers based on your inputs.

# Air density at this altitude
rho = calc_rho(alt_m)

# Get the wing area. If AR is zero you're doing something wrong, but the input widget handles that.
wing_area = span_m**2 / ar # S = b^2 / AR

# That force of smacking into the air
q = 0.5 * rho * v_mps**2 # Dynamic pressure

# Total lift the wings are generating based on CL
lift_n = q * wing_area * cl # L = q * S * CL

# Drag, man. That's the thrust you gotta fight.
thrust_req_n = q * wing_area * cd # Thrust Required = Drag = q * S * CD

# Power needed just to push through the air at this speed
power_req_w = thrust_req_n * v_mps # Pr = Tr * V

# Simple model for how much thrust the engine is giving you up here (scales with density)
thrust_avail_n = thrust_sl_n * (rho / rho_sl)

# Engine power output at this speed
power_avail_w = thrust_avail_n * v_mps # Pa = Ta * V

# How much extra thrust you got left over for climbing or speeding up
excess_thrust_n = thrust_avail_n - thrust_req_n

# Leftover power for getting places faster or higher
excess_power_w = power_avail_w - power_req_w


# --- Output Results ---
st.subheader("Calculated Numbers")
st.write("Here's the lowdown based on what you told me.")

st.write(f"Air Density up at {alt_m:.1f} m: **{rho:.3f}** kg/m³")
st.write(f"Wing 'Footprint' Area (S): **{wing_area:.2f}** m²")
st.write(f"Air-Smacking Force (Dynamic Pressure, q): **{q:.2f}** Pa")

st.subheader("Thrust & Power Situation")

# Display the key stuff using some fancy boxes
colA, colB, colC = st.columns(3)

with colA:
    st.metric("Thrust Required (Tr)", f"{thrust_req_n:.2f} N")
    st.metric("Power Required (Pr)", f"{power_req_w:.2f} W")

with colB:
    st.metric("Thrust Available (Ta)", f"{thrust_avail_n:.2f} N")
    st.metric("Power Available (Pa)", f"{power_avail_w:.2f} W")

with colC:
    st.metric("Excess Thrust (Te)", f"{excess_thrust_n:.2f} N")
    st.metric("Excess Power (Pe)", f"{excess_power_w:.2f} W")


st.subheader("Lift vs. Weight Check")
st.write("So, is this thing flying level or not?")
st.write(f"What the wings are putting out (Lift): **{lift_n:.2f}** N")
st.write(f"What the plane weighs (Weight): **{weight_n:.2f}** N")

# Check if Lift is close to Weight (within 1%)
# Don't divide by zero if somehow weight is zero
lift_weight_diff_pct = abs(lift_n - weight_n) / weight_n * 100 if weight_n > 0 else float('inf')

if lift_weight_diff_pct < 1.0: # Close enough for government work
    st.info("Calculated Lift is pretty much equal to Weight. Looks like steady, level flight.")
elif lift_n > weight_n:
    st.warning("Calculated Lift is more than Weight. This bird is pulling up or climbing.")
else:
    st.warning("Calculated Lift is less than Weight. Uh oh, it's headed down or descending.")

st.caption("Heads up: The Thrust/Power required numbers are based on the drag calculated at the CL/CD you gave me, not necessarily the exact thrust needed to perfectly balance forces if Lift isn't equal to Weight.")
