import streamlit as st
import link_utils

st.title("Blocked Websites Manager")

links = st.text_input("Enter a URL to add to the blocklist:")
links = link_utils.link_cleaner(links)

links_per_line = ""
for link in links:
    links_per_line += f"{link}\n"   

if links_per_line != "":
    st.download_button("Download formatted links", links_per_line)