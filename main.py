# Fix sqlite3 compatibility for Streamlit Cloud
import sys
sys.modules["sqlite3"] = __import__("pysqlite3")

import streamlit as st
from rag import process_urls, generate_answer


st.markdown(
    """
    <div style='text-align: center; font-size: 12px; color: gray;'>
        Created By Rohesen ♥️
    </div>
    """,
    unsafe_allow_html=True
)


st.title("Real Estate Research Tool")

url1 = st.sidebar.text_input("URL 1")
url2 = st.sidebar.text_input("URL 2")
url3 = st.sidebar.text_input("URL 3")

placeholder = st.empty()

process_url_button = st.sidebar.button("Process URLs")
if process_url_button:
    urls = [url for url in (url1, url2, url3) if url!= '']
    if len(urls)==0:
        placeholder.text("You must provide at least one valid url")

    else:
        for status in process_urls(urls):
            placeholder.text(status)

query = placeholder.text_input("Question")
if query:
    try:
        answer, sources = generate_answer(query)
        st.header("Answer:")
        st.write(answer)

        if sources:
            st.subheader("Sources:")
            st.write(sources)

    except RuntimeError as e:
        placeholder.text("You must process urls first")
