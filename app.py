import streamlit as st
import math

# Set page configuration for a wider layout and a custom title
st.set_page_config(page_title="Advanced Calculator", page_icon="🔢", layout="centered")

# Custom CSS for enhanced styling
st.markdown("""
    <style>
    .main {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
    }
    .stButton>button {
        background-color: #4CAF50;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stNumberInput, .stSelectbox {
        background-color: white;
        border-radius: 5px;
        padding: 10px;
    }
    .result {
        font-size: 20px;
        font-weight: bold;
        color: #2e7d32;
        background-color: #e8f5e9;
        padding: 15px;
        border-radius: 8px;
        margin-top: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #e3f2fd;
        padding: 15px;
        border-radius: 8px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with instructions and app info
with st.sidebar:
    st.header("📖 Instructions")
    st.markdown("""
    1. Enter two numbers (a and b) in the input fields.
    2. Select an operator from the dropdown menu.
    3. Click **Calculate** to see the result.
    4. Use **Clear** to reset the inputs.
    - For **Square Root** and **Factorial**, ensure inputs are valid (non-negative).
    - Avoid division or modulo by zero.
    """)
    st.markdown("**Created by:** Naveen")
    st.markdown("**Version:** 1.0")

# Main content
st.title("🔢 Advanced Calculator")
st.markdown("A sleek and powerful calculator for all your mathematical needs!")

# Optional image banner (user can add their own image)
# To add an image, upload it to your project directory or use a URL
# Example: st.image("path_to_image.jpg", use_column_width=True)
st.markdown("<!-- Placeholder for image banner -->")
# If you have an image, uncomment and update the line below with the correct path or URL
# st.image("https://example.com/calculator_banner.jpg", use_column_width=True, caption="Calculator Banner")

# Input section with columns for better layout
col1, col2 = st.columns(2)
with col1:
    a = st.number_input("Enter first number (a):", value=0.0, step=0.1, format="%.2f")
with col2:
    b = st.number_input("Enter second number (b):", value=0.0, step=0.1, format="%.2f")

# Operator selection
operator = st.selectbox(
    "Choose an operator:",
    [
        "Addition (+)",
        "Subtraction (-)",
        "Multiplication (*)",
        "Division (/)",
        "Power (a^b)",
        "Modulo (a % b)",
        "Square Root (√a, √b)",
        "Factorial (a!, b!)"
    ],
    help="Select the operation to perform"
)

# Calculation function
def calculator(a, b, operator):
    try:
        if operator == "Addition (+)":
            return f"{a} + {b} = {a + b:.2f}"
        elif operator == "Subtraction (-)":
            return f"{a} - {b} = {a - b:.2f}"
        elif operator == "Multiplication (*)":
            return f"{a} × {b} = {a * b:.2f}"
        elif operator == "Division (/)":
            if b == 0:
                return "❌ Cannot divide by zero"
            return f"{a} ÷ {b} = {a / b:.2f}"
        elif operator == "Power (a^b)":
            return f"{a} ^ {b} = {a ** b:.2f}"
        elif operator == "Modulo (a % b)":
            if b == 0:
                return "❌ Cannot perform modulo by zero"
            return f"{a} % {b} = {a % b:.2f}"
        elif operator == "Square Root (√a, √b)":
            sqrt_a = math.sqrt(a) if a >= 0 else "Invalid"
            sqrt_b = math.sqrt(b) if b >= 0 else "Invalid"
            return f"√{a} = {sqrt_a:.2f}, √{b} = {sqrt_b:.2f}" if isinstance(sqrt_a, float) and isinstance(sqrt_b, float) else f"√{a} = {sqrt_a}, √{b} = {sqrt_b}"
        elif operator == "Factorial (a!, b!)":
            if a < 0 or b < 0 or a != int(a) or b != int(b):
                return "❌ Factorial only defined for non-negative integers"
            return f"{int(a)}! = {math.factorial(int(a))}, {int(b)}! = {math.factorial(int(b))}"
        else:
            return "Invalid operator"
    except Exception as e:
        return f"❌ Error: {str(e)}"

# Button section with columns
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Calculate", key="calc"):
        result = calculator(a, b, operator)
        st.markdown(f'<div class="result">✅ Result: {result}</div>', unsafe_allow_html=True)
with col2:
    if st.button("Clear", key="clear"):
        st.rerun()

# Footer
st.markdown("---")
st.markdown("💻 Built with Streamlit | © 2025 Naveen")
