import streamlit as st
from contract import Sales
from pydantic import ValidationError

from database import save_to_postgres

def main():
    st.title("CRM System")

    email = st.text_input("Email")
    # password = st.text_input("Password", type="password")
    date = st.date_input("Date")
    hour = st.time_input("Hour")
    value = st.number_input("Value")
    quantity = st.number_input("Quantity", value=0)
    product = st.text_input("Product")

    if st.button("Save"):
        
        try:
            sales = Sales(
                email=email,
                date=date,
                hour=hour,
                value=value,
                quantity=quantity,
                product=product
            )
            
            save_to_postgres(sales)

            st.write(sales)
        
        except  ValidationError as e:
            st.error(f"Error found: {e}")

if __name__ == "__main__":
    main()
