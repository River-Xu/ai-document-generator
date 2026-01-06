import streamlit as st
from generator import generate

st.set_page_config(page_title="AI Document Generator", layout="wide")
st.title("AI Document Generator")

doc_type = st.selectbox("Document Type", ["prd", "test_plan", "meeting_summary"])
raw = st.text_area("Input Text", height=240, placeholder="Paste raw notes or requirements here")

if st.button("Generate Document", type="primary"):
    if not raw.strip():
        st.error("Please provide input text")
    else:
        with st.spinner("Generating document..."):
            out = generate(doc_type, raw)
        st.markdown("## Result")
        st.markdown(out)
