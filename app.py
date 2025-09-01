import streamlit as st

st.title("Realistic Calculator")

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

st.text_area("Calculator Display:", st.session_state.expression, height=100, key="display")

cols = st.columns(4)

buttons = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('0', '.', 'C', '+'),
]

for row in buttons:
    for i, btn in enumerate(row):
        if cols[i].button(btn):
            if btn == 'C':
                clear_expression()
            else:
                add_to_expression(btn)

if st.button("="):
    calculate_result()

# Reset button to clear expression
if st.button("Reset"):
    clear_expression()
