import sqlite3
from cryptography.fernet import Fernet
import streamlit as st

# Function to load the key
def load_key():
    return open("secret.key", "rb").read()

key = load_key()
cipher_suite = Fernet(key)

# Connect to the database
conn = sqlite3.connect('gnoTalks_contactBase.db')
cursor = conn.cursor()

# Function to decrypt phone number
def decrypt_phone_number(encrypted_phone_number):
    return cipher_suite.decrypt(encrypted_phone_number).decode() if encrypted_phone_number else '-'

# Streamlit UI
st.title("Manage Contacts")

# Search contacts
st.subheader("Search Contacts")
search_name = st.text_input("Enter name to search")

if st.button("Search"):
    cursor.execute("SELECT id, name, domain FROM contacts WHERE name LIKE ?", ('%' + search_name + '%',))
    results = cursor.fetchall()
    st.session_state['results'] = results

# Check if results are available in session state
if 'results' in st.session_state:
    results = st.session_state['results']
    if results:
        st.write("Matching Contacts:")
        for row in results:
            st.write(f"ID: {row[0]}, Name: {row[1]}, Domain: {row[2]}")

        # Deletion of records
        st.subheader("Delete Contacts")
        delete_ids = st.text_input("Enter IDs to delete (comma-separated)")

        if st.button("Delete"):
            ids_to_delete = delete_ids.split(',')
            ids_to_delete = [id.strip() for id in ids_to_delete]  # Strip whitespace

            for id_to_delete in ids_to_delete:
                cursor.execute("DELETE FROM contacts WHERE id=?", (id_to_delete,))
            conn.commit()
            st.success("Selected contacts deleted successfully.")
    else:
        st.write("No matching contacts found.")

# Close the connection
conn.close()
