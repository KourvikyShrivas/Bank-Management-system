import streamlit as st

st.set_page_config(page_title="Bank Management System")

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Operation",
    [
        "Create Account",
        "Deposit Money",
        "Withdraw Money",
        "Show Details",
        "Delete Account"
    ]
)

if menu == "Create Account":
    st.header("Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    email = st.text_input("Email")
    pin = st.text_input("PIN", type="password")

    if st.button("Create Account"):
        st.success("Account Created Successfully!")

elif menu == "Deposit Money":
    st.header("Deposit Money")

    account = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Deposit"):
        st.success(f"₹{amount} deposited successfully!")

elif menu == "Withdraw Money":
    st.header("Withdraw Money")

    account = st.text_input("Account Number")
    amount = st.number_input("Amount", min_value=0)

    if st.button("Withdraw"):
        st.success(f"₹{amount} withdrawn successfully!")

elif menu == "Show Details":
    st.header("User Details")
    st.info("User details will appear here.")

elif menu == "Delete Account":
    st.header("Delete Account")

    account = st.text_input("Account Number")

    if st.button("Delete"):
        st.warning("Account Deleted!")