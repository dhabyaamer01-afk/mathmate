import streamlit as st
import sympy as sp

# -------------------------
# MathMate - Simple Dark App
# -------------------------

st.set_page_config(page_title="MathMate", page_icon="🧠")

# Dark theme styling
st.markdown(
    """
    <style>
    .stApp {
        background-color: #0f1117;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("🧠 MathMate")
st.write("Solve math easily by typing your problem below")

# Input
problem = st.text_input("Enter math problem (example: x^2 + 2*x + 1)")

mode = st.selectbox(
    "Choose what to do",
    ["Calculate", "Simplify", "Solve", "Differentiate", "Integrate"]
)

x = sp.Symbol('x')

# Button
if st.button("Solve"):
try:
    expr = sp.sympify(problem)

    if mode == "Calculate":
        result = expr.evalf()
        st.success(result)

    elif mode == "Simplify":
        result = sp.simplify(expr)
        st.success(result)

    elif mode == "Solve":
        result = sp.solve(expr, x)

        if len(result) == 0:
            st.warning("No solutions found")
        else:
            st.success(result)

    elif mode == "Differentiate":
        result = sp.diff(expr, x)
        st.success(result)

    elif mode == "Integrate":
        result = sp.integrate(expr, x)
        st.success(result)

except:
    st.error("Invalid input. Try something like: x**2 + 2*x + 1")

st.markdown("---")
st.caption("MathMate AI - Simple Math Solver")
