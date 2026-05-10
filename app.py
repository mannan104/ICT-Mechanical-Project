import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="centered"
)

# Title
st.title("⚙️ Mechanical Unit Converter and Material Density Checker")

# Student Information
st.markdown("### 👨‍🎓 Developed By")
st.write("**Name:** Abdul Mannan")
st.write("**Roll Number:** 25-ME-55")

st.divider()

# =========================
# UNIT CONVERTER
# =========================

st.header("🔄 Unit Converter")

conversion_type = st.selectbox(
    "Select Conversion Type",
    ["Length", "Temperature", "Pressure"]
)

# Length Conversion
if conversion_type == "Length":

    meter = st.number_input("Enter value in meters")

    centimeter = meter * 100
    millimeter = meter * 1000
    feet = meter * 3.28084

    st.success(f"Centimeters: {centimeter:.2f} cm")
    st.success(f"Millimeters: {millimeter:.2f} mm")
    st.success(f"Feet: {feet:.2f} ft")

# Temperature Conversion
elif conversion_type == "Temperature":

    celsius = st.number_input("Enter temperature in Celsius")

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
    st.success(f"Kelvin: {kelvin:.2f} K")

# Pressure Conversion
elif conversion_type == "Pressure":

    pascal = st.number_input("Enter pressure in Pascal")

    kpa = pascal / 1000
    bar = pascal / 100000
    psi = pascal * 0.000145038

    st.success(f"kPa: {kpa:.4f} kPa")
    st.success(f"Bar: {bar:.6f} bar")
    st.success(f"PSI: {psi:.4f} psi")

st.divider()

# =========================
# DENSITY CHECKER
# =========================

st.header("🧱 Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Cast Iron": 7200
}

material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

density = materials[material]

st.info(f"Density of {material}: {density} kg/m³")

st.divider()

st.caption("Made with Streamlit 🚀")
