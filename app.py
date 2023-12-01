# app.py
import streamlit as st
import random

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    a = random.choices(letters, k=nr_letters)
    b = random.choices(numbers, k=nr_symbols)
    c = random.choices(symbols, k=nr_numbers)

    password = ''.join(random.sample((a + b + c), k=(nr_letters + nr_symbols + nr_numbers)))
    return password

def main():
    st.title("Random Password Generator")

    nr_letters = st.number_input("How many letters would you like in your password?", min_value=0, step=1)
    nr_symbols = st.number_input("How many symbols would you like?", min_value=0, step=1)
    nr_numbers = st.number_input("How many numbers would you like?", min_value=0, step=1)

    if st.button("Generate Password"):
        password = generate_password(int(nr_letters), int(nr_symbols), int(nr_numbers))
        st.success(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
