import streamlit as st
import math

st.title("🔢 Advanced Calculator by Naveen")

# Input numbers
a = st.number_input("Enter your first number:", value=0.0)
b = st.number_input("Enter your second number:", value=0.0)

# Operator selection
operator = st.selectbox(
    "Choose an operator:", 
    ["+", "-", "*", "/", "Power (a^b)", "Modulo (a % b)", "Square Root (√a, √b)", "Factorial (a!, b!)"]
)

# Calculation function
def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "❌ Cannot divide by zero"
        return a / b
    elif operator == "Power (a^b)":
        return a ** b
    elif operator == "Modulo (a % b)":
        if b == 0:
            return "❌ Cannot perform modulo by zero"
        return a % b
    elif operator == "Square Root (√a, √b)":
        return f"√a = {math.sqrt(a) if a >= 0 else 'Invalid'}, √b = {math.sqrt(b) if b >= 0 else 'Invalid'}"
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
