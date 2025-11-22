
import streamlit as st
import pdfplumber
from transformers import pipeline
from database import save_document
from gpt_explainer import explain_text

st.title("📄 GenAI Document Intelligence – Pro Edition")

summarizer=pipeline("summarization",model="sshleifer/distilbart-cnn-12-6")

uploaded=st.file_uploader("Upload PDF Document")

if uploaded:
    with pdfplumber.open(uploaded) as pdf:
        text=" ".join([p.extract_text() or "" for p in pdf.pages])

    st.subheader("Extracted Text")
    st.write(text[:2000]+"...")

    if st.button("Summarize"):
        summary=summarizer(text[:3000])[0]["summary_text"]
        st.subheader("AI Summary")
        st.write(summary)

        explanation=explain_text(text)
        st.subheader("GPT Insights")
        st.write(explanation)

        save_document(text, summary, explanation)
        st.success("Saved to database!")
