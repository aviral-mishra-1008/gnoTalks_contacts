import sqlite3
from cryptography.fernet import Fernet
import streamlit as st

# Function to load the key
def load_key():
    return open("key.gnotalks", "rb").read()

# Streamlit UI for key input
encryption_key = load_key()

if encryption_key:
    # Initialize cipher suite with the provided key
    cipher_suite = Fernet(encryption_key)

    # Connect to the database
    conn = sqlite3.connect('gnoTalks_contactBase.db')
    cursor = conn.cursor()

    # Function to insert data into the contacts table
    def insert_contact(name, phone_number, email, remark, domain):
        encrypted_phone_number = cipher_suite.encrypt(phone_number.encode()) if phone_number else None
        cursor.execute('''INSERT INTO contacts (name, phone_number, email, remark, domain)
                          VALUES (?, ?, ?, ?, ?)''', (name, encrypted_phone_number, email, remark, domain))
        conn.commit()


    # Streamlit UI for contact details input
    name = st.text_input("Enter name")
    phone_number = st.text_input("Enter phone number (optional)", value="")
    email = st.text_input("Enter email (optional)", value="")
    remark = st.text_input("Enter remark")
    domain = st.text_input("Enter domain")

    # Validate required fields and submit
    if st.button("Submit"):
        if not name:
            st.error("Name can't be null. Please enter the name.")
        elif not remark:
            st.error("Remark can't be null. Please enter the remark.")
        elif not domain:
            st.error("Domain can't be null. Please enter the domain.")
        else:
            insert_contact(name, phone_number, email, remark, domain)
            st.success("Contact added successfully!")

    # Close the connection
    conn.close()
else:
    st.warning("Please enter the encryption key to proceed.")
