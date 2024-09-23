import streamlit as st


def main():
    st.title("CRM System")

    email = st.text_input("Email")
    # password = st.text_input("Password", type="password")
    date = st.date_input("Date")
    hour = st.time_input("Hour")
    value = st.number_input("Value")
    quantity = st.number_input("Quantity")
    product = st.text_input("Product")

    if st.button("Login"):
        st.success("Logged in as {}".format(email))


main()
