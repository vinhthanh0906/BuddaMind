import streamlit as st

# ==============================
# PAGE CONFIG
# ==============================
st.set_page_config(
    page_title="BuddhaMind — Digital Sutra Companion",
    page_icon="🪷",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==============================
# SIDEBAR NAVIGATION
# ==============================
st.sidebar.title("🪷 BuddhaMind")
st.sidebar.markdown("Your Digital Buddhist Bible Companion")


st.sidebar.page_link("pages/Kinh.py", label="📖 Read Bibles")
st.sidebar.page_link("pages/Hoidap.py", label="💬 Chatbot")
st.sidebar.page_link("pages/GhiChep.py", label="📝 Notes")
st.sidebar.page_link("pages/KinhNghe.py", label="Listen")


st.sidebar.divider()
st.sidebar.caption("Bible Library management ")

# ==============================
# HOME PAGE CONTENT
# ==============================
st.title("🪷 BuddhaMind — The Digital Sutra Companion")

st.markdown("""
Welcome to **BuddhaMind**, a peaceful space to explore Buddhist scriptures, reflect, and interact with teachings through an elegant web interface.

---

### 🌸 What You Can Do
- **📖 Read Bibles:** Browse Buddhist texts and sutras  
- **💬 Chatbot:** (Coming soon) Ask AI about teachings  
- **📝 Notes:** Write reflections and personal insights  
- **🪷 Teachings:** Learn about Buddhist lists and doctrines  

> “Peace comes from within. Do not seek it without.” — *The Buddha*
""")

st.image(
    "https://upload.wikimedia.org/wikipedia/commons/7/7a/Buddha_in_Sarnath_Museum_%28Dhammajak_Mutra%29.jpg",
    use_container_width=True,
    caption="Sarnath Buddha — Dhammajak Mudra"
)

st.success("🌿 Use the sidebar on the left to explore BuddhaMind.")



