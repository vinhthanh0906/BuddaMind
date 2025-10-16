import streamlit as st
import sys 

sys.path.append('/Users/nguyenthanhvinh/Documents/PYTHON/Project/BuddaMind/modules')

from sqlalchemy.orm import Session
from modules.database import SessionLocal
from modules.models import User
from modules.auth_utils import hash_password

st.set_page_config(page_title="Sign Up - BuddhaMind", page_icon="🪷", layout="centered")

st.title("🪷 Create a BuddhaMind Account")

with st.form("signup_form"):
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    submit = st.form_submit_button("Create Account")

if submit:
    if password != confirm:
        st.error("Passwords do not match.")
    elif not username or not email:
        st.error("Please fill all fields.")
    else:
        db: Session = SessionLocal()
        existing_user = db.query(User).filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            st.warning("User already exists.")
        else:
            new_user = User(
                username=username,
                email=email,
                password=hash_password(password)
            )
            db.add(new_user)
            db.commit()
            st.success("✅ Account created successfully! You can now log in.")
        db.close()
