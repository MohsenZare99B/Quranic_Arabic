import streamlit as st
from utils import random_verse, get_verse

# Initialize session state variables if they do not exist
if 'text' not in st.session_state:
    st.session_state['text'] = None
if 'show_translation' not in st.session_state:
    st.session_state['show_translation'] = False
if 'translation' not in st.session_state:
    st.session_state['translation'] = None
if 'verses' not in st.session_state:
    st.session_state['verses'] = []

def generate_verse(surah_number, ayah_range):
    """Generates a random verse and updates the session state."""
    surah, ayah, text, translation = random_verse(Surah=surah_number, Ayah_range=ayah_range)
    st.session_state['text'] = f"<p style='text-align: center;'><b>{surah} {ayah}</b> : {text}</p>"
    st.session_state['show_translation'] = False
    st.session_state['translation'] = f"<p style='text-align: center;'>{translation}</p>"

def display_text_and_translation():
    """Displays the text and its translation, with a button to show the translation."""
    if st.session_state['text']:
        st.markdown(st.session_state['text'], unsafe_allow_html=True)
        if not st.session_state['show_translation']:
            if st.button("Show Translation", key="show_translation_main"):
                st.session_state['show_translation'] = True
                st.experimental_rerun()  # Rerun the app to update the state
        else:
            st.markdown(st.session_state['translation'], unsafe_allow_html=True)

def display_verses_and_translations(iter_range=5):
    """Displays the verses and their translations, with buttons to show the translations."""
    if len(st.session_state['verses']) == 0:
        return
    besmellah = get_verse(1, (1, 1))[0]["text"]
    st.markdown(f"<h6 style='text-align: center;'>{besmellah}</h6>", unsafe_allow_html=True)    
    verses = st.session_state['verses']
    for i in range(0, len(verses), iter_range):
        if i + iter_range > len(verses):
            end = len(verses)
        else:
            end = i + iter_range
        text = f""
        for j in range(i, end):
            text += f'<b>{verses[j]["text"]}</b> {verses[j]["number"]}&nbsp;&nbsp;&nbsp;&nbsp;'
        text = '<p style="text-align: center;">' + text + '</p>'
        st.markdown(text, unsafe_allow_html=True)
        translations = f""
        for j in range(i, end):
            translations += f'{verses[j]["translation"]} {verses[j]["number"]}&nbsp;&nbsp;&nbsp;&nbsp;'
        translations = '<p style="text-align: center;">' + translations + '</p>'
        st.markdown(translations, unsafe_allow_html=True)
        st.write("---")  # Separator between verses

# Layout for input fields in the same row
col1, col2, col3 = st.columns(3)

with col1:
    surah_number = st.number_input("Enter the Surah number", value=12, key="surah_number_1")

with col2:
    ayah_start = st.number_input("Start of Ayah range", value=1, key="ayah_start_1")

with col3:
    ayah_end = st.number_input("End of Ayah range", value=-1, key="ayah_end_1")

ayah_range = (ayah_start, ayah_end)

# Generate button to fetch a random verse
if st.button("Choose a random verse", key="generate_1"):
    generate_verse(surah_number, ayah_range)

# Display generated text and translation button
display_text_and_translation()
st.markdown("---")

# Layout for input fields in the same row
col1, col2, col3, col4 = st.columns(4)

with col1:
    entire_surah = st.number_input("Enter the Surah number", value=114, key="surah_number_2")

with col2:
    entire_ayah_start = st.number_input("Start of Ayah range", value=1, key="ayah_start_2")

with col3:
    entire_ayah_end = st.number_input("End of Ayah range", value=-1, key="ayah_end_2")
with col4:
    iter_range = st.number_input("NO. Verses per iteration", value=5, key="iter_range", min_value=1)

if st.button("Get selected verses", key="get_verses"):
    st.session_state['verses'] = get_verse(entire_surah, (entire_ayah_start, entire_ayah_end))
    st.session_state['translations_shown'] = [False] * len(st.session_state['verses'])
    st.experimental_rerun()

# Display the verses and translation buttons
display_verses_and_translations(iter_range=iter_range)