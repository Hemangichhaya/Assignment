import streamlit as st
import time
from spacy_model_ner import extract_entity
import sys
sys.path.append('C:/Users/Brij Chavda/Desktop/UserReady_assignment/assignments/assignment1_new/assignment1')
uploaded_file = st.file_uploader("Choose a file", type=['.docx', '.png'])
correct_labels = ['Party One', 'Agreement End Date', 'Renewal Notice (Days)', 'Party Two', 'Agreement Start Date', 'Agreement Value']
if uploaded_file is not None:
    with open(uploaded_file.name, 'wb') as file:
        file.write(uploaded_file.getvalue())
    with st.spinner():
        val_dictionary = extract_entity('./models/split_fixedlen_main', uploaded_file.name, '.')
        labels = ['Party One', 'Aggrement End Date', 'Renewal Notice (Days)', 'Party Two', 'Aggrement Start Date', 'Aggrement Value']
        for idx, label in enumerate(labels):
            if label in val_dictionary:
                st.text_area(label=correct_labels[idx],value=val_dictionary[label])
            else:
                st.text_area(label=correct_labels[idx],value='None')


