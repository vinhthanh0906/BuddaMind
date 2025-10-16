import streamlit as st
from sqlalchemy.orm import Session

import sys 

sys.path.append('/Users/nguyenthanhvinh/Documents/PYTHON/Project/BuddaMind/modules')

from modules.database import SessionLocal
from modules.models import User
from modules.auth_utils import verify_password

st.set_page_config(page_title="Login - BuddhaMind", page_icon="🪷", layout="centered")

st.title("🔐 Login to BuddhaMind")

with st.form("login_form"):
    username = st.text_input("Username or Email")
    password = st.text_input("Password", type="password")
    login_btn = st.form_submit_button("Login")

if login_btn:
    db: Session = SessionLocal()
    user = db.query(User).filter((User.username == username) | (User.email == username)).first()

    if user and verify_password(password, user.password):
        st.session_state["user"] = {"id": user.id, "username": user.username, "email": user.email}
        st.success(f"Welcome back, {user.username} 🌿")
        st.page_link("pages/3_Home.py", label="Go to Home →")
    else:
        st.error("Invalid username or password.")
    db.close()

# Logout button if user logged in
if "user" in st.session_state:
    if st.button("Logout"):
        del st.session_state["user"]
        st.info("You’ve been logged out.")
