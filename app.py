import streamlit as st

st.title("Fast & Compact Calculator")

if "expression" not in st.session_state:
    st.session_state.expression = ""

def add_to_expression(char):
    st.session_state.expression += str(char)

def clear_expression():
    st.session_state.expression = ""

def calculate_result():
    try:
        result = eval(st.session_state.expression)
        st.session_state.expression = str(result)
    except Exception:
        st.session_state.expression = "Error"

# Use a disabled text_input for compact display
st.text_input("Display", value=st.session_state.expression, key="display", disabled=True)

# Define buttons including all operators you want
buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '(',
    '1', '2', '3', '-', ')',
    '0', '.', '=', '+', 'Reset'
]

cols = st.columns(5)

for i, button in enumerate(buttons):
    if cols[i % 5].button(button):
        if button == 'C':
            clear_expression()
        elif button == 'Reset':
            clear_expression()
        elif button == '=':
            calculate_result()
        else:
            add_to_expression(button)
