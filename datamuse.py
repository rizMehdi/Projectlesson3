import streamlit as st
import json, request

st.header('Exercise with Datamuse')
selection = st.selectbox('what do you want to know?', ('means like...', 'sounds like...', 'antonyms', 'synonims'))

keyword = st.write(input('give me word': ))

if selection = 'means like':
    url= 'https://api.datamuse.com/words?ml=' + keyword 
elif selection = 'sounds like':
    url= 'https://api.datamuse.com/words?sl=' + keyword 
elif selection = 'antonyms':
    url= 'https://api.datamuse.com/words?rel_ant=' + keyword 
else selection = 'synonims':
    url= 'https://api.datamuse.com/words?rel_syn=' + keyword 

    
