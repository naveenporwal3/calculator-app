import streamlit as st
import math

st.title("🔢 Advanced Calculator by Naveen")

# Input numbers
a = st.number_input("Enter your first number (a):", value=0.0)
b = st.number_input("Enter your second number (b):", value=0.0)

# Operator selection
operator = st.selectbox(
    "Choose an operator:", 
    ["+", "-", "*", "/", "Power (a^b)", "Modulo (a % b)", "Square Root (√a, √b)", "Factorial (a!, b!)"]
)

# Calculation function
def calculator(a, b, operator):
    if operator == "+":
        return f"{a} + {b} = {a + b}"
    elif operator == "-":
        return f"{a} - {b} = {a - b}"
    elif operator == "*":
        return f"{a} × {b} = {a * b}"
    elif operator == "/":
        if b == 0:
            return "❌ Cannot divide by zero"
        return f"{a} ÷ {b} = {a / b}"
    elif operator == "Power (a^b)":
        return f"{a} ^ {b} = {a ** b}"
    elif operator == "Modulo (a % b)":
        if b == 0:
            return "❌ Cannot perform modulo by zero"
        return f"{a} % {b} = {a % b}"
    elif operator == "Square Root (√a, √b)":
        sqrt_a = math.sqrt(a) if a >= 0 else "Invalid"
        sqrt_b = math.sqrt(b) if b >= 0 else "Invalid"
        return f"√a = {sqrt_a}, √b = {sqrt_b}"
    elif operator == "Factorial (a!, b!)":
        if a < 0 or b < 0:
            return "❌ Factorial not defined for negative numbers"
        return f"a! = {math.factorial(int(a))}, b! = {math.factorial(int(b))}"
    else:
        return "Invalid operator"

# Button to calculate
if st.button("Calculate"):
    result = calculator(a, b, operator)
    st.success(f"✅ Result: {result}")

# Reset button
if st.button("Clear"):
    st.experimental_rerun()
