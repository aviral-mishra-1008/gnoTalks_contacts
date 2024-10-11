import sqlite3
import streamlit as st
from cryptography.fernet import Fernet

# Load the encryption key from the file
def load_key():
    return open("key.gnotalks", "rb").read()

key = load_key()
cipher_suite = Fernet(key)

# Connect to the database
conn = sqlite3.connect('gnoTalks_contactBase.db')
cursor = conn.cursor()

# Function to decrypt phone number
def decrypt_phone_number(encrypted_phone_number):
    return cipher_suite.decrypt(encrypted_phone_number).decode() if encrypted_phone_number else '-'

# Streamlit UI
st.title("Search Contacts")

# Take user input for name
search_name = st.text_input("Enter name to search")

if st.button("Search"):
    # Use wildcards to find matching names
    cursor.execute("SELECT name, phone_number, email, remark, domain FROM contacts WHERE name LIKE ?", ('%' + search_name + '%',))
    results = cursor.fetchall()

    if results:
        # Display results in a table
        for row in results:
            name, encrypted_phone_number, email, remark, domain = row
            phone_number = decrypt_phone_number(encrypted_phone_number)
            st.write(f"**Name:** {name if name else '-'}")
            st.write(f"**Phone Number:** {phone_number if phone_number else '-'}")
            st.write(f"**Email:** {email if email else '-'}")
            st.write(f"**Remark:** {remark if remark else '-'}")
            st.write(f"**Domain:** {domain if domain else '-'}")
            st.write("-----------------------------------------------------------------------")
    else:
        st.write("No matching contacts found.")

# Close the connection
conn.close()
