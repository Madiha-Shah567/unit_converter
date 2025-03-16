import streamlit as st

# Page Configuration
st.set_page_config(page_title="Unit Converter", page_icon="⚖", layout="centered")

# Custom CSS for Styling
st.markdown("""
    <style>
        h1 { text-align: center; color: #4CAF50; }
        div.stButton > button {
            background-color: #4CAF50; color: white; font-size: 18px; padding: 10px; border-radius: 10px;
        }
        .stSelectbox, .stNumberInput { text-align: center; }
    </style>
""", unsafe_allow_html=True)

# Heading
st.markdown("<h1>Unit Converter</h1>", unsafe_allow_html=True)

# Unit Conversion Logic
def convert_units(value, from_unit, to_unit, category):
    conversion_factors = {
        "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Mile": 0.000621371},
        "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
        "Temperature": {"Celsius": 1, "Fahrenheit": lambda c: (c * 9/5) + 32, "Kelvin": lambda c: c + 273.15}
    }
    
    units = conversion_factors[category]
    if from_unit in units and to_unit in units:
        if callable(units[to_unit]):  # If it's a function (Temperature)
            return units[to_unit](value)  
        return value * (units[to_unit] / units[from_unit])  # Length or Weight Conversion
    return None  

# UI Elements
category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])

# Define the units based on the selected category
if category == "Length":
    units = ["Meter", "Kilometer", "Centimeter", "Millimeter", "Mile"]
elif category == "Weight":
    units = ["Kilogram", "Gram", "Pound", "Ounce"]
else:  # Temperature
    units = ["Celsius", "Fahrenheit", "Kelvin"]

# Selectboxes for From and To units
from_unit = st.selectbox("From", units)
to_unit = st.selectbox("To", units)

# Number input for value
value = st.number_input("Enter Value", min_value=0.0, format="%0.2f")

# Conversion Button
if st.button("Convert"):
    result = convert_units(value, from_unit, to_unit, category)
    if result is not None:
        st.success(f"{value} {from_unit} = {result:.2f} {to_unit}")
    else:
        st.error("Conversion not possible!")

# Footer
st.markdown("<p style='text-align: center; color: grey;'>Made by Madiha</p>", unsafe_allow_html=True)
