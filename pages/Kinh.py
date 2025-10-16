import streamlit as st

st.title("Bible")
st.markdown("""
Explore Buddhist texts and sutras.  
Soon you'll be able to choose from variants like *Dhammapada*, *Lotus Sutra*, and more.
""")

col1, col2 = st.columns(2)
with col1:
    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1d/Dhammapada-Manuscript.jpg", caption="Dhammapada Manuscript", use_container_width=True)
with col2:
    st.info("Reading view and text browser coming soon 🌸")
