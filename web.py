import streamlit as st
from modules import functions
import time
import os

if not os.path.exists("items.txt"):
    with open("items.txt", "w") as file:
        pass

items = functions.get_items()
clock = time.strftime("%d %b %Y")

def add_item():
        item = st.session_state["new_item"] + "\n"
        items.append(item)
        functions.write_items(items)


st.title("Einkaufsliste")
st.write("Heute ist der " + clock)

col1, col2 = st.columns(2)

with col1:
    st.subheader("Das hier muss alles mit:")
    for index, item in enumerate(items):
        checkbox = st.checkbox(item, key=item)
        if checkbox:
            items.pop(index)
            functions.write_items(items)
            del st.session_state[item]
            st.experimental_rerun()

with col2:
    st.subheader("Hinzugefügt am:")
    for index, item in enumerate(items):
        st.write(clock)

st.text_input(label="Was möchtest du einkaufen?", placeholder="Hier hinzufügen...", on_change=add_item, key='new_item')