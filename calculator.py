import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="GRAPHIC CALCULATOR")

# --- Session Setup ---
if "expression" not in st.session_state:
    st.session_state.expression = ""


# --- Title ---
st.title("GRAPHIC CALCULATOR")

# --- Expression Display ---
st.markdown(f"""
<div style='
    font-size: 32px;
    padding: 15px;
    border-radius: 10px;
    text-align: right;
    border: 2px solid #888;
    margin-bottom: 10px;
'>
    {st.session_state.expression if st.session_state.expression else "0"}
</div>
""", unsafe_allow_html=True)

# --- Button Click Handler ---
def button_click(label):
    if label.strip() == "=":
        try:
            st.session_state.expression = str(eval(
                st.session_state.expression.replace("×", "*").replace("÷", "/")
            ))
        except:
            st.session_state.expression = "Error"
    elif label.strip() == "C":
        st.session_state.expression = ""
    else:
        st.session_state.expression += label.strip()

# --- Buttons Layout ---
buttons = [
    ["7", "8", "9", "÷"],
    ["4", "5", "6", "×"],
    ["1", "2", "3", "-\u00A0"],
    ["0", "C", "=", "+\u00A0"]
]

for row in buttons:
    cols = st.columns(len(row))
    for i, label in enumerate(row):
        if cols[i].button(label, key=f"{label}_{i}"):
            button_click(label)
            st.rerun()

# --- Optional Manual Input ---
with st.form("manual_input"):
    expr = st.text_input("Or type an expression:", value=st.session_state.expression)
    submit = st.form_submit_button("Calculate")
    if submit:
        try:
            st.session_state.expression = str(eval(expr.replace("×", "*").replace("÷", "/")))
        except:
            st.session_state.expression = "Error"
        st.rerun()
