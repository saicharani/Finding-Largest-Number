import streamlit as st

st.write("""
Largest among 3 numbers 
""")
#Get Input

def find_largest(num1, num2, num3):
    if (a>=b) and (a>=c): return a
    elif (b>=a) and (b>=c): return b
    else: return c

def main():
    num1 = st.number_input("Enter the first number:")
    num2 = st.number_input("Enter the second number:")
    num3 = st.number_input("Enter the third number:")
    
    if st.button("Find Largest"):
        largest = find_largest(num1, num2, num3)
        st.write(f"The largest number is: {largest}")

if __name__ == "__main__":
    main()
