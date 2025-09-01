import streamlit as st

import codecs

import streamlit.components.v1 as stc

def st_calculator(calc_html,width=700,height=500):
    calc_file = codecs.open(calc_html,'r')
    page = calc_file.read()
    stc.html(page,width=width,height=height,scrolling=False)

def main():
    menu= ["simple Calculator","Advance Calculator","BMI Calculator","About"]
    choice = st.sidebar.selectbox("Menu:",menu)
    
    if(choice==  "Advance Calculator"):
        st.subheader("Advance Calculator")
        st_calculator('advance.html')
        st.sidebar.write("A scientific calculator for complex calculations.")
        st.sidebar.write("Keys:")
        st.sidebar.write("🔹0–9 → Numbers.")
        st.sidebar.write("🔹+, -, *, / → Arithmetic operators.")
        st.sidebar.write("🔹(, ) → Grouping of expressions.")
        st.sidebar.write("🔹. → Decimal point.")
        st.sidebar.write("🔹C → Clear all input.")
        st.sidebar.write("🔹<-- → Backspace (delete one character).")
        st.sidebar.write("🔹= → Show result.")
        st.sidebar.write("🔹π → Insert value of Pi (3.14159).")
        st.sidebar.write("🔹mod → Modulus (remainder after division).")
        st.sidebar.write("🔹n! → Factorial.")
        st.sidebar.write("🔹ln → Natural logarithm.")
        st.sidebar.write("🔹√ → Square root.")
        st.sidebar.write("🔹x² → Square of a number.")
        st.sidebar.write("🔹10ˣ → Power of 10.")
        st.sidebar.write("🔹cos, sin, tan → Trigonometric functions.")
        
    elif choice== "About":
        st.subheader("About app")
        st.write("Welcome to the Multi-Functional Online Calculator — a powerful yet simple tool designed to meet all your basic and advanced calculation needs in one place.")
        st.write("🔹 Whether you want to add, subtract, multiply, or divide,")
        st.write("🔹 Solve scientific and trigonometric problems, or")
        st.write("🔹 Calculate your Body Mass Index (BMI) for fitness tracking —")
        st.write("this calculator is here to help you, anytime, anywhere!")
        st.write("It is lightweight, user-friendly, and works directly in your browser without needing installation.")
        
    elif(choice== "simple Calculator"):
        st.subheader("Simple Calculator")
        st_calculator('calculator.html')
        st.sidebar.write("A standard calculator for everyday math.")
        st.sidebar.write("Keys:")
        st.sidebar.write("🔹0–9 → Number inputs.")
        st.sidebar.write("🔹+, -, *, / → Basic arithmetic operators.")
        st.sidebar.write("🔹(, ) → Parentheses for expressions.")
        st.sidebar.write("🔹. → Decimal point.")
        st.sidebar.write("🔹C → Clear all input.")
        st.sidebar.write("🔹Del → Delete the last digit/character.")
        st.sidebar.write("🔹= → Show result.")
    else:
        st.subheader("Body to Mass Index (BMI)")
        st_calculator('bmi.html')
        st.sidebar.write("A health tool to check Body Mass Index.")
        st.sidebar.write("Keys/Fields:")
        st.sidebar.write("🔹Height (in cm) → Enter your height.")
        st.sidebar.write("🔹Weight (in kg) → Enter your weight.")
        st.sidebar.write("🔹Calculate → Compute your BMI value.")
        st.sidebar.write("🔹Clear → Reset the fields.")
        st.sidebar.write("🔹Output: BMI result with category (e.g., Underweight, Normal, Overweight, Obese).")
        
        
main()