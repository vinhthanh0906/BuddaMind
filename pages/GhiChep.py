import streamlit as st

st.title("Kinh Doc")
st.markdown("""
Write and save reflections as you read or meditate.  
For now, this is just a design preview — database integration coming later.
""")

st.text_area("Write your note here...", height=200)
st.button("💾 Save Note", type="primary")
st.info("Saving feature will be enabled once database is added 🙏")
