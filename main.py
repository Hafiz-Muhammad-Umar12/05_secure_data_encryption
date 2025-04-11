import streamlit as st
from cryptography.fernet import Fernet

# Set the page config at the very top
st.set_page_config(page_title="🔐 Secure Encryption App", layout="centered")

# Generate or load a key (in a real app, store this securely!)
@st.cache_data
def get_key():
    return Fernet.generate_key()

key = get_key()
cipher = Fernet(key)

# UI Setup
st.title("🔐 Secure Data Encryption System")
st.caption("Built with Python and Streamlit")

# Tabs for encryption and decryption
tab1, tab2 = st.tabs(["🔒 Encrypt", "🔓 Decrypt"])

# Encryption Tab
with tab1:
    st.subheader("🔒 Encrypt Text")
    text_to_encrypt = st.text_area("Enter text to encrypt:")
    if st.button("Encrypt"):
        if text_to_encrypt:
            encrypted = cipher.encrypt(text_to_encrypt.encode())
            st.success("Encrypted Text:")
            st.code(encrypted.decode())
        else:
            st.warning("Please enter some text to encrypt.")

# Decryption Tab
with tab2:
    st.subheader("🔓 Decrypt Text")
    encrypted_text = st.text_area("Enter encrypted text:")
    if st.button("Decrypt"):
        try:
            decrypted = cipher.decrypt(encrypted_text.encode())
            st.success("Decrypted Text:")
            st.code(decrypted.decode())
        except Exception as e:
            st.error("❌ Decryption failed. Make sure you enter valid encrypted text.")
