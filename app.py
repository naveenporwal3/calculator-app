import streamlit as st

st.title("Simple Calculator by Naveen ")

a = st.number_input("Enter your first number:")
b = st.number_input("Enter your second number:")
operator = st.selectbox("Choose an operator:", ["+", "-", "*", "/"])

def calculator(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        if b == 0:
            return "Cannot divide by zero"
        return a / b
    else:
        return "Invalid operator"

if st.button("Calculate"):
    result = calculator(a, b, operator)
    st.success(f"Result: {result}")
