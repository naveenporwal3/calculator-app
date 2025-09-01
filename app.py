import streamlit as st

st.title("Faster Calculator")

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

st.text_input("Display", value=st.session_state.expression, disabled=True, key="display")

buttons = [
    '7', '8', '9', '/', 'C',
    '4', '5', '6', '*', '(',
    '1', '2', '3', '-', ')',
    '0', '.', '=', '+', 'Reset'
]

cols = st.columns(5)

# To avoid multiple state changes in one rerun, use a flag variable
clicked_button = None

for i, button in enumerate(buttons):
    if cols[i % 5].button(button):
        clicked_button = button

# Process only after all buttons checked, to avoid multiple triggers
if clicked_button:
    if clicked_button == 'C' or clicked_button == 'Reset':
        clear_expression()
    elif clicked_button == '=':
        calculate_result()
    else:
        add_to_expression(clicked_button)
